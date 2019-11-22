from odoo import models, fields, api

class upoelectro_cliente(models.Model):
    _name = 'upoelectro.upoelectro_venta'

    fecha = fields.Datetime('Fecha', required=True, autodate = True)
    importe = fields.Float('Importe', digit=10, required=True)
    direccion = fields.Text('Dirección de facturación', size=60)
    cliente = fields.One2many(' upoelectro.upoelectro_cliente','upoelectro_cliente_nombre', 'Cliente')