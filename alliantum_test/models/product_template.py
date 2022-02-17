# -*- coding: utf-8 -*-
from odoo import _, api, fields, models
from odoo.exceptions import UserError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_burger = fields.Boolean(string='Is a Burger')
    size = fields.Selection([('sm', 'SM'),
                             ('m', 'M'),
                             ('l', 'L'),
                             ('xl', 'XL')], string='Size')
    meat = fields.Selection([('beef', 'Beef'),
                             ('pig', 'Pig'),
                             ('chicken', 'Chicken'),
                             ('peas', 'Peas'),
                             ('soja', 'Soja')], default='beef', string='Meat')
    limited_edition = fields.Boolean(string='Limited Edition')
    is_vegan = fields.Boolean(string='Is Vegan')
    gluten_free = fields.Boolean(string='Gluten Free')
    author = fields.Many2one('res.partner', string='Author',  domain="[('supplier_rank', '=', 1)]")
    slogan = fields.Char(string='Slogan', translate=True)
    rating = fields.Integer()
    popularity = fields.Selection([('low', 'Low'),
                                   ('medium', 'Medium'),
                                   ('high', 'High')], string='Popularity', readonly=True, compute='_compute_popularity',
                                  store=True)
    vegan_warning = fields.Boolean(compute='_compute_vegan_warning', store=True)
    burger_image_ids = fields.One2many('burger.image.line', 'product_tmpl_id')

    @api.onchange('rating')
    def no_negative_values(self):
        for value in self:
            if value.rating < 0:
                raise UserError(_("Values set on rating must be positives"))

    @api.depends('rating')
    def _compute_popularity(self):
        for record in self:
            if 0 <= record.rating <= 4000:
                record.popularity = 'low'
            elif 4000 < record.rating <= 10000:
                record.popularity = 'medium'
            else:
                record.popularity = 'high'

    @api.depends('is_vegan','meat')
    def _compute_vegan_warning(self):
        for record in self:
            vegan_warning = False
            if record.is_vegan and record.meat not in ('peas','soja'):
                vegan_warning = True
            record.vegan_warning = vegan_warning

