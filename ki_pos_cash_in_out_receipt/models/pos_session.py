# Copyright © 2026 Khichdi InfoTech (https://khichdiinfotech.com)

from odoo import _, fields, models
from odoo.exceptions import UserError


class PosSession(models.Model):
    _inherit = "pos.session"

    cash_currency_ids = fields.Many2many(related="config_id.cash_currency_ids")

    def _load_pos_data_fields(self, config_id):
        return super()._load_pos_data_fields(config_id=config_id) + ["cash_currency_ids"]

    def format_currency_amount_cash(self, amount, currency_id=False):
        currency = (
            self.env["res.currency"].browse(int(currency_id))
            if currency_id
            else self.env.company.currency_id
        )
        if currency.position == "before":
            return f"{currency.symbol}\u00A0{amount}"
        return f"{amount}\u00A0{currency.symbol}"

    def try_cash_in_out(self, _type, amount, reason, extras):
        sign = 1 if _type == "in" else -1
        company_currency = self.env.company.currency_id

        payment_methods = self.payment_method_ids.filtered("is_cash_count").filtered(
            "cash_in_out"
        )
        if len(payment_methods) > 1:
            raise UserError(
                _(
                    "Multiple cash payment methods are configured for cash in/out on POS '%s'. "
                    "Only one cash payment method per shop can be enabled.",
                    self.config_id.name,
                )
            )
        payment_method = payment_methods[:1]
        if not payment_method or not payment_method.journal_id:
            raise UserError(
                _(
                    "There is no cash payment method configured for cash in/out on POS '%s'. "
                    "Enable 'Use For POS Cash In/Out' on exactly one cash payment method.",
                    self.config_id.name,
                )
            )

        selected_currency = (
            self.env["res.currency"].browse(int(extras["currency_id"]))
            if extras.get("currency_id")
            else company_currency
        )
        converted_amount = selected_currency._convert(
            amount, company_currency, self.env.company, fields.Date.today()
        )

        self.env["account.bank.statement.line"].create(
            [
                {
                    "pos_session_id": session.id,
                    "journal_id": payment_method.journal_id.id,
                    "amount": sign * converted_amount,
                    "date": fields.Date.context_today(session),
                    "payment_ref": "-".join([session.name, extras["translatedType"], reason]),
                    "foreign_currency_id": (
                        selected_currency.id
                        if selected_currency.id != company_currency.id
                        else False
                    ),
                    "amount_currency": (
                        sign * amount
                        if selected_currency.id != company_currency.id
                        else False
                    ),
                }
                for session in self.filtered("cash_journal_id")
            ]
        )

        message_lines = [
            f"Cash {extras['translatedType']}",
            f"- Amount: {extras['formattedAmountSymbol']}",
        ]
        if reason:
            message_lines.append(f"- Reason: {reason}")
        self.message_post(body="<br/>\n".join(message_lines))
