from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread']
    _description = 'Patient Master'

    name = fields.Char(string="Name", required=True, tracking=True,
                       help="Name of the patient")
    date_of_birth = fields.Date(
        string="DOB", tracking=True, help="Date of birth of the patient")
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')],
        string="Gender",
        help="Gender of the patient"
    )

    tag_ids = fields.Many2many(
        'patient.tag', 'patient_tag_rel', 'patient_id', 'tag_id', string="Tags")

    is_minor = fields.Boolean(string="Minor")
    guardian = fields.Char(string="Guardian")
    weight = fields.Float(string="Weight")


@api.ondelete(at_uninstall=False)
def _check_patient_appointments(self):
    for rec in self:
        appointments = self.env['hospital.appointment'].search([
            ('patient_id', '=', rec.id)
        ])
        if appointments:
            raise UserError(_(
                "You cannot delete the patient '%s' because there are existing appointments."
            ) % rec.name)


# Rabbi Bhai Sheraaaaaa
#
#
# aded cpmment
