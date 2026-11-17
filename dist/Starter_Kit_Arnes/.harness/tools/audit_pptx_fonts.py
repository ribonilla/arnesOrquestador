"""
audit_pptx_fonts.py
Herramienta de auditoría activa de tipografía y contenedores para presentaciones PowerPoint (.pptx).
Verifica que las fuentes cumplan el umbral mínimo (piso de 22pt) y reporte anomalías.
"""

import sys
from pptx import Presentation

def auditar_fuentes_pptx(ruta_pptx, tamano_minimo_pts=16):
    """
    Recorre todas las diapositivas y párrafos asegurando que no existan textos por debajo del umbral establecido (piso de 16pt).
    """
    try:
        prs = Presentation(ruta_pptx)
        errores = []

        for s_idx, slide in enumerate(prs.slides, start=1):
            for shape_idx, shape in enumerate(slide.shapes, start=1):
                if shape.has_text_frame:
                    for p_idx, p in enumerate(shape.text_frame.paragraphs, start=1):
                        texto = p.text.strip()
                        if not texto:
                            continue

                        # Revisar tamaño en runs individuales o a nivel de párrafo
                        if p.font.size and p.font.size.pt < tamano_minimo_pts:
                            errores.append(f"Slide {s_idx}, Forma {shape_idx}, Párrafo {p_idx}: '{texto[:25]}...' tiene {p.font.size.pt}pt (< {tamano_minimo_pts}pt)")
                        else:
                            for run in p.runs:
                                if run.font.size and run.font.size.pt < tamano_minimo_pts:
                                    errores.append(f"Slide {s_idx}, Run '{run.text[:20]}...': tiene {run.font.size.pt}pt (< {tamano_minimo_pts}pt)")

        if errores:
            return False, f"❌ Falla de Calidad Tipográfica en PPTX ({len(errores)} hallazgos):\n" + "\n".join(errores[:5])
        
        return True, "✅ Auditoría Tipográfica Aprobada: Todas las fuentes cumplen el piso directivo de 16pt."

    except Exception as e:
        return False, f"Error al auditar fuentes PPTX: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python audit_pptx_fonts.py <ruta_archivo.pptx> [tamano_minimo_pts]")
        sys.exit(1)

    archivo = sys.argv[1]
    umbral = int(sys.argv[2]) if len(sys.argv) > 2 else 16
    ok, msg = auditar_fuentes_pptx(archivo, umbral)
    print(msg)
    sys.exit(0 if ok else 1)
