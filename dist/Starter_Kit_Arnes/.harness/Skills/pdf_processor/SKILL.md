---
name: pdf_processor
description: "Extracción estructurada de texto y tablas desde archivos PDF (políticas, contratos, informes de comités) para volcarlos directamente en 01_Estrategia_y_Alcance/."
---

# 📑 SKILL: PROCESAMIENTO Y EXTRACCIÓN DE PDFS

Esta skill permite procesar insumos crudos en PDF que envían clientes o directivos para transformarlos en texto estructurado en Markdown dentro de la bóveda.

---

## 🛠️ Script de Extracción (`extract_pdf.py`)
Utiliza `pypdf` o `pdfplumber`. Si falta, el agente lo instala automáticamente.
