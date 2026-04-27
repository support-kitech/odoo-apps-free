{
    'name': "Website WhatsApp",
    'summary': "Floating WhatsApp chat button for Odoo Website with configurable mobile number.",
    'version': '18.0.1.0.0',
    'category': 'Extra Tools',
    'description': """
        Website WhatsApp Chat Button for Odoo 17

        This module adds a floating WhatsApp button on your Odoo website so visitors can start instant chat with your business.

        Main features:
        - Floating WhatsApp icon on all website pages
        - Website-level WhatsApp mobile number configuration
        - Mobile number validation with country code
        - Clean responsive design and lightweight frontend assets
        - Easy setup from Website Settings

        Best for:
        - Odoo website WhatsApp integration
        - WhatsApp live chat on website
        - Click to chat button for Odoo
        - Customer inquiry and lead generation from website pages
    """,
    'author': 'Khichdi InfoTech',
    'email': 'contact@khichdiinfotech.com',
    'company': 'Khichdi InfoTech.',
    'website': 'https://www.khichdiinfotech.com/',
    'maintainer': 'Yagnesh Borad',
    'depends': ['base','website'],
    'data': [
        'views/res_config_settings_views.xml',
        'views/website_whatsapp_views.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            '/ki_website_whatsapp/static/src/css/website_whatsapp.css',
        ],
    },
    'images': ['static/description/banner.png', 'static/description/icon.png'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
