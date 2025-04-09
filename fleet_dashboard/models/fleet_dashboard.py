from odoo import models, fields, api

class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    capacidad_kg = fields.Float(string="Capacidad (kg)")
    picking_ids = fields.One2many('stock.picking', 'vehicle_id', string="Pedidos Asignados")
    peso_total = fields.Float(string="Peso total cargado")
    used_weight_percentage = fields.Float(string="% Uso camión")  # Este campo es obligatorio para el kanban

    def _get_total_weight(self):
        for record in self:
            total = sum(p.peso_total for p in record.picking_ids)
            record.peso_total = total
            record.used_weight_percentage = (total / record.capacidad_kg) * 100 if record.capacidad_kg else 0


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    vehicle_id = fields.Many2one('fleet.vehicle', string="Camión asignado")
    peso_total = fields.Float(string="Peso del pedido (kg)")

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        for picking in records:
            if picking.picking_type_id.code == 'outgoing' and picking.vehicle_id:
                picking.vehicle_id._get_total_weight()
        return records

    def write(self, vals):
        res = super().write(vals)
        for picking in self:
            if picking.picking_type_id.code == 'outgoing' and (vals.get('vehicle_id') or picking.vehicle_id):
                picking.vehicle_id._get_total_weight()
        return res
