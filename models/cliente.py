from odoo import models, fields, api

class cliente(models.Model):
    _name = 'upoelectro.cliente'


    nif = fields.Char('DNI/NIF', size=9, required=True)
    name = fields.Char('Nombre completo', size=60, required=True)
    telefono = fields.Char('Teléfono', size=9)
    correo = fields.Char('Correo', size=40)
    direccion = fields.Char('Dirección', size=60)
    codigo_postal = fields.Char('Código postal', size=5)
    ciudad = fields.Char('Ciudad', size=60)
    provincia = fields.Char('Provincia', size=60)
    foto = fields.Binary('Foto de perfil')
    ventas_ids = fields.One2many('upoelectro.venta','cliente_id', 'Ventas')
    
    nVentas = fields.Integer(compute='_ventas_count',string='Nº Ventas',store=True)
    
    @api.depends('ventas_ids')
    def _ventas_count(self):

        x = self.env['upoelectro.cliente']
        
        for cliente in self:
            cont = 0
        
            for rec in cliente.ventas_ids:
            
                cont+=1
            
            cliente.nVentas= cont