# -*- coding: utf-8 -*-
from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    delivery_address = fields.Text(
        string='Delivery Address',
        compute='_compute_delivery_address',
        store=True
    )

    product_details = fields.Text(
        string='Products',
        compute='_compute_product_details',
        store=True
    )

    @api.depends('partner_id', 'partner_id.street', 'partner_id.street2', 'partner_id.city', 
                'partner_id.state_id', 'partner_id.zip', 'partner_id.country_id')
    def _compute_delivery_address(self):
        for picking in self:
            if picking.partner_id:
                address_parts = []
                partner = picking.partner_id
                if partner.name:
                    address_parts.append(partner.name)
                if partner.street:
                    address_parts.append(partner.street)
                if partner.street2:
                    address_parts.append(partner.street2)
                if partner.city:
                    address_parts.append(partner.city)
                if partner.state_id:
                    address_parts.append(partner.state_id.name)
                if partner.zip:
                    address_parts.append(partner.zip)
                if partner.country_id:
                    address_parts.append(partner.country_id.name)
                picking.delivery_address = '\n'.join(filter(None, address_parts))
            else:
                picking.delivery_address = False

    @api.depends('move_ids', 'move_ids.product_id', 'move_ids.product_uom_qty', 'move_ids.product_uom')
    def _compute_product_details(self):
        for picking in self:
            product_lines = []
            for move in picking.move_ids:
                # Get product variant complete name (including attributes)
                product_name = move.product_id.display_name
                # Format quantity with UOM
                qty_str = f"{move.product_uom_qty} {move.product_uom.name}"
                # Add line with product name and quantity
                product_lines.append(f"{product_name}: {qty_str}")
            
            picking.product_details = '\n'.join(product_lines) if product_lines else False