from odoo import models, fields, api

class proveedor(models.Model):
    _name = 'upoelectro.proveedor'

    identificador = fields.Integer('ID', required=True)
    name = fields.Char('Nombre completo', size=60, required=True)
    telefono = fields.Char('Teléfono', size=9)
    correo = fields.Char('Correo', size=20)
    direccion = fields.Char('Dirección', size=60)
    codigo_postal = fields.Char('Código postal', size=5)
    ciudad = fields.Char('Ciudad', size=60)
    provincia = fields.Char('Provincia', size=60)
    foto = fields.Binary('Foto de perfil')
    compras_ids = fields.One2many('upoelectro.compra','proveedor_id', 'Compras')
    nCompras = fields.Integer(compute='_compras_count',string='Nº Compras',store=True)
    
    @api.depends('compras_ids')
    def _compras_count(self):

        x = self.env['upoelectro.proveedor']
        
        for proveedor in self:
            cont = 0
        
            for rec in proveedor.compras_ids:
            
                cont+=1
            
            proveedor.nCompras= cont
    
    _sql_constraints = [('proveedor_identificador_unique','UNIQUE (identificador)','El identificador debe ser único')]