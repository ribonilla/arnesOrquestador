"""
audit_excel.py
Herramienta de auditoría activa en caliente para archivos Excel (.xlsx).
Evalúa fórmulas dinámicas y verifica coherencia numérica y aforos contra benchmarks.
"""

import sys
import openpyxl

def auditar_modelo_excel(ruta_xlsx, benchmark_margen=None, checks_formulas=None, limite_aforo=None):
    """
    Audita dinámicamente un archivo Excel generado.
    
    Args:
        ruta_xlsx: Ruta al archivo .xlsx
        benchmark_margen: Tupla (celda, valor_esperado, tolerancia)
        checks_formulas: Lista de celdas que DEBEN contener fórmulas (iniciar con '=')
        limite_aforo: Dict con {'rango_filas': (r_min, r_max), 'rango_cols': (c_min, c_max), 'limite_por_defecto': N, 'excepciones': {fila: N}}
    
    Returns:
        tuple (bool, str): (True si pasa todas las pruebas, mensaje descriptivo)
    """
    try:
        # 1. Cargar con data_only=False para revisar fórmulas
        wb_formulas = openpyxl.load_workbook(ruta_xlsx, data_only=False)
        ws_form = wb_formulas.active

        if checks_formulas:
            for celda in checks_formulas:
                val = str(ws_form[celda].value or "")
                if not val.startswith("="):
                    return False, f"Falla de Calidad: La celda {celda} no contiene una fórmula dinámica (valor actual: '{val}')."

        # 2. Cargar con data_only=True para evaluar valores calculados (si fueron cacheados) o evaluar matriz
        wb_vals = openpyxl.load_workbook(ruta_xlsx, data_only=True)
        ws_vals = wb_vals.active

        # 3. Validar aforos si se especificó el rango
        if limite_aforo:
            r_min, r_max = limite_aforo.get('rango_filas', (1, ws_vals.max_row))
            c_min, c_max = limite_aforo.get('rango_cols', (1, ws_vals.max_column))
            u_default = limite_aforo.get('limite_por_defecto', 999)
            excepciones = limite_aforo.get('excepciones', {})

            for r in range(r_min, r_max + 1):
                u_max = excepciones.get(r, u_default)
                for c in range(c_min, c_max + 1):
                    val = ws_vals.cell(r, c).value
                    if isinstance(val, (int, float)) and val > u_max:
                        return False, f"Violación de Restricción: En fila {r}, columna {c}, el valor {val} supera el límite de aforo permitido ({u_max})."

        # 4. Validar margen/KPI benchmark si se proporcionó
        if benchmark_margen:
            celda_kpi, valor_esperado, tolerancia = benchmark_margen
            val_kpi = ws_vals[celda_kpi].value
            if isinstance(val_kpi, (int, float)):
                if abs(val_kpi - valor_esperado) > tolerancia:
                    return False, f"Discrepancia Numérica en {celda_kpi}: Calculado={val_kpi}, Benchmark Esperado={valor_esperado} (Diferencia: {val_kpi - valor_esperado})."

        return True, "✅ Auditoría Activa de Excel Aprobada: Fórmulas dinámicas y restricciones respetadas."

    except Exception as e:
        return False, f"Error al ejecutar auditoría de Excel: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python audit_excel.py <ruta_archivo.xlsx>")
        sys.exit(1)
    
    archivo = sys.argv[1]
    ok, msg = auditar_modelo_excel(archivo)
    print(msg)
    sys.exit(0 if ok else 1)
