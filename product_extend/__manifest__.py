# -*- coding: utf-8 -*-
{
    'name': "Product Extend (Ejemplo Herencia)",

    'summary': """
        Ejemplo de herencia en el modulo product
        Agrega un campo seleccionable Tipologia
        """,

    'author': "Mit-Mut",
    'website': "http://www.Mit-Mut.com",

    'category': "Product",
    'version': "0.1",

    # any module necessary for this one to work correctly
    'depends': ['product'],

    # always loaded
    'data': [
        'views/product_view.xml',
    ],
    'Installable': True,
    'application': True,
}
