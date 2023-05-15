from odoo import fields, models

class MemberModel(models.Model):
    _name = "member.list"
    _description = "list of member/trip"

    member_name = fields.Char()
    member_phone_num = fields.Integer()
    member_point = fields.Float()
    availability_date = fields.Date(string="Availability Date", copy=False, default=lambda self: fields.Datetime.today())
    selling_price = fields.Float(string="Selling Price", copy=False, readonly=True)
    bedroom = fields.Integer(default=2)
    active = fields.Boolean(string='Active', default=True)

    STATE_SELECTION = [
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled'),
    ]

    state = fields.Selection(STATE_SELECTION, string='State', default='new', required=True, copy=False)
