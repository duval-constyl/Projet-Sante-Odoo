# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class ClinicPersonnel(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _name = 'clinic.personnel'
    _description = 'info.personnel'