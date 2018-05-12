# -*- coding: utf-8 -*-
from openerp import http

# class Myfirstmodel(http.Controller):
#     @http.route('/myfirstmodel/myfirstmodel/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/myfirstmodel/myfirstmodel/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('myfirstmodel.listing', {
#             'root': '/myfirstmodel/myfirstmodel',
#             'objects': http.request.env['myfirstmodel.myfirstmodel'].search([]),
#         })

#     @http.route('/myfirstmodel/myfirstmodel/objects/<model("myfirstmodel.myfirstmodel"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('myfirstmodel.object', {
#             'object': obj
#         })