"""
Extractor de texto de archivos PDF a Markdown
Uso: python extract_pdf.py ruta_archivo.pdf [salida.md]
"""
import sys
import os

try:
    import pypdf
except ImportError:
    print("Instalando pypdf...")
    os.system(f"{sys.executable} -m pip install pypdf")
    import pypdf

def extract_pdf_to_md(pdf_path, output_md_path=None):
    if not os.path.exists(pdf_path):
        print(f"Error: No se encontró el archivo {pdf_path}")
        return
        
    reader = pypdf.PdfReader(pdf_path)
    total_pages = len(reader.pages)
    
    extracted_text = [f"# 📑 Extracción de Insumo PDF: {os.path.basename(pdf_path)}\n"]
    extracted_text.append(f"> **Total Páginas:** {total_pages}\n\n---\n")
    
    for i, page in enumerate(reader.pages, 1):
        extracted_text.append(f"## Página {i}\n")
        text = page.extract_text() or "(Página sin texto seleccionable o escaneada)"
        extracted_text.append(text + "\n\n---\n")
        
    final_md = "".join(extracted_text)
    
    if output_md_path:
        os.makedirs(os.path.dirname(os.path.abspath(output_md_path)), exist_ok=True)
        with open(output_md_path, "w", encoding="utf-8") as f:
            f.write(final_md)
        print(f"Texto extraído guardado en: {output_md_path}")
    else:
        print(final_md[:1000] + "\n...(truncado)...")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        out = sys.argv[2] if len(sys.argv) > 2 else None
        extract_pdf_to_md(sys.argv[1], out)
    else:
        print("Uso: python extract_pdf.py <archivo.pdf> [salida.md]")
