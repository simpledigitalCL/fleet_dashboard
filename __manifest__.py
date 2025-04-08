{
    "name": "Fleet Dashboard Report",
    "version": "1.0",
    "category": "Inventory",
    "summary": "Dashboard PDF con pedidos asignados a camiones",
    "depends": ["fleet", "web"],
    "data": [
        "views/fleet_dashboard_view.xml",
        "views/fleet_dashboard_detailed_view.xml",
        "views/fleet_dashboard_kanban_view.xml",
        "views/fleet_dashboard_menu_view.xml",
        "report/fleet_dashboard_report.xml",
        "report/fleet_dashboard_report_detailed.xml",
    ],
    "assets": {},
    "installable": True,
    "application": True,
}
