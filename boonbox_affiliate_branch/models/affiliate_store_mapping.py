# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StoreMapping(models.Model):
    _description = "Store Mapping"
    _name = 'store.mapping'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Store Name', required=True, index=True)
    active = fields.Boolean(default=True, help="The active field allows you to hide the branch without removing it.")
    store_type = fields.Many2one('store.type', 'Store Type', required=True)
    # storefront_store_id = fields.Char('Storefront Store ID', required=True)
    store_priority = fields.Selection([('0', 'Normal'), ('1', 'High')], ' Store Priority', default='0')
    # mode_of_order = fields.Many2one('Mode of Order', required=True)
    payment = fields.Many2one('account.payment.term', 'Payment', required=True)
    # delivery_type = fields.Many2one('Delivery Type', required=True)
    is_partial_payment = fields.Boolean('Partial Payment Allowed')
    invoicing_restriction = fields.Boolean('Invoicing Restriction')
    # covered_pincode = fields.Many2many('Covered PIN Codes')
    # tat_details = fields.Many2one('TAT Details')
