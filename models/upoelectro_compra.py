from odoo import models, fields, api

class upoelectro_compra(models.Model):
    _name = 'upoelectro.upoelectro_compra'

    fecha = fields.Datetime('Fecha', required=True, autodate = True)
    importe = fields.Float('Importe', digit=10, required=True)
    direccion = fields.Text('Dirección de facturación', size=60)
    proveedor_id = fields.Many2one('upoelectro.upoelectro_proveedor', 'Proveedor')
    empleado_id = fields.Many2one('upoelectro.upoelectro_empleado', 'Empleado')