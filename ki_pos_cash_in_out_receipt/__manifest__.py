# Copyright © 2026 Khichdi InfoTech (https://khichdiinfotech.com)
{
    "name": "POS Cash In/Out Multi Currency & Receipt",
    "summary": "POS multi-currency cash in/out with receipt printing for Odoo 18 Enterprise.",
    "version": "18.0.1.0.0",
    "category": "Sales/Point of Sale",
    "description": """
POS Cash In/Out Multi Currency & Receipt
========================================

This free module adds focused Point of Sale enhancements for Odoo 18 Enterprise:

* Configure allowed currencies for cash in/out per POS.
* Perform cash in/out using selected currency in POS.
* Automatically convert entered amount to company currency.
* Dedicated receipt screen with print support.
* Foreign currency tracking in cash register and journal entries.
    """,
    "author": "Khichdi InfoTech",
    "email": "contact@khichdiinfotech.com",
    "website": "https://www.khichdiinfotech.com/",
    "maintainer": "Khichdi InfoTech",
    "license": "LGPL-3",
    "depends": ["point_of_sale"],
    "data": [
        "views/pos_config_views.xml",
    ],
    "assets": {
        "point_of_sale._assets_pos": [
            "ki_pos_cash_in_out_receipt/static/src/js/cash_in_out_receipt.js",
            "ki_pos_cash_in_out_receipt/static/src/js/cash_in_out_success.js",
            "ki_pos_cash_in_out_receipt/static/src/js/cash_in_out_screen.js",
            "ki_pos_cash_in_out_receipt/static/src/js/cash_in_out_popup.js",
            "ki_pos_cash_in_out_receipt/static/src/xml/cash_in_out_receipt.xml",
            "ki_pos_cash_in_out_receipt/static/src/xml/cash_in_out_receipt_screen.xml",
            "ki_pos_cash_in_out_receipt/static/src/xml/cash_in_out_popup.xml",
        ],
    },
    'images': ['static/description/banner.png', 'static/description/icon.png'],
    "installable": True,
    "application": False,
    "auto_install": False,
}
