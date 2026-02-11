from odoo import models, fields, api, _
from odoo.exceptions import AccessError, ValidationError, UserError
from dateutil.relativedelta import relativedelta

class ClubMember(models.Model):
    _name = 'club.member'
    _inherit = 'club.member'

    js_number = fields.Integer(string="J+S Number", required=False, readonly=False)

    @api.depends('birthdate_date')
    def _compute_require_ssnid(self):
        age_of_majority = int(self.env['ir.config_parameter'].sudo().get_param('clubmanagement.age_of_majority', 18))
        today = fields.Date.today()
        for member in self:
            country = member.partner_id.country_id
            if country and country.id == self.env.ref("base.ch").id:
                # we only require SSN ID for Swiss members, and only if they are minors
                # as birthdate and SSN ID are required for J+S registration
                if not member.birthdate_date:
                    raise UserError(_("Member must have a birthdate registered."))
                
                age = relativedelta(today, member.birthdate_date).years
                if age < age_of_majority:
                    if not member.partner_id.ssnid:
                        raise UserError(_("Member is below age of majority. SSN ID required for J+S number."))