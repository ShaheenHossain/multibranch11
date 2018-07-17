# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class SaleReport(models.Model):
    _inherit = "sale.report"

    company_branch_id = fields.Many2one(
        'res.company.branch',
        string="Branch",
        readonly=True
    )

    def _select(self):
        select_str = super(SaleReport, self)._select()
        select_str += ", s.company_branch_id as company_branch_id"
        return select_str

    def _group_by(self):
        group_by_str = super(SaleReport, self)._group_by()
        group_by_str += ", s.company_branch_id"
        return group_by_str

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
