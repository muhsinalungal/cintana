# -*- coding: utf-8 -*-
{
    'name': "Affiliate Branch",

    'summary': """
        Used to create Affiliate Branches""",

    'author': "Cintana Technologies Pvt.Ltd",
    'website': "http://www.cintanatech.com/",
    'category': 'Crm',
    'version': '0.1',
    'sequence': 6,

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm_affiliate'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/affiliate_branch_view.xml',
        'views/store_mapping_view.xml',
        'views/store_type_view.xml',
        'views/postal_code_view.xml',
        'views/country_view.xml',
        'views/country_state_view.xml',
    ],

}
