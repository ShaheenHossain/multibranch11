# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class MrpBomLine(models.Model):
    _inherit = 'mrp.bom.line'

    company_branch_id = fields.Many2one(
        'res.company.branch',
        string="Branch",
        copy=False,
        default=lambda self: self.env.user.company_branch_id.id,
    )

    @api.model
    def create(self, vals):
        bom_id = self.env['mrp.bom'].browse(int(vals.get("bom_id")))
        if bom_id.company_branch_id and vals.get("company_branch_id") and not (vals.get("company_branch_id") == bom_id.company_branch_id.id):
            raise ValidationError("Branch Should be Same on BOM And BOM Line")
        return super(MrpBomLine, self).create(vals)

    @api.multi
    def write(self, vals):
        for rec in self:
            if rec.bom_id.company_branch_id and vals.get("company_branch_id") and not (vals.get("company_branch_id") == rec.bom_id.company_branch_id.id):
                raise ValidationError("Branch Should be Same on BOM And BOM Line")
        return super(MrpBomLine, self).write(vals)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: