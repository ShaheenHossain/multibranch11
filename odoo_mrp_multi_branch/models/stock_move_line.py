# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    @api.model
    def create(self, vals):
        move_line_id = super(StockMoveLine, self).create(vals)
        if move_line_id.move_id and move_line_id.move_id.raw_material_production_id:
            move_line_id.company_branch_id = move_line_id.move_id.raw_material_production_id.company_branch_id.id
        return move_line_id

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: