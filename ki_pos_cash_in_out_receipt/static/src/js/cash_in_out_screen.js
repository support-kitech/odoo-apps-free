/** @odoo-module **/

import { useErrorHandlers, useTrackedAsync, useAsyncLockedMethod } from "@point_of_sale/app/hooks/hooks";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { usePos } from "@point_of_sale/app/hooks/pos_hook";
import { Component, onMounted, onWillUnmount } from "@odoo/owl";
import { CashInOutReceiptWidget } from "./cash_in_out_receipt";
import { CashInOutSuccess } from "./cash_in_out_success";

export class CashMoveReceiptScreen extends Component {
    static template = "ki_pos_cash_in_out_receipt.CashMoveReceiptScreen";
    static components = {
        CashInOutReceiptWidget,
    };

    setup() {
        super.setup();
        this.pos = usePos();
        useErrorHandlers();
        this.ui = useService("ui");
        this.dialog = useService("dialog");
        this.printer = useService("printer");
        this.receiptData = this.pos.cashMoveReceiptData || {};
        this.receiptOrder = this._createReceiptOrder();
        this.clickPrintBill = useAsyncLockedMethod(this.clickPrintBill);
        this.backScreen = useTrackedAsync(() => this.getBackScreen());
        onMounted(() => {
            this.dialog.add(CashInOutSuccess, {});
        });
        onWillUnmount(() => {
            this._deleteReceiptOrder();
            delete this.pos.cashMoveReceiptData;
        });
    }

    _createReceiptOrder() {
        return this.pos.models["pos.order"].create({
            session_id: this.pos.session,
            company_id: this.pos.company,
            config_id: this.pos.config,
            user_id: this.pos.user,
            ticket_code: "",
            tracking_number: "",
            sequence_number: 0,
            pos_reference: "",
        });
    }

    _deleteReceiptOrder() {
        if (this.receiptOrder) {
            this.pos.models["pos.order"].delete(this.receiptOrder);
            this.receiptOrder = null;
        }
    }

    cashExportForPrinting() {
        return {
            translatedType: this.receiptData.translatedType,
            reason: this.receiptData.reason,
            formattedAmountSymbol: this.receiptData.formattedAmountSymbol,
            order: this.receiptOrder,
            date: new Date().toLocaleString(),
        };
    }

    async clickPrintBill() {
        await this.printer.print(
            CashInOutReceiptWidget,
            { data: this.cashExportForPrinting() },
            { webPrintFallback: true }
        );
        return true;
    }

    getBackScreen() {
        this.pos.navigate("ProductScreen", { orderUuid: this.pos.getOrder()?.uuid });
    }
}

registry.category("pos_pages").add("KiCashMoveReceiptScreen", {
    name: "KiCashMoveReceiptScreen",
    component: CashMoveReceiptScreen,
    route: `/pos/ui/${odoo.pos_config_id}/cash-move-receipt`,
    params: {},
});
