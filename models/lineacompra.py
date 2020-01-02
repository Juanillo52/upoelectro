from odoo import models, fields, api

class lineacompra(models.Model):
    _name = 'upoelectro.lineacompra'

    cantidad = fields.Integer('Cantidad', required=True)
    precio = fields.Float('Precio', required=True)
    articulo_id = fields.Many2one('upoelectro.articulo', 'Articulo')
    compra_id = fields.Many2one('upoelectro.compra', 'Compra')
    
    
    @api.onchange('cantidad')
    def _check_capacity(self):
            self.precio = self.cantidad * self.articulo_id.precio
            
    @api.one
    @api.constrains('cantidad')
    def _check_cantidad(self):
        if self.cantidad >= 50:
            raise models.ValidationError('No se pueden realizar pedidos superiores a 50 unidades')