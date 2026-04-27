# Copyright © 2025 Khichdi InfoTech (https://khichdiinfotech.com)
{
    'name': "Website WhatsApp Product Inquiry",
    'summary': "WhatsApp product inquiry button on Odoo product pages with prefilled message.",
    'version': '19.0.1.0.0',
    'category': 'Extra Tools',
    'description': """
        Website Product WhatsApp Inquiry for Odoo 17

        Add a WhatsApp INQUIRE button on product pages so customers can quickly contact your business about any product.

        Main features:
        - WhatsApp inquiry button on Odoo eCommerce product pages
        - Prefilled inquiry message with product name
        - Website-level configurable default inquiry text
        - Smooth redirect support for WhatsApp Mobile, WhatsApp Web, and WhatsApp Desktop
        - Clean frontend styling for desktop and mobile layouts

        Best for:
        - Odoo website product inquiries
        - WhatsApp click-to-chat for eCommerce
        - Faster lead generation from product pages
        - Direct customer communication for product questions
    """,
    'author': 'Khichdi InfoTech',
    'email': 'contact@khichdiinfotech.com',
    'company': 'Khichdi InfoTech.',
    'website': 'https://www.khichdiinfotech.com/',
    'maintainer': 'Yagnesh Borad',
    'depends': ['base', 'website_sale', 'ki_website_whatsapp'],
    'data': [
        'views/res_config_settings_views.xml',
        'views/website_whatsapp_inquiry_views.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            '/ki_website_whatsapp_inquiry/static/src/css/website_whatsapp_inquiry.css',
        ],
    },
    'images': ['static/description/banner.png', 'static/description/icon.png'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
