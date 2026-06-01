# Copyright © 2026 Khichdi InfoTech (https://khichdiinfotech.com)

from odoo import _, fields, models
from odoo.exceptions import UserError


class PosSession(models.Model):
    _inherit = "pos.session"

    def format_currency_amount_cash(self, amount, currency_id=False):
        currency = (
            self.env["res.currency"].browse(int(currency_id))
            if currency_id
            else self.env.company.currency_id
        )
        if currency.position == "before":
            return f"{currency.symbol}\u00A0{amount}"
        return f"{amount}\u00A0{currency.symbol}"

    def _get_cash_in_out_payment_method(self):
        self.ensure_one()
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
        return payment_method

    def _prepare_account_bank_statement_line_vals(
        self, session, sign, amount, reason, partner_id, extras
    ):
        payment_method = session._get_cash_in_out_payment_method()
        company_currency = self.env.company.currency_id
        selected_currency = (
            self.env["res.currency"].browse(int(extras["currency_id"]))
            if extras.get("currency_id")
            else company_currency
        )
        converted_amount = amount
        if selected_currency != company_currency:
            converted_amount = selected_currency._convert(
                amount, company_currency, self.env.company, fields.Date.today()
            )

        vals = super()._prepare_account_bank_statement_line_vals(
            session, sign, converted_amount, reason, partner_id, extras
        )
        vals["journal_id"] = payment_method.journal_id.id
        if selected_currency != company_currency:
            vals.update(
                {
                    "foreign_currency_id": selected_currency.id,
                    "amount_currency": sign * amount,
                }
            )
        return vals

    def try_cash_in_out(self, _type, amount, reason, partner_id, extras):
        sign = 1 if _type == "in" else -1
        sessions = self.filtered("cash_journal_id")
        if not sessions:
            raise UserError(_("There is no cash payment method for this PoS Session"))

        vals_list = [
            self._prepare_account_bank_statement_line_vals(
                session, sign, amount, reason, partner_id, extras
            )
            for session in sessions
        ]
        self.env["account.bank.statement.line"].with_context(
            no_retrieve_partner=True
        ).create(vals_list)

        message_lines = [
            f"Cash {extras['translatedType']}",
            f"- Amount: {extras.get('formattedAmountSymbol', extras.get('formattedAmount'))}",
        ]
        if reason:
            message_lines.append(f"- Reason: {reason}")
        self.message_post(body="<br/>\n".join(message_lines))
