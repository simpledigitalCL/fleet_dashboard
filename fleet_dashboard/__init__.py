def pre_init_check(cr):
    from odoo import api, SUPERUSER_ID
    env = api.Environment(cr, SUPERUSER_ID, {})
    if not env.registry.get('stock.picking'):
        raise Exception("El módulo 'stock' no está cargado. Instálalo antes de 'fleet_dashboard'.")

from . import models
