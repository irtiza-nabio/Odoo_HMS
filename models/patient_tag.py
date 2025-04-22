from odoo import fields, models


class HospitalTag(models.Model):
    _name = 'patient.tag'
    _description = 'Patient Tag'

    name = fields.Char(string="Catagory", required=True)
    sequence = fields.Integer(default=10)
