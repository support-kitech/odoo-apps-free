    # -*- coding: utf-8 -*-
# Copyright © 2025 Khichdi InfoTech (https://khichdiinfotech.com)
from odoo import api, fields, models


class WebsiteConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    google_tag_manager_key = fields.Char(related='website_id.google_tag_manager_key', readonly=False)
