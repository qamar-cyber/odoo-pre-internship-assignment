# noinspection PyUnresolvedReferences
from odoo import fields, models

class LinkEstateInvoice(models.Model):
    _name = 'link.estate.invoice'
    _description = 'Link Estate Invoice Model'

    estate_property_id = fields.Many2one('estate.property', string='Estate Property', required=True)
    invoice_id = fields.Many2one('account.invoice', string='Invoice', required=True)

    def create_invoice_for_estate(self, estate_property):
        invoice = self.env['account.invoice'].create({
            'partner_id': estate_property.customer_id.id,
            'date_invoice': fields.Date.today(),
        })
        self.invoice_id = invoice.idf