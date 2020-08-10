# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class bug_manage_advanced(models.Model):
#     _name = 'bug_manage_advanced.bug_manage_advanced'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100