from odoo import models, fields, api

class proveedor(models.Model):
    _name = 'upoelectro.proveedor'

    identificador = fields.Integer('ID', required=True)
    name = fields.Char('Nombre completo', size=60, required=True)
    telefono = fields.Char('Teléfono', size=9)
    correo = fields.Char('Correo', size=20)
    direccion = fields.Char('Dirección', size=20)
    foto = fields.Binary('Foto de perfil')
    compras_ids = fields.One2many('upoelectro.compra','proveedor_id', 'Compras')