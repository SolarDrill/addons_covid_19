# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class covid_19(models.Model):
#     _name = 'covid_19.covid_19'
#     _description = 'covid_19.covid_19'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
