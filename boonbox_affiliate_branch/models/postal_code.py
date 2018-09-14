# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PostalCode(models.Model):
    _description = 'Postal Code'
    _name = 'postal.code'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('PIN Code', required=True, index=True)
    active = fields.Boolean(default=True, help="The active field allows you to hide the branch without removing it.")
    area = fields.Char('Area', required=True)
    city = fields.Char('City', required=True)
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict')
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict')
