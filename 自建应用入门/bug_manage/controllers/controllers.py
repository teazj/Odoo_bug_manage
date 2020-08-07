# -*- coding: utf-8 -*-
from odoo import http


class Bug(http.Controller):
    @http.route('/bug_manage')
    def bug_manage(self, **kw):
        bugs = http.request.env['bm.bug']  # 获取 bm.bug 记录集
        domain_bug = [('is_closed', '=', False)]  # 搜索条件
        bugs_open = bugs.search(domain_bug)  # 返回符合搜索条件的记录集
        return http.request.render('bug_manage.bugs_templates', {'bugs_open': bugs_open})


class Hello(http.Controller):
    @http.route('/hello', auth='public')
    def say_hello(self, **kw):
        return ('<h1>Hello World</h1>')

# class BugManage(http.Controller):
#     @http.route('/bug_manage/bug_manage/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bug_manage/bug_manage/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bug_manage.listing', {
#             'root': '/bug_manage/bug_manage',
#             'objects': http.request.env['bug_manage.bug_manage'].search([]),
#         })

#     @http.route('/bug_manage/bug_manage/objects/<model("bug_manage.bug_manage"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bug_manage.object', {
#             'object': obj
#         })
