"""
Generador de Documentos Word (.docx) Corporativos
Uso: python create_docx.py --title "Título del Documento" --output "05_Entregables/Informe.docx" --content "ruta_o_texto.md"
"""
import sys
import os

try:
    from docx import Document
    from docx.shared import Inches, Pt, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.oxml import OxmlElement, parse_xml
    from docx.oxml.ns import nsdecls, qn
except ImportError:
    print("Instalando python-docx...")
    os.system(f"{sys.executable} -m pip install python-docx")
    from docx import Document
    from docx.shared import Inches, Pt, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.table import WD_TABLE_ALIGNMENT

def create_executive_doc(title, subtitle, sections, output_path):
    doc = Document()
    
    # Configuración de márgenes
    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)
        
    # Título Principal
    p_title = doc.add_paragraph()
    run_title = p_title.add_run(title)
    run_title.font.name = 'Calibri'
    run_title.font.size = Pt(24)
    run_title.font.bold = True
    run_title.font.color.rgb = RGBColor(15, 23, 42) # Slate 900
    
    # Subtítulo
    if subtitle:
        p_sub = doc.add_paragraph()
        run_sub = p_sub.add_run(subtitle)
        run_sub.font.name = 'Calibri'
        run_sub.font.size = Pt(13)
        run_sub.font.italic = True
        run_sub.font.color.rgb = RGBColor(71, 85, 105) # Slate 600
        
    doc.add_paragraph() # Espacio
    
    # Secciones
    for sec_title, sec_content in sections.items():
        h = doc.add_heading(sec_title, level=1)
        h.style.font.name = 'Calibri'
        h.style.font.color.rgb = RGBColor(30, 58, 138) # Navy Blue
        
        p = doc.add_paragraph(sec_content)
        p.style.font.name = 'Calibri'
        p.style.font.size = Pt(11)
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_after = Pt(8)

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    doc.save(output_path)
    print(f"Documento Word generado con éxito: {output_path}")

if __name__ == "__main__":
    # Test básico
    sample_sections = {
        "1. Resumen Ejecutivo": "Este documento resume los resultados del análisis estratégico...",
        "2. Propuesta de Valor": "La implementación del piloto permitirá validar la disposición de pago en B2B...",
        "3. Próximos Pasos": "Iniciar pruebas con la empresa aliada durante el mes en curso."
    }
    create_executive_doc("Informe Ejecutivo de Expansión", "Dirección General - Octubre 2026", sample_sections, "05_Entregables/Ejemplo_Informe.docx")
