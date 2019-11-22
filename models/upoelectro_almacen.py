from odoo import models, fields, api

class upoelectro_almacen(models.Model):
    _name = 'upoelectro.upoelectro_almacen'

    identificador = fields.Integer('ID', required=True)
    localizacion = fields.Char('Localizacion', size=60, required=True)
    foto = fields.Binary('Nuestras instalaciones')
    empleados_ids = fields.Many2many('upoelectro.upoelectro_empleado', string='Empleados')