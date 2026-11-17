#!/usr/bin/env python3
"""
build_starter_zip.py
Generador oficial y determinista del Starter Kit descargable del Arnés.
Empaqueta únicamente el motor, agentes, reglas y guías, garantizando
que NO incluya ninguna carpeta de proyecto (01_, 02_, 03_) ni 00_Centro_de_Mando.md.
"""

import os
import zipfile

# Archivos y carpetas permitidos en el paquete mínimo
INCLUDED_ROOT_FILES = [
    "AGENTS.md",
    "GEMINI.md",
    "CLAUDE.md",
    "GUIA_ESTRUCTURA_BOVEDA.md",
    "README.md",
    "requirements.txt",
    ".gitignore",
    "LICENSE",
    "01_Direccion_y_Estrategia/README.md",
    "02_Ejecucion_y_Seguimiento/README.md",
    "03_Entregables_Finales/README.md",
]

INCLUDED_DIRS = [
    ".harness",
]

# Exclusiones estrictas dentro de directorios permitidos
EXCLUDED_EXTENSIONS = [
    ".pyc",
    ".pyo",
    ".tmp",
    ".temp",
    ".DS_Store",
]

EXCLUDED_DIR_NAMES = [
    "__pycache__",
    ".git",
    ".obsidian",
    ".trash",
]

def build_zip(output_filename="arnes_starter.zip"):
    workspace_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    output_path = os.path.join(workspace_root, output_filename)
    
    print(f"📦 Construyendo starter kit limpio en: {output_path}")
    
    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zip_out:
        # 1. Archivos raíz seleccionados
        for filename in INCLUDED_ROOT_FILES:
            file_path = os.path.join(workspace_root, filename)
            if os.path.isfile(file_path):
                print(f"  + Agregando archivo raíz: {filename}")
                zip_out.write(file_path, arcname=filename)
            else:
                print(f"  ⚠️ Archivo no encontrado (omitido): {filename}")

        # 2. Directorios autorizados (.harness)
        for folder_name in INCLUDED_DIRS:
            dir_path = os.path.join(workspace_root, folder_name)
            if os.path.isdir(dir_path):
                for root, dirs, files in os.walk(dir_path):
                    # Filtrar directorios excluidos en caliente
                    dirs[:] = [d for d in dirs if d not in EXCLUDED_DIR_NAMES]
                    
                    for f in files:
                        ext = os.path.splitext(f)[1]
                        if ext in EXCLUDED_EXTENSIONS or f in EXCLUDED_DIR_NAMES:
                            continue
                        
                        full_path = os.path.join(root, f)
                        rel_path = os.path.relpath(full_path, workspace_root)
                        print(f"  + Agregando motor: {rel_path}")
                        zip_out.write(full_path, arcname=rel_path)
            else:
                print(f"  ⚠️ Directorio no encontrado: {folder_name}")

    print(f"\n✅ Starter Kit empaquetado exitosamente con estructura limpia: {output_path}")
    print(f"   Tamaño: {os.path.getsize(output_path) / 1024:.2f} KB")

if __name__ == "__main__":
    build_zip()
