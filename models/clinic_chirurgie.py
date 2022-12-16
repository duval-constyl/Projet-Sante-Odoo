# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class ClinicChirurgie(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _name = 'clinic.chirurgie'
    _description = 'info.chirurgie'