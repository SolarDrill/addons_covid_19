# -*- coding: utf-8 -*-

from odoo import models, fields, api


class covid_19(models.Model):
    _name = 'covid.covid_19'
    _order = 'id descr'

    source = fields.Char(string='Source', required=True)
    date = fields.Datetime(string='Date Time', required=True, default=fields.Datetime.now())
    country_id = fields.Many2one(comodel_name="res.country", string="", required=True)
    infected = fields.Integer(string="Infected", required=True, default=0)
    recovered = fields.Integer(string="Recovered", required=True, default=0)
    deceased = fields.Integer(string="Deceased", required=True, default=0)
    total_infected = fields.Integer(string='Total Infected', compute='set_total_infected', required=True, default=0)
    total_recovered = fields.Integer(string='Total Recovered', compute='set_total_recovered', required=True, default=0)
    total_deceased = fields.Integer(string='Total Deceased', compute='set_total_deceased', required=True, default=0)

    def set_total_infected(self):
        for data in self:
            domain = [
                ('country_id', '=', data.country_id.id),
                ('date', '<', data.date),
                ]
            records = self.search(domain)
            infecteds = records.mapped('infected')
            data.total_infected = sum(infecteds)+data.infected

    def set_total_recovered(self):
        for data in self:
            domain = [
                ('country_id', '=', data.country_id.id),
                ('date', '<', data.date),
                ]
            records = self.search(domain)
            recovereds = records.mapped('recovered')
            data.total_recovered = sum(recovereds)+data.recovered

    def set_total_deceased(self):
        for data in self:
            domain = [
                ('country_id', '=', data.country_id.id),
                ('date', '<', data.date),
                ]
            records = self.search(domain)
            deceaseds = records.mapped('deceased')
            data.total_deceased = sum(deceaseds)+data.deceased

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
