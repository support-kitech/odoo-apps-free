from odoo import api, fields, models, _
from odoo.exceptions import UserError


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    whatsapp_number = fields.Char(related="website_id.whatsapp_number", readonly=False, string='Mobile Number', help="Your WhatsApp mobile number")


    @api.constrains('whatsapp_number')
    def _check_whatsapp_number(self):
        for rec in self:
            if rec.whatsapp_number:
                rec.mobile_number_validation(rec.whatsapp_number, rec.company_id.country_id)

    def mobile_number_validation(self, mobile_number, phone_country_id):
        mobile_number = (mobile_number or '').replace(' ', '')
        error_message = _("Please add mobile or phone with '+' and country code.")
        if not mobile_number.startswith('+'):
            raise UserError(error_message)

        country_code = phone_country_id.phone_code if phone_country_id else ''
        validate_code = f'+{country_code}' if country_code else '+'
        remaining_number = mobile_number.replace(validate_code, '', 1)
        if not mobile_number.startswith(validate_code) or not remaining_number.isdigit():
            raise UserError(error_message)
        return True
