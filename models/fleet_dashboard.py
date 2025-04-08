from odoo import models, fields, api

class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    capacidad_kg = fields.Float(string="Capacidad (kg)")
    picking_ids = fields.One2many('stock.picking', 'vehicle_id', string="Pedidos Asignados")

    def _get_total_weight(self):
        for record in self:
            total = sum(p.peso_total for p in record.picking_ids)
            record.peso_total = total
            record.porcentaje_uso = (total / record.capacidad_kg) * 100 if record.capacidad_kg else 0

    peso_total = fields.Float(string="Peso total cargado", compute="_get_total_weight", store=True)
    porcentaje_uso = fields.Float(string="% Uso camión", compute="_get_total_weight", store=True)

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    vehicle_id = fields.Many2one('fleet.vehicle', string="Camión asignado")
    peso_total = fields.Float(string="Peso del pedido (kg)")
