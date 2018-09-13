# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools.safe_eval import safe_eval


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    crm_lead_type = fields.Selection(
        [('sale_lead', 'Sales Lead'), ('affiliate_lead', 'Affiliate Lead')],
        string='CRM Lead Type', required=True,
        readonly=True, copy=False, default='sale_lead'
    )


class CrmTeam(models.Model):
    _inherit = 'crm.team'

    team_type = fields.Selection(
        [('sales_team', 'Sales Team'), ('affiliates_team', 'Affiliates Team')],
        string='Team Type', required=True,
        readonly=True, copy=False, default='sales_team'
    )

    @api.model
    def action_your_affiliate_pipeline(self):
        action = self.env.ref('crm.crm_lead_opportunities_tree_view').read()[0]
        user_team_id = self.env.user.sale_team_id.id
        if not user_team_id:
            user_team_id = self.search([], limit=1).id
            action['help'] = """<p class='oe_view_nocontent_create'>
            Click here to add new opportunities</p>
            <p>Looks like you are not a member of a sales channel.
            You should add yourself as a member of one of the sales channel.
            </p>"""
            if user_team_id:
                action['help'] += """<p>As you don't belong to any sales channel,
                Odoo opens the first one by default.</p>"""

        action_context = safe_eval(action['context'], {'uid': self.env.uid})
        if user_team_id:
            action_context['default_team_id'] = user_team_id

        tree_view_id = self.env.ref('crm.crm_case_tree_view_oppor').id
        form_view_id = self.env.ref('crm.crm_case_form_view_oppor').id
        kanb_view_id = self.env.ref('crm.crm_case_kanban_view_leads').id
        action['views'] = [
            [kanb_view_id, 'kanban'],
            [tree_view_id, 'tree'],
            [form_view_id, 'form'],
            [False, 'graph'],
            [False, 'calendar'],
            [False, 'pivot']
        ]
        action_context['default_crm_lead_type'] = 'affiliate_lead'
        action_context['search_default_assigned_to_me'] = 0
        action_context['search_default_affiliate_assigned_to_me'] = 1
        action['context'] = action_context
        return action


class CrmStage(models.Model):
    _inherit = 'crm.stage'

    stage_type = fields.Selection([
        ('sales_crm_stage', 'Sales CRM Stage'),
        ('affiliates_crm_stage', 'Affiliates CRM Stage')],
        string='Stage Type', required=True, readonly=True,
        copy=False, default='sales_crm_stage'
    )


class ResPartner(models.Model):
    _inherit = 'res.partner'

    affiliate = fields.Boolean(string='Is a Affiliate')
