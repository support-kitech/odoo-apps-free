from odoo import fields, models
from urllib.parse import quote_plus


class Website(models.Model):
    _inherit = 'website'

    whatsapp_number = fields.Char(string='Whatsapp Number', help="Your WhatsApp mobile number")


    def _get_whatsapp_link(self, message=None):
        self.ensure_one()
        if not self.whatsapp_number:
            return False
        normalized_number = self.whatsapp_number.replace(' ', '').replace('+', '')
        encoded_message = quote_plus(message or "")
        if encoded_message:
            return "https://wa.me/%s?text=%s" % (normalized_number, encoded_message)
        return "https://wa.me/%s" % normalized_number
