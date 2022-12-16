# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class ClinicCompte(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _name = 'clinic.compte'
    _description = 'info.compte'