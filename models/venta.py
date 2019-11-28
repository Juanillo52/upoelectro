from odoo import models, fields, api

class venta(models.Model):
    _name = 'upoelectro.venta'

    fecha = fields.Datetime('Fecha', required=True, autodate = True)
    importe = fields.Float('Importe', digit=10, required=True)
    direccion = fields.Text('Dirección de facturación', size=60)
    cliente_id = fields.Many2one('upoelectro.cliente', 'Cliente')
    empleado_id = fields.Many2one('upoelectro.empleado', 'Empleado')