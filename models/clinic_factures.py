# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class ClinicFactures(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _name = 'clinic.factures'
    _description = 'info.factures'