from odoo import fields, models, api


class ProductModel(models.Model):
    _name = "fashion.product"
    _description = "List of products"

    product_name = fields.Char(string="Product Name", required=True)
    PRODUCT_SELECTION = [('shorts', 'Shorts'),
                        ('jackets', 'Jackets'),
                        ('shoes','Shoes')
                        ]
    product_types = fields.Selection(PRODUCT_SELECTION,  string="Product Types", required=True, copy=False)
    product_price = fields.Monetary(string="Product Price",currency_field="customer_id", required=True)
    product_sale_deal = fields.Integer(string="Product Sale Deal", required=True, compute="_onchange_sale", store=True)
    product_number = fields.Integer(string="Number Of Products", required=True)
    product_release_date = fields.Date(string="Release Date", copy=False, default=lambda self: fields.Datetime.now())
    customer_id = fields.Many2one('fashion.customer',string="Customer", required=True)

    @api.depends('product_number')
    def _onchange_sale(self):
        deals_list = [x for x in range(0,101,10)]  # List of product numbers with associated deals
        for record in self:
            if record.product_number in deals_list:
                record.product_sale_deal = 1  # Set the deal value as needed





