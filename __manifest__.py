# -*- coding: utf-8 -*-
{
    'name': "l10n_ch_clubmanagement",

    'summary': "Swiss Localization for Club Management",

    'description': """
Swiss localization addon for Odoo Club Management system.

Extends the club member module with Switzerland-specific features:
- J+S Number (Jugend+Sport) field for members
- Automatic SSN ID validation (compliance with Swiss youth sports regulations)
- Age-based member classification for Swiss sport associations

Requires the clubmanagement addon.
For more information, visit: https://github.com/michi-blicki/Odoo_Clubmanagement
    """,

    #
    # Issuer Specification
    'author': "Michael Blickenstorfer",
    'website': "https://github.com/michi-blicki/l10n_ch_clubmanagement",
    'license': "AGPL-3",
    #'price': 10.00,
    #'currency': "CHF",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Association',
    'version': '18.0.1.1.0',
    'application': False,
    'auto_install': False,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': [
        'clubmanagement',
        'l10n_ch_oasi_verification',
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

