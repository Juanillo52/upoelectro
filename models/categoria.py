from odoo import models, fields, api

class categoria(models.Model):
    _name = 'upoelectro.categoria'

    name = fields.Char('Nombre', size=60, required=True)
    descripcion = fields.Char('Descripción', size=100)
    imagen = fields.Binary('Imagen de la categoría')
    almacen_id = fields.Many2one('upoelectro.almacen', 'Almacén')
    articulo_id = fields.One2many('upoelectro.articulo','categoria_nombre', 'Articulos') 