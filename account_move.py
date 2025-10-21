from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    amount_discount = fields.Monetary(
        string='Total Diskon', 
        compute='_compute_amount_discount', 
        store=True
    )

    @api.depends('invoice_line_ids.discount', 'invoice_line_ids.price_unit', 'invoice_line_ids.quantity')
    def _compute_amount_discount(self):
        for move in self:
            total_discount = 0.0
            for line in move.invoice_line_ids:
                # Menghitung nilai diskon per baris: (harga * qty) * (diskon % / 100)
                line_discount = (line.price_unit * line.quantity) * (line.discount / 100)
                total_discount += line_discount
            move.amount_discount = total_discount