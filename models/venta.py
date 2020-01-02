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
    lineaventa_ids = fields.One2many('upoelectro.lineaventa', 'venta_id', 'Pedido')
    state = fields.Selection([('solicitante','Solicitante'),
                              ('enproceso','En Proceso'),
                              ('cancelado','Cancelado'),
                              ('enviado','Enviado'),],
                              'Estado',
                              default='solicitante')
    @api.one
    def btn_submit_to_enproceso(self):
        self.write({'state':'enproceso'})
        
    @api.one
    def btn_submit_to_cancelado(self):
        self.write({'state':'cancelado'})
        
    @api.one
    def btn_submit_to_enviado(self):
        self.write({'state':'enviado'})
        
    @api.onchange('lineaventa_ids')
    def onchange_lineaventa(self):
        if self.state == 'enviado':
            
            for lineaventa in self.lineaventa_ids:
                lineaventa.articulo_id.stock = lineaventa.articulo_id.stock - lineaventa.cantidad
    
    @api.onchange('lineaventa_ids')
    def onchange_venta(self):
        self.importe = 0
        
        for lineaventa in self.lineaventa_ids:
            self.importe = self.importe + lineaventa.precio
    
    