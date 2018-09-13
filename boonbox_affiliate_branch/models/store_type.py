# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StoreType(models.Model):
    _description = 'Store Type'
    _name = 'store.type'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Store Type', required=True, index=True)
    store_code = fields.Char('Store Code', required=True)
    active = fields.Boolean(default=True, help="The active field allows you to hide the branch without removing it.")
