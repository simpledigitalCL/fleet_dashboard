def pre_init_check(env):
    if not env.registry.get('stock.picking'):
        raise Exception("El módulo 'stock' no está cargado. Instálalo antes de 'fleet_dashboard'.")

from . import models
