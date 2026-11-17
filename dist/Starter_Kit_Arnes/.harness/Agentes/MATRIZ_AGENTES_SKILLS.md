# 🗺️ MATRIZ DE AGENTES, SKILLS Y SCRIPTS

Esta matriz establece qué habilidades (`Skills`) y utilidades (`Scripts`) tiene asignadas cada uno de los roles del Staff de Agentes.

---

| Agente Especialista | Carpeta de Skill Asociada | Scripts Principales | Formato de Salida Generado |
|---|---|---|---|
| **🧙‍♂️ Orquestador & PM** | `.harness/Skills/COMANDOS_RAPIDOS.md` | Auto-bootstrap / Diagnóstico | `00_Centro_de_Mando.md` |
| **🏛️ Arquitecto PARA/Zettelkasten** | `.harness/Skills/pdf_processor/` | `extract_pdf.py` | `01_Estrategia_y_Alcance/` & `06_Zettelkasten/` |
| **📋 Controller Kanban** | `.harness/Skills/COMANDOS_RAPIDOS.md` | Gestión Markdown nativo | `02_Planificacion_y_Kanban/` |
| **📊 Auditor Cuantitativo / Financiero** | `.harness/Skills/xlsx_financial/` | `create_xlsx.py` | `05_Entregables/*.xlsx` |
| **📄 Diseñador Documental (Word)** | `.harness/Skills/docx_executive/` | `create_docx.py` | `05_Entregables/*.docx` |
| **🎨 Especialista Visual & PPTX** | `.harness/Skills/pptx_executive/` | Generadores OOXML / Markdown Deck | `05_Entregables/*.pptx` / Guía de Oratoria |
| **🌐 Especialista Storytelling Web** | `.harness/Skills/web_storytelling/` | Plantillas Slide HTML | `05_Entregables/*.html` |
| **😈 Abogado del Diablo** | `.harness/Agentes/EXPERTOS_Y_ROLES.md` | Simulador Pre-Mortem | `04_Decisiones_y_Trazabilidad/` |

---

## ⚙️ Regla de Auto-Instalación de Dependencias
Cuando el Agente deba compilar un archivo binario (`.docx`, `.xlsx`, `.pptx`, `.pdf`), ejecuta los scripts de Python con auto-instalación transparente de dependencias en caso de faltar (`python-docx`, `openpyxl`, `pypdf`).
