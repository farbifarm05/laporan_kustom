# -*- coding: utf-8 -*-
{
    'name': "Laporan Kustom Invoice", 
    'summary': "Menambahkan laporan invoice untuk printer dot matrix.",
    'description': "Modul ini berisi paper format, template, dan action untuk mencetak invoice ke printer dot matrix.",
    'author': "Fakhrul Rosyid",
    'website': "https://www.websiteanda.com",
    'category': 'Accounting/Reporting',
    'version': '1.0',

    
    'depends': ['base', 'account'],

    
    'data': [
        'reports/report_invoice_dot_matrix.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}