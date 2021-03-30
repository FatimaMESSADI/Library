# -*- coding: utf-8 -*-
{
    'name': "Library_members",

    

    'description': 'Manage people who will be able to borrow books.',

    'author': "Tima",
    #'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['bibliotheque','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/book_view.xml',
        'views/member_view.xml',
        #'views/templates.xml',
        'views/library_menu.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application': False,
}