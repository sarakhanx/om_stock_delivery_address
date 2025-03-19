# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Stock Picking Delivery Address',
    'version': '17.0.1.0.0',
    'category': 'Inventory/Inventory',
    'summary': 'Add delivery address to stock picking list view',
    'description': """
        This module adds the delivery address field to the stock picking list view.
    """,
    'depends': ['stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/stock_picking_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'application': False,
    'sequence': 1,
} 