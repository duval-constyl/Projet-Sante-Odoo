# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class ClinicPatient(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _name = 'clinic.patient'
    _description = 'info.patient'