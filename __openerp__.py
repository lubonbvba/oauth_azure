# -*- coding: utf-8 -*-
{
    'name': "oauth_azure",

    'summary': """
        Implement azure oauth""",

    'description': """
	This module overrides the auth_oauth_rpc method so that it works for microsoft oauth
	Nothing else is changed to the oauth mechanism
    """,

    'author': "Lubon bvba",
    'website': "http://www.lubon.be",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','auth_oauth'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
