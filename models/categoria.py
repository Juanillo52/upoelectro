from odoo import models, fields, api

class categoria(models.Model):
    _name = 'upoelectro.categoria'

    name = fields.Char('Nombre', size=60, required=True)
    descripcion = fields.Char('Descripción', size=100)
    imagen = fields.Binary('Imagen de la categoría')
    almacen_id = fields.Many2many('upoelectro.almacen', string='Almacenes')
    articulos_ids = fields.One2many('upoelectro.articulo','categoria_nombre', 'Articulos') 
    nArticulos = fields.Integer(compute='_articulos_count',string='Nº Artículos',store=True)
    
    @api.depends('articulos_ids')
    def _articulos_count(self):
        x = self.env['upoelectro.categoria']
        
        for categoria in self:
            cont = 0
        
            for rec in categoria.articulos_ids:
            
                cont+=1
            
            categoria.nArticulos= cont