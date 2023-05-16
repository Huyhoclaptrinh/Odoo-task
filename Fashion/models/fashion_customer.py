from odoo import fields, models, api

class CustomerModel(models.Model):
    _name = "fashion.customer"
    _description = "List of customers"

    customer_name = fields.Char(string="Customer Name", required=True)
    GENDER_SELECTION = [('male', 'Male'),
                        ('female', 'Female'),
                        ]
    customer_gender = fields.Selection(GENDER_SELECTION,  string="Customer Gender", required=True, copy=False)
    customer_dob = fields.Datetime(string="Customer Date Of Birth", required=True)
    customer_point = fields.Integer(string="Customer Point", required=True, related="products_id.product_sale_deal")
    products_id = fields.One2many('fashion.product','customer_id',string="Products", required=True)



