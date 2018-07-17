# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    company_branch_id = fields.Many2one(
        'res.company.branch',
        string="Branch",
        copy=False,
        default=lambda self: self.env.user.company_branch_id.id,
    )

    def _generate_raw_move(self, bom_line, line_data):
        result = super(MrpProduction, self)._generate_raw_move(bom_line=bom_line, line_data=line_data)
        if bom_line:
            result.company_branch_id = bom_line.company_branch_id
        else:
            result.company_branch_id = self.company_branch_id
        return result

    def _workorders_create(self, bom, bom_data):
        workorders = super(MrpProduction, self)._workorders_create(bom=bom, bom_data=bom_data)
        for workorder in workorders:
            workorder.company_branch_id = self.company_branch_id.id
        return workorders

    @api.onchange('product_id', 'picking_type_id', 'company_id')
    def onchange_product_id(self):
        result = super(MrpProduction, self).onchange_product_id()
        if self.bom_id:
            self.company_branch_id = self.bom_id.company_branch_id.id
        return result

    @api.depends('move_finished_ids.move_line_ids')
    def _compute_lines(self):
        result = super(MrpProduction, self)._compute_lines()
        for production in self:
            production.finished_move_line_ids.write({'company_branch_id':production.company_branch_id.id})

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
