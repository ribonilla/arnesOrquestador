---
name: xlsx_financial
description: "Modelado financiero y generación de hojas de cálculo (.xlsx) con fórmulas nativas (SUM, TIR, VAN), múltiples pestañas (Supuestos, Flujos, Resumen), formato contable y validación."
---

# 📊 SKILL: MODELADO FINANCIERO Y AUDITORÍA CUANTITATIVA (.XLSX)

Esta skill dota al **Auditor Cuantitativo y Financiero** de las capacidades para generar y estructurar hojas de cálculo profesionales en Excel.

---

## 📌 1. Principios de Modelado Financiero
1. **Separación de Capas:**
   * **Pestaña 1: Resumen Ejecutivo / Dashboard:** KPIs principales, gráficos y conclusiones.
   * **Pestaña 2: Proyecciones / Flujos:** Tablas dinámicas y cálculos paso a paso.
   * **Pestaña 3: Supuestos & Variables:** Todos los inputs (precios, costos, tasas) aislados para permitir análisis de sensibilidad sin tocar fórmulas.
2. **Fórmulas Nativas en Mayúsculas:** Usar `=SUM()`, `=NPV()`, `=IRR()`, `=XLOOKUP()`, evitando números quemados a mano (*hardcoded*).
3. **Formateo Numérico Estricto:** Moneda con dos decimales (`$#,##0.00`), porcentajes con un decimal (`0.0%`) y números enteros separados por comas.

---

## 🛠️ 2. Script de Generación Automática (`create_xlsx.py`)
Utiliza `openpyxl`. Si falta, el agente corre `pip install openpyxl` en segundo plano.
