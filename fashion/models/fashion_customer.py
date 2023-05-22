from odoo import fields, models, api, _

class CustomerModel(models.Model):
    _name = "fashion.customer"
    _description = "List of customers"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    customer_name = fields.Char(string="Customer Name", required=True)
    GENDER_SELECTION = [('male', 'Male'),
                        ('female', 'Female'),
                        ]
    customer_gender = fields.Selection(GENDER_SELECTION,  string="Customer Gender", required=True, copy=False)
    customer_dob = fields.Datetime(string="Customer Date Of Birth", required=True)
    customer_point = fields.Integer(string="Customer Point", required=True, related="products_ids.product_sale_deal")
    products_ids = fields.One2many('fashion.product', 'customer_id', string="Products", required=True)
    ref = fields.Char(string="Reference", default=lambda self: _('New'))

    @api.model_create_multi
    def create(self, vals_list):
        # for vals in vals_list:
        #     vals['ref'] = self.env['ir.sequence'].next_by_code('fashion.customer')
        return super(CustomerModel, self).create(vals_list)



