---
fecha: 2026-10-29 12:30
tema: "Mejoras de Experiencia de Usuario en Bóveda, Prompts Asistidos, Preguntas como Aprendizaje, Kanban Base y HTML Claro"
participantes:
  - "Ricardo Bonilla (Sponsor)"
  - "Director Estratégico & Chief of Staff (IA)"
tipo: "sesion-ideacion-y-arquitectura"
estado: "concluida"
---

# 💡 Sesión 2026-10-29 12:30: Calibración de UX, Prompts Asistidos y Estándares del Arnés

> **Contexto de la Sesión:**
> A partir de múltiples pruebas en casos reales de proyectos corporativos y SvelteKit, el sponsor levantó 6 oportunidades clave de mejora para optimizar la usabilidad de la bóveda, la comprensión del arnés y la calidad de los entregables.

---

## 📌 1. Diagnóstico de Oportunidades Identificadas

1. **Biblioteca de Prompts y Enriquecimiento Asistido:**
   * *Problema:* El usuario pide cosas con frases cortas o ambiguas (*"guarda en la bóveda"*). El usuario no tiene por qué conocer la arquitectura de carpetas.
   * *Solución:* Crear la subcarpeta `01_Direccion_y_Estrategia/Aprendizajes_y_Conocimiento/Prompts/` para registrar patrones de cómo pide el usuario y cómo sugerirle versiones de alto impacto. Además, instruir al arnés a clasificar automáticamente con máximo detalle sin esperar rutas técnicas del usuario.
2. **Toda Pregunta del Usuario es un Aprendizaje:**
   * *Problema:* Si el usuario detecta un descuadre (ej. *"no me cuadró el Excel"*), el modelo solía disculparse en chat y corregir efímeramente, perdiéndose la causa raíz.
   * *Solución:* Regla obligatoria: toda pregunta o reporte de descuadre detona una investigación de causa y una nota atómica en `Aprendizajes_y_Conocimiento/`, tanto si el usuario tenía la razón (error de cálculo) como si tenía una duda conceptual (regla de negocio a clarificar).
3. **Despliegue Correcto del Tablero Kanban en Obsidian Bases:**
   * *Problema:* El filtro apuntaba a una carpeta histórica no existente (`02_Planificacion_y_Kanban/Tareas`), impidiendo que Obsidian Bases renderizara las tarjetas automáticamente.
   * *Solución:* Corregir la ruta en `Tablero_Kanban.base` y en `TPL_02_Tablero_Kanban.base` hacia `02_Ejecucion_y_Seguimiento/Kanban_y_Tareas/Tareas`.
4. **Visibilidad del Flujograma y Comprensión del Arnés:**
   * *Problema:* Usuarios en proyectos externos (ej. SvelteKit) quieren ver qué hace el arnés y cómo opera.
   * *Solución:* Referenciar de forma prominente `[.harness/Agentes/FLUJOGRAMA_ORQUESTADOR.md](file:///.harness/Agentes/FLUJOGRAMA_ORQUESTADOR.md)` y crear `README.md` / `GUIA_ESTRUCTURA_BOVEDA.md` para responder inmediatamente a *"¿qué estás haciendo?"*.
5. **Presentaciones HTML en Tema Claro y Letra Grande por Defecto:**
   * *Problema:* Entregables HTML cargaban con tipografía pequeña requiriendo zoom excesivo en navegadores y proyectores.
   * *Solución:* Estandarizar la skill `web_storytelling` y las reglas del sistema para exigir **tema claro corporativo por defecto** y un piso tipográfico de **18px-19px para cuerpo** y encabezados de gran impacto.
6. **Guía de Orientación de Carpetas (Evitar Parálisis):**
   * *Problema:* Usuarios se pierden y dudan si sus respuestas de chat están guardadas en disco.
   * *Solución:* Crear `GUIA_ESTRUCTURA_BOVEDA.md`, `README.md` en la raíz y actualizar los READMEs de cada macro-carpeta explicando el contenido exacto y la respuesta a *"¿dónde está mi respuesta del chat?"*.

---

## 🛠️ 2. Acciones y Artefactos Desplegados

* Creación de `01_Direccion_y_Estrategia/Aprendizajes_y_Conocimiento/Prompts/README.md`.
* Creación de `PROMPT_01_Persistencia_y_Registro_Boveda.md`.
* Creación de `Leccion_2026-10-29_Toda_Pregunta_Usuario_es_Aprendizaje.md`.
* Corrección de `Tablero_Kanban.base` y plantilla `TPL_02_Tablero_Kanban.base`.
* Actualización de `web_storytelling/SKILL.md` (tema claro y escala tipográfica).
* Actualización de reglas en `.harness/REGLAS_OPERATIVAS_IA.md`, `AGENTS.md`, `GEMINI.md`, `CLAUDE.md`.
* Generación de `README.md` y `GUIA_ESTRUCTURA_BOVEDA.md` en raíz y subcarpetas.
* Registro de decisión DEC-17 en la `Matriz_de_Cambios_y_Acuerdos.md`.
* Sincronización y reconstrucción de `dist/Starter_Kit_Arnes/` y `dist/Starter_Kit_Arnes_Universal.zip`.
