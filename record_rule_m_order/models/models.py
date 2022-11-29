from odoo import models, fields, api

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    user_id_r = fields.Many2one('res.users', string='Responsible', required=False, default=lambda self: self.env.user)
