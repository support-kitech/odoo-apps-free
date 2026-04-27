from odoo import fields, models


class Website(models.Model):
    _inherit = 'website'

    inquiry_message = fields.Text(
        string='Inquiry Message',
        help="Message sent with product inquiries.",
        default="I'm interested in knowing the details of this product.",
    )
