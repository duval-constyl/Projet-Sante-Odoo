# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class ClinicPharmacie(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _name = 'clinic.pharmacie'
    _description = 'info.pharmacie'