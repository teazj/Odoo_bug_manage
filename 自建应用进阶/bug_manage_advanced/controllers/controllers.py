# -*- coding: utf-8 -*-
from odoo import http

# class BugManageAdvanced(http.Controller):
#     @http.route('/bug_manage_advanced/bug_manage_advanced/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bug_manage_advanced/bug_manage_advanced/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bug_manage_advanced.listing', {
#             'root': '/bug_manage_advanced/bug_manage_advanced',
#             'objects': http.request.env['bug_manage_advanced.bug_manage_advanced'].search([]),
#         })

#     @http.route('/bug_manage_advanced/bug_manage_advanced/objects/<model("bug_manage_advanced.bug_manage_advanced"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bug_manage_advanced.object', {
#             'object': obj
#         })