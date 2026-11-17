---
titulo: "Sesión: Plantilla Limpia, Skills de Terceros y Bóveda de Trabajo en Carpeta Aparte"
fecha: "2026-11-17 16:32"
tipo: "Sesion de Trabajo / Cierre Ejecutivo"
autor: "Ricardo Bonilla"
rol: "Consultor en Ciencia de Datos"
estado: "Completada"
repo: "arnesOrquestador (rama refactor/plantilla-limpia)"
bóveda: "arnes-boveda (worktree de la rama dev-vault)"
---

# 📋 Resumen de Sesión: Plantilla Limpia, Skills de Terceros y Bóveda de Trabajo

## 🎯 Objetivo de la Sesión
Separar la plantilla del arnés de la bóveda viva de desarrollo. La plantilla debe quedar limpia para que un clon nuevo no herede notas de desarrollo, y la bóveda de trabajo debe vivir en una carpeta aparte que el usuario abre en Obsidian.

---

## 🛠️ Trabajo Realizado

1. **Fase A: Respaldo y limpieza de la plantilla.**
   - Se creó la rama `dev-vault` (commit `185a68e`) como respaldo de la bóveda viva.
   - En `refactor/plantilla-limpia` se retiró la bóveda viva de la plantilla (63 archivos) y se eliminaron las copias duplicadas del kit.
   - Se restauraron `dist/` y los entregables del curso, porque el sitio de Netlify los usa.
2. **Fase B: Entradas cortas y skills.**
   - `CLAUDE.md`, `AGENTS.md` y `GEMINI.md` quedan en 12 líneas, con enlace a `REGLAS_OPERATIVAS_IA.md`, que abre con la secuencia de 8 pasos.
   - Se eliminaron las cinco skills propias de `.harness/Skills/`. El arnés funciona en modo básico y el bootstrap revisa si faltan.
   - Se redactó la guía `INSTALACION_SKILLS` con un comando por herramienta: `npx skills add <repo> -a <motor> -s <skill> --copy -y`.
3. **Pruebas de instalación.**
   - Probado en carpeta temporal con Claude Code, OpenCode y Antigravity (`agy`).
   - Pendiente: Gemini CLI, Codex, Pi y macOS.
4. **Diagramas Mermaid.**
   - Validados sintácticamente con mermaid 11.
   - No renderizados todavía en Obsidian. El render visual queda pendiente de confirmación del usuario.
5. **Configuración de la bóveda.**
   - `.obsidian/appearance.json` se dejó de rastrear en git (commit `f2e3e83`), porque el hook de revisión pedía consentimiento por ese archivo.
   - La bóveda de trabajo se creó como worktree de `dev-vault` en la carpeta `arnes-boveda`.

---

## ⚖️ Decisiones Registradas
* **DEC-27:** [[01_Direccion_y_Estrategia/Decisiones_y_Acuerdos/Matriz_de_Cambios_y_Acuerdos|Respaldo antes de limpiar]] (rama `dev-vault`).
* **DEC-28:** Plantilla limpia en `refactor/plantilla-limpia`.
* **DEC-29:** Entradas cortas y secuencia única (entradas de 12 líneas).
* **DEC-30:** Sin skills de terceros dentro del repositorio.
* **DEC-31:** Instalación de skills con un comando por herramienta.
* **DEC-32:** Bóveda de trabajo en carpeta aparte, `arnes-boveda`.

---

## ⏳ Pendientes (no completados)
* **Fase C:** niveles de logro y `TPL_07_Contrato_de_Logro.md`.
* **Fase D:** bóveda navegable (índices con Bases y bloque "Dónde quedé").
* **Fase E:** comando `/guardar` con recibo.
* **Fase F:** `requirements.txt`, `LICENSE` y dependencias.
* **Pruebas de motores:** Gemini CLI, Codex, Pi y macOS.
* **Render visual de mermaids en Obsidian:** el usuario lo confirma.
* **Manual de uso:** `03_Entregables_Finales/Manual_de_Uso_del_Arnes.html`, líneas ~773-776, mencionan skills eliminadas.
* **Revisión de cambios:** el hook de revisión pidió consentimiento varias veces por `.obsidian/appearance.json`. Ya se dejó de rastrear.

---

## 🚀 Siguiente Paso
Completar la Fase C (niveles de logro y `TPL_07_Contrato_de_Logro.md`) y corregir las líneas del manual que mencionan skills eliminadas. Ver [[02_Ejecucion_y_Seguimiento/Kanban_y_Tareas/Tareas/TAR_07_Plantilla_Limpia_y_Skills|TAR_07]].
