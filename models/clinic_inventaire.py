# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class ClinicInventaire(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _name = 'clinic.inventaire'
    _description = 'info.inventaire'