# -*- coding: utf-8 -*-

from odoo import api,models, fields, exceptions

class LibraryBooks(models.Model):
    _name = "library.books"
    _description = "Libreria de odoo"

    name = fields.Char(string='Book', default='New')
    description = fields.Text(string='Description')

    isbn = fields.Char('ISBN')

    #LOS LIBROS SOLO MUEDEN TENER UNA CATEGORIA
    #category_id = fields.Many2one(comodel_name='library.category',
    #                              string='Categoria')

    #LOS LIBROS PUEDEN TENER MUCHAS CATEGORIAS
    category_id = fields.Many2many(comodel_name='library.category', string='Categoria')

    #RESTRICCIONES POR MEDIO DE POSTGRES
    _sql_constraints = [
        ('name_uniq', 'unique (name)', """ El libro ya existe!!! """)
    ]

    #ESTRICCIONES POR MEDIO DE PYTHON
    @api.constrains("isbn") #campo que se restringe o controla
    def check_isbn(self):
        isbn = self.search([['id', '!=', self.id]]).mapped('isbn')
        if self.isbn and self.isbn in isbn:
            raise exceptions.ValidationError("ISBN duplicado")
