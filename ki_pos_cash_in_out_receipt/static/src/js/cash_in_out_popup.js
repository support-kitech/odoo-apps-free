/** @odoo-module **/

import { CashMovePopup } from "@point_of_sale/app/components/popups/cash_move_popup/cash_move_popup";
import { patch } from "@web/core/utils/patch";
import { _t } from "@web/core/l10n/translation";
import { parseFloat } from "@web/views/fields/parsers";
import { useState } from "@odoo/owl";

patch(CashMovePopup.prototype, {
    setup() {
        super.setup();
        this.cash_currency_ids = this._getCashCurrencies();
        this.cashCurrencyState = useState({
            currency_id: this.pos.currency?.id || false,
        });
    },

    _getCashCurrencies() {
        const configuredCurrencyIds = this.pos.config.cash_currency_ids || [];
        const currencyModel = this.pos.models["res.currency"];
        const currencies = [];
        const seenCurrencyIds = new Set();

        const addCurrency = (currency) => {
            if (currency && !seenCurrencyIds.has(currency.id)) {
                seenCurrencyIds.add(currency.id);
                currencies.push(currency);
            }
        };

        addCurrency(this.pos.currency);

        if (!currencyModel) {
            return currencies;
        }

        for (const currencyRef of configuredCurrencyIds) {
            const currencyId = typeof currencyRef === "object" ? currencyRef.id : currencyRef;
            addCurrency(currencyModel.get(currencyId));
        }
        return currencies;
    },

    getSelectedCurrency() {
        const currencyId = Number(this.cashCurrencyState.currency_id);
        if (!currencyId) {
            return this.pos.currency;
        }
        const currency = this.pos.models["res.currency"]?.get(currencyId);
        return currency || this.pos.currency;
    },

    isValidCashMove() {
        return (
            this.env.utils.isValidFloat(this.state.amount) &&
            this.state.reason.trim() !== "" &&
            !!this.cashCurrencyState.currency_id
        );
    },

    _prepareTryCashInOutPayload(type, amount, reason, partnerId, extras) {
        return super._prepareTryCashInOutPayload(type, amount, reason, partnerId, {
            ...extras,
            currency_id: this.cashCurrencyState.currency_id,
        });
    },

    async confirm() {
        const amount = parseFloat(this.state.amount);
        const currencyId = this.cashCurrencyState.currency_id;
        const formattedAmount = this.env.utils.formatCurrency(amount);
        const formattedAmountSymbol = await this.pos.data.call(
            "pos.session",
            "format_currency_amount_cash",
            [[this.pos.session.id], amount, currencyId]
        );

        if (!amount) {
            this.notification.add(_t("Cash in/out of %s is ignored.", formattedAmount));
            return this.props.close();
        }

        const type = this.state.type;
        const translatedType = _t(type);
        const reason = this.state.reason.trim();
        const extras = {
            formattedAmount,
            formattedAmountSymbol,
            translatedType,
            currency_id: currencyId,
        };

        await this.pos.data.call(
            "pos.session",
            "try_cash_in_out",
            this._prepareTryCashInOutPayload(type, amount, reason, this.partnerId, extras),
            {},
            true
        );
        await this.pos.logEmployeeMessage(
            `${_t("Cash")} ${translatedType} - ${_t("Amount")}: ${formattedAmountSymbol}`,
            "CASH_DRAWER_ACTION"
        );

        this.pos.cashMoveReceiptData = {
            formattedAmountSymbol,
            reason,
            formattedAmount,
            translatedType,
            currency_id: String(currencyId),
        };

        this.props.close();
        this.notification.add(
            _t("Successfully made a cash %s of %s.", type, formattedAmountSymbol),
            3000
        );
        this.pos.navigate("KiCashMoveReceiptScreen");
    },
});
