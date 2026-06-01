/** @odoo-module **/

import { Component } from "@odoo/owl";
import { Dialog } from "@web/core/dialog/dialog";

export class CashInOutSuccess extends Component {
    static template = "ki_pos_cash_in_out_receipt.CashInOutSuccess";
    static components = { Dialog };
    static props = ["close"];

    close() {
        this.props.close();
    }
}
