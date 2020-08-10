from odoo import api, fields, models


class BugTag(models.Model):
    _name = 'bm.bug_tag'
    _description = "bug标签"

    name = fields.Char('名称')

    # 关系字段
    bug_ids = fields.Many2many("bm.bug", string="bug", )
