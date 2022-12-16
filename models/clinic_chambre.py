# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class ClinicChambre(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _name = 'clinic.chambre'
    _description = 'info.chambre'