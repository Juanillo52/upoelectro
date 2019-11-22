from odoo import models, fields, api

class upoelectro_empleado(models.Model):
    _name = 'upoelectro.upoelectro_empleado'

    name = fields.Char('Nombre completo', size=60, required=True)
    usuario = fields.Char('Nombre de usuario', size=60, required=True)
    telefono = fields.Char('Teléfono', size=9)
    correo = fields.Char('Correo', size=20)
    direccion = fields.Char('Dirección', size=20)
    foto = fields.Binary('Foto de perfil')
    ventas_ids = fields.One2many('upoelectro.upoelectro_venta','empleado_id', 'Ventas')
    compras_ids = fields.One2many('upoelectro.upoelectro_compra','empleado_id', 'Compras')
    almacenes_ids = fields.Many2many('upoelectro.upoelectro_almacen', string='Almacenes')