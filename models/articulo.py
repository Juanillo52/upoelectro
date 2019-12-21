from odoo import models, fields, api

class articulo(models.Model):
    _name = 'upoelectro.articulo'

    name = fields.Char('Nombre completo', size=60, required=True)
    identificador = fields.Integer('ID', required=True)
    descripcion = fields.Text('Descripcion', size=200)
    marca = fields.Char('Marca', size=20, requiered=True)
    imagen = fields.Binary('Imagen')
    caracteristicas = fields.Text('Caracteristicas', size=100, required=True)
    precio = fields.Float('Precio', required=True)
    stock = fields.Integer('Stock', required=True)
    categoria_nombre = fields.Many2one('upoelectro.categoria', 'Categoria')
    
    @api.onchange('gymclass_ids')
    def onchange_gymclass(self):
        if self.state != 'admitido':
            