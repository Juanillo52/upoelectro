from odoo import models, fields, api

class lineaventa(models.Model):
    _name = 'upoelectro.lineaventa'

    cantidad = fields.Integer('Cantidad', required=True)
    precio = fields.Float('Precio', required=True)
    articulo_id = fields.Many2one('upoelectro.articulo', 'Articulo')
    venta_id = fields.Many2one('upoelectro.venta', 'Venta')
    
    
    @api.onchange('cantidad')
    def _check_capacity(self):
            self.precio = self.cantidad * self.articulo_id.precio