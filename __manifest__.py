# -*- coding: utf-8 -*-
{
    'name': "upoelectro",
    'summary': """UPOELECTRO management""",
    'description': """UPOELECTRO management:classes, users, material...""",
    'author': "Equipo 01",
    'category': 'UPOElectro',
    'version': '0.1',
    'depends': ['base'],
    'data': ['views/upoelectro_cliente_view.xml', 'views/upoelectro_venta_view.xml', 'views/upoelectro_empleado_view.xml', 
             'views/upoelectro_proveedor_view.xml', 'views/upoelectro_compra_view.xml', 'views/upoelectro_almacen_view.xml'],
    'demo': ['demo/upoelectro_prueba_demo.xml'],
    'application': True,
}