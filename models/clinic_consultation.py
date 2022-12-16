# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class ClinicConsultation(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _name = 'clinic.consultation'
    _description = 'info.consultation'