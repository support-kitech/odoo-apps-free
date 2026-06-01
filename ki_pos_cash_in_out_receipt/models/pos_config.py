# Copyright © 2026 Khichdi InfoTech (https://khichdiinfotech.com)

from odoo import fields, models


class PosConfig(models.Model):
    _inherit = "pos.config"

    cash_currency_ids = fields.Many2many(
        "res.currency",
        string="Cash In/Out Currencies",
        help="Currencies allowed in POS cash in/out popup.",
    )
