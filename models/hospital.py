from odoo import models


class HospitalHospital(models.Model):
    _name = 'hospital.hospital'  # your model name

    def action_open_contacts_website(self):
        return {
            'type': 'ir.actions.act_url',
            'url': '/hospital/contacts',  # your website URL
            'target': 'new',  # open in a new tab
        }
