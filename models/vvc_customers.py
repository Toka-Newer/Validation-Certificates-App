from odoo import models, fields

class Customers(models.Model):
    _name = 'vvc.customers'
    
    name = fields.Char(string="Name", max_length=50, required=True)
    phone = fields.Char(string="Phone", required=True)
