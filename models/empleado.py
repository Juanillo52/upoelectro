from odoo import models, fields, api

class empleado(models.Model):
    _name = 'upoelectro.empleado'

    name = fields.Char('Nombre completo', size=60, required=True)
    usuario = fields.Char('Nombre de usuario', size=60, required=True)
    telefono = fields.Char('Teléfono', size=9)
    correo = fields.Char('Correo', size=40)
    direccion = fields.Char('Dirección', size=60)
    foto = fields.Binary('Foto de perfil')
    ventas_ids = fields.One2many('upoelectro.venta','empleado_id', 'Ventas')
    compras_ids = fields.One2many('upoelectro.compra','empleado_id', 'Compras')
    almacenes_ids = fields.Many2many('upoelectro.almacen', string='Almacenes')