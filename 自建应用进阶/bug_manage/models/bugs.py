from odoo import fields, models, api


class Bugs(models.Model):
    _name = "bm.bug"
    _description = "bug模型"
    name = fields.Char(string='bug简述', required=True)  # 特殊字段
    detail = fields.Text(size=150)
    is_closed = fields.Boolean(string="是否关闭")
    close_reason = fields.Selection([("changed", "已修改"), ("cannot", "无法修改"), ("delay", "推迟"), ],
                                    string="关闭理由")
    user_id = fields.Many2one('res.users', string="负责人",copy=False)
    follower_ids = fields.Many2many('res.partner', string='关注者')

    @api.multi
    def do_close(self):
        # 这里的self其实只有一条记录,因为是在表单视图中打开
        for item in self:
            item.is_closed = True
        return True
