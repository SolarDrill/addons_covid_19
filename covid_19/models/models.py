# -*- coding: utf-8 -*-

from odoo import models, fields, api


class covid_19(models.Model):
    _name = 'covid.covid_19'

    source = fields.Char(string='Source', required=True)
    date = fields.Datetime(string='Date Time', required=True, default=fields.Datetime.now())
    country_id = fields.Many2one(comodel_name="res.country", string="", required=True)
    infected = fields.Integer(string="Infected", required=True, default=0)
    recovered = fields.Integer(string="Recovered", required=True, default=0)
    deceased = fields.Integer(string="Deceased", required=True, default=0)


#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
