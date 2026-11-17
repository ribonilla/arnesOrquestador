"""
Generador de Modelos Financieros y Hojas de Cálculo (.xlsx) Profesionales
"""
import sys
import os

try:
    import openpyxl
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
    from openpyxl.utils import get_column_letter
except ImportError:
    print("Instalando openpyxl...")
    os.system(f"{sys.executable} -m pip install openpyxl")
    import openpyxl
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
    from openpyxl.utils import get_column_letter

def create_financial_model(project_name, output_path):
    wb = openpyxl.Workbook()
    
    # 1. Pestaña de Resumen
    ws_summary = wb.active
    ws_summary.title = "Resumen Ejecutivo"
    ws_summary.views.sheetView[0].showGridLines = True
    
    # Estilos
    header_fill = PatternFill(start_color="1E3A8A", end_color="1E3A8A", fill_type="solid")
    header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    title_font = Font(name="Calibri", size=16, bold=True, color="0F172A")
    kpi_font = Font(name="Calibri", size=14, bold=True, color="1E3A8A")
    
    ws_summary["A1"] = f"Modelo Financiero: {project_name}"
    ws_summary["A1"].font = title_font
    
    headers = ["Año / Periodo", "Ingresos Proyectados", "Costos Operativos", "Margen Bruto", "EBITDA"]
    for col_num, header in enumerate(headers, 1):
        cell = ws_summary.cell(row=3, column=col_num)
        cell.value = header
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center")
        
    # Datos de ejemplo y fórmulas
    sample_data = [
        ("Año 1", 100000, 60000),
        ("Año 2", 180000, 95000),
        ("Año 3", 320000, 150000),
    ]
    
    for idx, (yr, rev, cost) in enumerate(sample_data, 4):
        ws_summary[f"A{idx}"] = yr
        ws_summary[f"B{idx}"] = rev
        ws_summary[f"C{idx}"] = cost
        ws_summary[f"D{idx}"] = f"=B{idx}-C{idx}"
        ws_summary[f"E{idx}"] = f"=D{idx}*0.85" # Estimación EBITDA
        
        # Formatos
        ws_summary[f"B{idx}"].number_format = "$#,##0"
        ws_summary[f"C{idx}"].number_format = "$#,##0"
        ws_summary[f"D{idx}"].number_format = "$#,##0"
        ws_summary[f"E{idx}"].number_format = "$#,##0"
        
    # Ajuste de ancho de columnas
    for col in ws_summary.columns:
        max_len = max(len(str(cell.value or '')) for cell in col)
        col_letter = get_column_letter(col[0].column)
        ws_summary.column_dimensions[col_letter].width = max(max_len + 4, 14)
        
    # 2. Pestaña de Supuestos
    ws_assumptions = wb.create_sheet(title="Supuestos y Variables")
    ws_assumptions.views.sheetView[0].showGridLines = True
    ws_assumptions["A1"] = "Variables Clave del Modelo"
    ws_assumptions["A1"].font = title_font
    
    assumptions = [
        ("Tasa de Crecimiento Anual", 0.35, "0.0%"),
        ("Costo Unitario de Adquisición (CAC)", 320, "$#,##0"),
        ("Tasa de Descuento (WACC)", 0.12, "0.0%"),
    ]
    
    ws_assumptions["A3"] = "Parámetro"
    ws_assumptions["B3"] = "Valor"
    ws_assumptions["A3"].font = Font(bold=True)
    ws_assumptions["B3"].font = Font(bold=True)
    
    for idx, (param, val, fmt) in enumerate(assumptions, 4):
        ws_assumptions[f"A{idx}"] = param
        ws_assumptions[f"B{idx}"] = val
        ws_assumptions[f"B{idx}"].number_format = fmt
        
    ws_assumptions.column_dimensions["A"].width = 35
    ws_assumptions.column_dimensions["B"].width = 15

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    wb.save(output_path)
    print(f"Modelo Excel generado con éxito: {output_path}")

if __name__ == "__main__":
    create_financial_model("Expansión B2B", "05_Entregables/Ejemplo_Modelo_Financiero.xlsx")
