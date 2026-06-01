/** @odoo-module **/

import { useErrorHandlers, useTrackedAsync, useAsyncLockedMethod } from "@point_of_sale/app/utils/hooks";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { Component, useState, onMounted } from "@odoo/owl";
import { CashInOutReceiptWidget } from "./cash_in_out_receipt";
import { CashInOutSuccess } from "./cash_in_out_success";

export class CashMoveReceiptScreen extends Component {
    static template = "ki_pos_cash_in_out_receipt.CashMoveReceiptScreen";
    static components = {
        CashInOutReceiptWidget,
    };
    static props = {
        reason: String,
        translatedType: String,
        formattedAmount: String,
        formattedAmountSymbol: String,
        currency_id: { type: String, optional: true },
    };

    setup() {
        super.setup();
        this.pos = usePos();
        useErrorHandlers();
        this.ui = useState(useService("ui"));
        this.dialog = useService("dialog");
        this.clickPrintBill = useAsyncLockedMethod(this.clickPrintBill);
        this.backScreen = useTrackedAsync(() => this.getBackScreen());
        onMounted(() => {
            this.dialog.add(CashInOutSuccess, {});
        });
    }

    cashExportForPrinting() {
        return {
            translatedType: this.props.translatedType,
            reason: this.props.reason,
            formattedAmountSymbol: this.props.formattedAmountSymbol,
            headerData: this.pos.getReceiptHeaderData(),
            date: new Date().toLocaleString(),
        };
    }

    async clickPrintBill() {
        await this.pos.printer.print(
            CashInOutReceiptWidget,
            { data: this.cashExportForPrinting() },
            { webPrintFallback: true }
        );
        return true;
    }

    getBackScreen() {
        this.pos.showScreen("ProductScreen");
    }
}

registry.category("pos_screens").add("KiCashMoveReceiptScreen", CashMoveReceiptScreen);
