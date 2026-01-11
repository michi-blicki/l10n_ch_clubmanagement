# -*- coding: utf-8 -*-
{
    'name': "l10n_ch_clubmanagement",

    'summary': "Clubmanagement: Switzerland",

    'description': """
This is a small Addon, that enhances the clubmanagement suite, available at https://github.com/michi-blicki/Odoo_Clubmanagement.git.
    """,

    #
    # Issuer Specification
    'author': "Michael Blickenstorfer",
    'website': "https://www.blicki.ch",
    'license': "AGPL-3",
    #'price': 30.00,
    #'currency': "CHF",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Association',
    'version': '18.0.0.4.0',
    'application': False,
    'auto_install': False,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': [
        'clubmanagement'
    ],

    # always loaded
    'data': [

    ],

    'assets': {

    },

    'translation_files': [

    ],

    # only loaded in demonstration mode
    'demo': [
        
    ],

    #
    # Hooks
    'pre_init_hook': '_pre_init_hook',
    'post_init_hook': '_post_init_hook',
    'uninstall_hook': '_uninstall_hook',

}

