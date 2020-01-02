from odoo import models, fields, api

class almacen(models.Model):
    _name = 'upoelectro.almacen'

    identificador = fields.Integer('ID', required=True)
    localizacion = fields.Char('Localizacion', size=120, required=True)
    foto = fields.Binary('Nuestras instalaciones')
    empleados_ids = fields.Many2many('upoelectro.empleado', string='Empleados')
    categorias_ids = fields.Many2many('upoelectro.categoria', string='Categorías')
    
    nEmp = fields.Integer(compute='_empleados_count',string='Nº Empleados',store=True)
    
    _sql_constraints = [('almacen_identificador_unique','UNIQUE (identificador)','El identificador debe ser único')]
    
    @api.one
    @api.depends('empleados_ids')
    def _empleados_count(self):

        x = self.env['upoelectro.almacen']
        
        for almacen in self:
            cont = 0
        
            for rec in almacen.empleados_ids:
            
                cont+=1
            
            almacen.nEmp= cont

    
    def eliminarEmpleadosCategorias(self):         
        self.write({'empleados_ids':[ (5,  ) ]})
        self.write({'categorias_ids':[ (5,  ) ]})    