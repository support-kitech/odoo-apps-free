/** @odoo-module **/

import { Component } from "@odoo/owl";
import { ReceiptHeader } from "@point_of_sale/app/screens/receipt_screen/receipt/receipt_header/receipt_header";

export class CashInOutReceiptWidget extends Component {
    static template = "ki_pos_cash_in_out_receipt.CashInOutReceiptWidget";
    static components = { ReceiptHeader };
    static props = {
        data: Object,
    };
}
