# Fleet Dashboard Report for Odoo 18

Este módulo agrega un panel de control visual y reportes PDF para visualizar la asignación de pedidos a camiones, facilitando la planificación logística en el módulo de Inventario de Odoo 18.

## 🚚 Funcionalidades principales

- Vista tipo **Dashboard** (kanban) para ver camiones con entregas asignadas.
- Reporte PDF tipo resumen con:
  - Nombre del camión.
  - Peso total cargado.
  - Porcentaje de uso de su capacidad.
  - Detalles de pedidos asignados (cliente, ciudad, región, peso).
- Reporte PDF tipo detallado (estilo pivote) con:
  - Camión, referencia del pedido, productos, cantidades y peso.
- Solo se muestran camiones con entregas asignadas.
- Acceso directo desde el menú **Inventario → Dashboard de Camiones**.

## 📦 Instalación

1. Copiar la carpeta `fleet_dashboard` en tu directorio de `custom_addons`.
2. Asegúrate de que el `addons_path` de tu `odoo.conf` incluya ese directorio.
3. Reinicia Odoo.
4. Entra en modo desarrollador.
5. Actualiza la lista de aplicaciones.
6. Instala el módulo desde la vista de Aplicaciones buscando "Fleet Dashboard".

## 🧠 Requisitos

- Odoo 18
- Módulos instalados:
  - `stock`
  - `fleet`
  - `web`

## 🛠 Estructura técnica

- `fleet.vehicle` extendido con campos de capacidad, peso cargado y pedidos.
- `stock.picking` extendido con campo de asignación a camión y peso total.
- Reportes generados con QWeb PDF.
- Dashboard visual con vista kanban personalizada.

## 🧪 Créditos

Desarrollado por **SimpleDigital.cl** para optimizar la logística y gestión de flotas en empresas con entregas asignadas a camiones.
