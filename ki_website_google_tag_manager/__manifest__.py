
{
    'name': 'Google Tag Manager',
    'category': 'Website',
    'summary': 'Google Tag Manager - Odoo integration',
    'version': '17.0.1.0',
    'description': '''
Includes Google Tag Manager HTML elements in the website metadata
    ''',
    'website' : "https://khichdiinfotech.com/",
    "support" : "contact@khichdiinfotech.com",
    'author'  : "Khichdi InfoTech",
    "license": "LGPL-3",
    'images': ['static/description/banner.png', 'static/description/icon.png'],
    'depends': [
        'website_sale_delivery',
    ],
    'data': [
        'templates/website_layout.xml',
        'views/website_config_settings.xml',
    ],
    'installable': True,
    'application': False,
}
