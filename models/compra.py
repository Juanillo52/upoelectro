from odoo import models, fields, api

class compra(models.Model):
    _name = 'upoelectro.compra'

    fecha = fields.Datetime('Fecha', required=True, autodate = True)
    importe = fields.Float('Importe', digit=10, required=True)
    direccion = fields.Char('Dirección', size=60)
    codigo_postal = fields.Char('Código postal', size=5)
    ciudad = fields.Char('Ciudad', size=60)
    provincia = fields.Char('Provincia', size=60)
    proveedor_id = fields.Many2one('upoelectro.proveedor', 'Proveedor')
    empleado_id = fields.Many2one('upoelectro.empleado', 'Empleado')
    lineacompra_ids = fields.One2many('upoelectro.lineacompra', 'compra_id', 'Pedido')
    state = fields.Selection([('solicitada','Solicitada'),
                              ('aceptada','Aceptada'),
                              ('enconflicto','En Conflicto'),
                              ('cancelada', 'Cancelada'),
                              ('recibida','Recibida'),],
                              'Estado',
                              default='solicitada')
    @api.one
    def btn_submit_to_aceptada(self):
        self.write({'state':'aceptada'})
        
    @api.one
    def btn_submit_to_enconflicto(self):
        self.write({'state':'enconflicto'})
    
    @api.one
    def btn_submit_to_cancelada(self):
        self.write({'state':'cancelada'})
        
    @api.one
    def btn_submit_to_recibida(self):
        self.write({'state':'recibida'})
        
    @api.onchange('lineacompra_ids')
    def onchange_lineacompra(self):
        if self.state == 'recibida':
            
            for lineacompra in self.lineacompra_ids:
                lineacompra.articulo_id.stock = lineacompra.articulo_id.stock + lineacompra.cantidad
    
    @api.onchange('lineacompra_ids')
    def onchange_compra(self):
        self.importe = 0
        
        for lineacompra in self.lineacompra_ids:
            self.importe = self.importe + lineacompra.precio
    