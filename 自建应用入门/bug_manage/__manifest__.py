# -*- coding: utf-8 -*-
{
    'name': "bug管理",

    'summary': """
        用于软件开发过程中bug管理(summary)""",

    'description': """
        用于软件开发过程中bug管理(description)
    """,

    'author': "Rowry Cho",
    'website': "https://www.cnblogs.com/Rowry/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/bugs.xml',
        'views/follower.xml',
        'views/bugs_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
