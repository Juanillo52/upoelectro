# -*- coding: utf-8 -*-
from odoo import http

# class Upoelectro(http.Controller):
#     @http.route('/upoelectro/upoelectro/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/upoelectro/upoelectro/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('upoelectro.listing', {
#             'root': '/upoelectro/upoelectro',
#             'objects': http.request.env['upoelectro.upoelectro'].search([]),
#         })

#     @http.route('/upoelectro/upoelectro/objects/<model("upoelectro.upoelectro"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('upoelectro.object', {
#             'object': obj
#         })