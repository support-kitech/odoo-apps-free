# Copyright © 2026 Khichdi InfoTech (https://khichdiinfotech.com)

from odoo import api, models


class ResCurrency(models.Model):
    _inherit = "res.currency"

    @api.model
    def _load_pos_data_domain(self, data):
        config_data = data["pos.config"]["data"][0]
        company_currency_id = self.env["res.company"].browse(
            config_data["company_id"]
        ).currency_id.id
        pos_currency_id = config_data["currency_id"]
        cash_currency_ids = config_data.get("cash_currency_ids", [])

        currency_ids = set(cash_currency_ids + [company_currency_id, pos_currency_id])
        return [("id", "in", list(currency_ids))]
