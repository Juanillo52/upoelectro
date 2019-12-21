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
    provincia = fields.Char('Ciudad', size=60)
    foto = fields.Binary('Foto de perfil')
    ventas_ids = fields.One2many('upoelectro.venta','cliente_id', 'Ventas') 