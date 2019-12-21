from odoo import models, fields, api

class almacen(models.Model):
    _name = 'upoelectro.almacen'

    identificador = fields.Integer('ID', required=True)
    localizacion = fields.Char('Localizacion', size=120, required=True)
    foto = fields.Binary('Nuestras instalaciones')
    empleados_ids = fields.Many2many('upoelectro.empleado', string='Empleados')
    categorias_ids = fields.One2many('upoelectro.categoria', 'almacen_id', 'Categorías')