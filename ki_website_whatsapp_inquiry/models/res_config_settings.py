# Copyright © 2025 Khichdi InfoTech (https://khichdiinfotech.com)
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    inquiry_message = fields.Text(
        related="website_id.inquiry_message",
        readonly=False,
        string='Inquiry Message',
        help="Message sent with product inquiries.",
    )
