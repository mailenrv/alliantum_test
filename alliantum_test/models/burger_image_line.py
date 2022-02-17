# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from random import randint

class BurgerImageLine(models.Model):
    _name = 'burger.image.category'
    _description = 'Burger Image Tags'
    _order = 'name'

    def _get_default_color(self):
        return randint(1, 11)

    name = fields.Char(string='Tag Name', required=True, translate=True)
    color = fields.Integer(string='Color Index', default=_get_default_color)


class BurgerImageLine(models.Model):
    _name = 'burger.image.line'
    _description = "Burger Image Line"
    _order = "id desc"

    product_tmpl_id = fields.Many2one('product.template', ondelete='cascade')
    image = fields.Image("Big Image", max_width=1920, max_height=1920, required=True)
    image_512 = fields.Image("Medium Image", related="image", max_width=512, max_height=512, store=True)
    image_128 = fields.Image("Small Image", related="image", max_width=128, max_height=128, store=True)
    title = fields.Char(required=True)
    category_ids = fields.Many2many('burger.image.category')



