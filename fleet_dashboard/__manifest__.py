{
    "name": "Fleet Dashboard Report Simpledigital",
    "version": "1.0",
    "author": "Simpledigital",
    "website": "https://simpledigital.cl",
    "category": "Inventory",
    "summary": "Dashboard PDF con pedidos asignados a camiones",
    "depends": ["stock", "fleet", "web"],
    "data": [
        "data/picking_type_config.xml",
        "data/server_action_update_dashboard.xml",
        "views/fleet_dashboard_view.xml",
        "views/fleet_dashboard_detailed_view.xml",
        "views/fleet_dashboard_kanban_view.xml",
        "views/fleet_dashboard_menu_view.xml",
        "report/fleet_dashboard_report.xml",
        "report/fleet_dashboard_report_detailed.xml",
    ],
    "installable": True,
    "application": True,
    "pre_init_hook": "pre_init_check"
}
