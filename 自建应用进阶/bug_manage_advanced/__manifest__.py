# -*- coding: utf-8 -*-
{
    'name': "bug管理升级版",

    'summary': """
        管理项目测试过程中发现的bug""",

    'description': """
        管理项目测试过程中发现的bug
    """,

    'author': "Rowry Cho",
    'website': "https://www.cnblogs.com/Rowry/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/bug_advanced.xml',
        'views/bug_stage.xml',
        'views/bug_tag.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}