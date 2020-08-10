from odoo import api, models, fields


class BugAdvanced(models.Model):
    _inherit = "bm.bug"
    # 这里新增一个所需的时间字段
    need_time = fields.Integer('所需时间(小时)')
    # 为 bm.bug 的name字段添加help属性
    # 注意: 不是覆盖,是补充 => name = fields.Char(string='bug简述', required=True,help="简要描述发现的bug")
    name = fields.Char(help="简要描述发现的bug")

    # 关系字段
    stage_id = fields.Many2one('bm.bug_stage', string="阶段")
    tag_ids = fields.Many2many("bm.bug_tag",
                               string="标签",
                               relation="bm_bug_tag_rel",
                               column1="bug_id",
                               column2="tag_id")
