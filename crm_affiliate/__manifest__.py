# -*- coding: utf-8 -*-
{
    'name': "Affiliate CRM",
    'version': '0.1',
    'sequence': 6,
    'category': 'CRM',
    'author': "Cintana Technologies Pvt. Ltd.",
    'website': "http://cintanatech.com",
    'depends': ['crm'],

    'summary': """
        CRM for affiliate leads
    """,
    'description': """
        CRM for onboarding the affiliate leads
    """,

    'data': [
        # 'security/ir.model.access.csv',
        'views/crm_affiliate_view.xml',
        'menus/crm_affiliate_menu.xml',
    ]
}
