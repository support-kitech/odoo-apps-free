# Copyright © 2025 Khichdi InfoTech (https://khichdiinfotech.com)
import werkzeug
from odoo import http
from odoo.http import request
from urllib.parse import quote_plus
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSale(WebsiteSale):

    @http.route(['/whatsapp/inquiry/<int:product>'], type='http', auth="public", website=True)
    def whatsapp_product_inquiry(self, product, **kw):

        website = request.website.get_current_website()
        product_obj = request.env['product.product'].browse(product)
        inquiry_message = ''
        if website and website.inquiry_message:
            inquiry_message = website.inquiry_message
        message = (inquiry_message + '\nProduct Url: ' + request.website.get_base_url() + product_obj.website_url)
        encoded_message = quote_plus(message)
        return werkzeug.utils.redirect("https://wa.me/%s?text=%s" % (website.whatsapp_number, encoded_message))
