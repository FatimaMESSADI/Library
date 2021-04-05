# -*- coding: utf-8 -*-
{
    'name': "Library Book Borrowing",

    
    'description': "Members can borrow books from the library.",

    'author': "Tima",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['library_member','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/checkout_view.xml',
        'views/library_menu.xml',
        'data/library_checkout_stage.xml',
        'wizard/checkout_mass_message_wizard_view.xml',
        #'wizard/wizard_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}