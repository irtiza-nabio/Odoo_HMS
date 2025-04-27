from odoo import http
from odoo.http import request


class HospitalWebsite(http.Controller):
    @http.route('/hospital/contacts', type='http', auth="public", website=True)
    def hospital_contacts(self):
        contacts = request.env['res.partner'].sudo().search([])
        return request.render('madaripur_hospital.contacts_page', {'contacts': contacts})
