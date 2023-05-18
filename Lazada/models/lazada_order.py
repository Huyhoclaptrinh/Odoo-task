from odoo import fields, models, api

class SaleOrder(models.Model):
    _inherit = ['sale.order']
    _description = "Lazada Sales Order"

    loan_order = fields.Boolean(
        string="Loan Order",
        compute="_compute_loan_order",
        store=True, readonly=False, precompute=True,
    )

    @api.depends('company_id')
    def _compute_loan_order(self):
        for order in self:
            order.loan_order = order.company_id.portal_confirmation_pay
