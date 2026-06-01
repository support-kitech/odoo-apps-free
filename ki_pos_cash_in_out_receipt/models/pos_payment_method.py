# Copyright © 2026 Khichdi InfoTech (https://khichdiinfotech.com)

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class PosPaymentMethod(models.Model):
    _inherit = "pos.payment.method"

    cash_in_out = fields.Boolean(string="Use For POS Cash In/Out")

    @api.constrains("cash_in_out", "config_ids", "is_cash_count")
    def _check_single_cash_in_out_per_pos(self):
        for method in self.filtered("cash_in_out"):
            if not method.is_cash_count:
                raise ValidationError(
                    _("Only cash payment methods can be used for POS Cash In/Out.")
                )
            if not method.config_ids:
                raise ValidationError(
                    _(
                        "Assign the payment method '%(method)s' to at least one Point of Sale "
                        "before enabling Cash In/Out.",
                        method=method.display_name,
                    )
                )
            for config in method.config_ids:
                other_methods = config.payment_method_ids.filtered(
                    lambda pm: pm.is_cash_count and pm.cash_in_out and pm != method
                )
                if other_methods:
                    raise ValidationError(
                        _(
                            "POS '%(pos)s' already has cash in/out enabled on '%(other)s'. "
                            "Only one cash payment method per shop can be enabled for cash in/out.",
                            pos=config.name,
                            other=other_methods[0].display_name,
                        )
                    )
