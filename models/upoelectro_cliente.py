from odoo import models, fields, api

class upoelectro_cliente(models.Model):
    _name = 'upoelectro.upoelectro_cliente'

    nif = fields.Char('DNI/NIF', size=9, required=True)
    name = fields.Char('Nombre completo', size=60, required=True)
    telefono = fields.Char('Teléfono', size=9)
    correo = fields.Char('Correo', size=20)
    direccion = fields.Char('Dirección', size=20)
    foto = fields.Binary('Foto de perfil')