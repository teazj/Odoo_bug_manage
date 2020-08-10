from odoo import api, models, fields


class BugStage(models.Model):
    # 模型属性
    _name = "bm.bug_stage"
    _description = "bug阶段"
    # _order是字段排序, seqience作为第一关键子,name为第二关键字
    _order = 'sequence asc,name asc'

    # 字符串相关类型
    name = fields.Char('名称')
    desc_detail = fields.Text("描述")
    status = fields.Selection([('waiting', '未开始'), ('doing', '进行中'),
                               ('clossed', '关闭'), ('rework', '重测为通过'), ], "状态")
    document = fields.Html("文档")

    # 数值相关类型
    sequence = fields.Integer('Sequence')
    percent_pro = fields.Float('进度', (3, 2))

    # 日期类型
    deadline = fields.Date('最晚解决日期')
    create_on = fields.Datetime("创建时间", default=lambda self: fields.Datetime.now())

    # 布尔类型
    dalay = fields.Boolean('是否延误')
    # 二进制类型
    image = fields.Binary("图片")

    # 关系字段
    bug_ids = fields.One2many("bm.bug", 'stage_id', string="bug")
