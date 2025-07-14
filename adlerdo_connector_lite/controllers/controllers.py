# -*- coding: utf-8 -*-
# from odoo import http


# class AdlerdoConnectorLite(http.Controller):
#     @http.route('/adlerdo_connector_lite/adlerdo_connector_lite', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/adlerdo_connector_lite/adlerdo_connector_lite/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('adlerdo_connector_lite.listing', {
#             'root': '/adlerdo_connector_lite/adlerdo_connector_lite',
#             'objects': http.request.env['adlerdo_connector_lite.adlerdo_connector_lite'].search([]),
#         })

#     @http.route('/adlerdo_connector_lite/adlerdo_connector_lite/objects/<model("adlerdo_connector_lite.adlerdo_connector_lite"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('adlerdo_connector_lite.object', {
#             'object': obj
#         })

