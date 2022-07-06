# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class covid-19(models.Model):
#     _name = 'covid-19.covid-19'
#     _description = 'covid-19.covid-19'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
