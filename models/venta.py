from odoo import models, fields, api

class venta(models.Model):
    _name = 'upoelectro.venta'

    fecha = fields.Datetime('Fecha', required=True, autodate = True)
    importe = fields.Float('Importe', digit=10, required=True)
    direccion = fields.Char('Dirección', size=60)
    codigo_postal = fields.Char('Código postal', size=5)
    ciudad = fields.Char('Ciudad', size=60)
    provincia = fields.Char('Provincia', size=60)
    cliente_id = fields.Many2one('upoelectro.cliente', 'Cliente')
    empleado_id = fields.Many2one('upoelectro.empleado', 'Empleado')