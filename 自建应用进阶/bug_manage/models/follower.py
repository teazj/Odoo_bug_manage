from odoo import models, fields, api


class Follower(models.Model):
    _inherit = 'res.partner'  # 继承字段,声明要继承类的_name
    bug_ids = fields.Many2many('bm.bug', string="bug")  # 新增字段
