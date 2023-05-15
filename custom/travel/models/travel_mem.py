from odoo import fields, models

class MemberModel(models.Model):
    _name = "member.list"
    _description = "list of member/trip"

    member_name = fields.Char()
    member_phone_num = fields.Integer()
    member_point = fields.Float()