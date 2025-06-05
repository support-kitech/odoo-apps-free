
{
    'name': 'Google Tag Manager',
    'category': 'Website',
    'summary': 'Google Tag Manager - Odoo integration',
    'version': '16.0.1.0',
    'description': '''
Includes Google Tag Manager HTML elements in the website metadata
    ''',
    'website' : "https://khichdiinfotech.com/",
    "support" : "contact@khichdiinfotech.com",
    'author'  : "Khichdi InfoTech",
    "license": "OPL-1",
    'depends': [
        'website_sale',
    ],
    'data': [
        'templates/website_layout.xml',
        'views/website_config_settings.xml',
    ],
    'installable': True,
    'application': False,
}
