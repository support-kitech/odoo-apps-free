# -*- coding: utf-8 -*-
# Copyright 2025 Khichdi Infotech

from odoo import api, fields, models


class Website(models.Model):
    _inherit = 'website'

    google_tag_manager_key = fields.Char('Google Tag Manager Key')
