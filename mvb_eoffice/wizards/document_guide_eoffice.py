# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class DocumentGuideEoffice(models.TransientModel):
    _name = 'document.guide.eoffice'
    _description = 'Tài liệu hướng dẫn sử dụng Module quản lý văn bản và điều hành'

    def name(self):
        res = 'Tài liệu hướng dẫn'
        return res
    name = fields.Char(string="", required=False, default=name)


