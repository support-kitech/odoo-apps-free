# Copyright © 2025 Khichdi InfoTech (https://khichdiinfotech.com)

{
    'name': 'Google Tag Manager',
    'category': 'Website',
'summary': 'Add Google Tag Manager to your Odoo website and send structured purchase data for use in GTM tags.',
'description': """
Connect your Odoo website to Google Tag Manager (GTM) and manage all your marketing and analytics tags from one place.
This add-on:
  - Injects the GTM container snippet on public website pages
  - Lets you configure the container ID directly from Website ▸ Configuration ▸ Settings
  - Sends purchase information from the shop confirmation page (order value, currency and items) so you can build conversions and audiences in GTM
It is designed to stay lightweight: no theme changes, no custom code in templates, just a clean integration with the standard Odoo website.
""",
    'version': '16.0.1.0.0',
    'website' : 'https://khichdiinfotech.com/',
    'support' : 'contact@khichdiinfotech.com',
    'author'  : 'Khichdi InfoTech',
    'license': 'LGPL-3',
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
