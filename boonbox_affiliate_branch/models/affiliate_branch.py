# -*- coding: utf-8 -*-

from odoo import models, fields, api
from email.utils import formataddr


class AffiliateBranch(models.Model):
    _description = 'Branch'
    _name = 'affiliate.branch'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Branch Name', required=True, index=True)
    active = fields.Boolean(default=True, help="The active field allows you to hide the branch without removing it.")
    branch_code = fields.Char('Branch Code', required=True)
    street = fields.Char(required=True)
    street2 = fields.Char()
    city = fields.Char()
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict', required=True)
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict', required=True)
    zip = fields.Char(change_default=True, required=True)
    phone = fields.Char(required=True)
    email = fields.Char()
    email_formatted = fields.Char(
        'Formatted Email', compute='_compute_email_formatted',
        help='Format email address "Name <email@domain>"')
    regional_sales_officer = fields.Many2one('res.partner', required=True)
    store = fields.Many2one('store.mapping', required=True)
    branch_manager = fields.Many2one('res.partner', required=True)
    # affiliate_id = fields.Many2one(required=True)

    @api.depends('name', 'email')
    def _compute_email_formatted(self):
        for partner in self:
            partner.email_formatted = formataddr((partner.name or u"False", partner.email or u"False"))
