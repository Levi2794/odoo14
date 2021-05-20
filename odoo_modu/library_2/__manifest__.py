# -*- coding: utf-8 -*-
{
    'name': "library 2",

    'summary': """
        library 2
        """,

    'author': "Mit-Mut",
    'website': "http://www.Mit-Mut.com",

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/library_books_view.xml',
        'views/library_category_view.xml',
    ],
    'Installable': True,
    'application': True,
}
