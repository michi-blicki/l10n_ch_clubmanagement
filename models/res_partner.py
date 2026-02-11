# -*- coding: utf-8 -*-
"""
Model extensions for OASI validation

This module extends hr.employee and res.partner models to include OASI validation
on their ssnid fields.
"""

from odoo import api, fields, models


class ResPartner(models.Model):
    """Extend res.partner to validate OASI in ssnid field"""

    _inherit = ["res.partner", 'oasi.validation.mixin']
    _inherit_oasi = True  # Flag to show this model includes OASI validation

    @api.constrains("ssnid")
    def _validate_employee_ssnid(self):
        """Validate OASI check digit if ssnid is set and looks like Swiss ID"""

        for record in self:
            ssnid = record.ssnid
            country = record.country_id
            if ssnid and country and country.id == self.env.ref("base.ch").id:
                # Only validate if it looks like a Swiss ID (starts with 756)
                self._validate_oasi_field('ssnid', field_label="SSNID")

    @api.onchange("ssnid")
    def _onchange_employee_ssnid(self):
        """Validate OASI on field change (real-time feedback to user)"""

        ssnid = self.ssnid
        country = self.country_id
        if ssnid and country and country.id == self.env.ref("base.ch").id:
            # Only validate if it looks like a Swiss ID (starts with 756)
            self._onchange_validate_oasi_field("ssnid", field_label="SSNID")
