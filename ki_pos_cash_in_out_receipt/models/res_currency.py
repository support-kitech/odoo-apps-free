# Copyright © 2026 Khichdi InfoTech (https://khichdiinfotech.com)

from odoo import api, models


class ResCurrency(models.Model):
    _inherit = "res.currency"

    @api.model
    def _load_pos_data_domain(self, data, config):
        domain = super()._load_pos_data_domain(data, config)
        cash_currency_ids = config.cash_currency_ids.ids
        if not cash_currency_ids:
            return domain

        currency_ids = set(cash_currency_ids)
        if domain and domain[0][0] == "id":
            if domain[0][1] == "in":
                currency_ids.update(domain[0][2])
            elif domain[0][1] == "=":
                currency_ids.add(domain[0][2])
        return [("id", "in", list(currency_ids))]
