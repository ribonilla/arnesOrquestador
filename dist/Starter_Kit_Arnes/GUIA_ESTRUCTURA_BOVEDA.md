# 🏛️ Guía Rápida de Navegación de la Bóveda (Arquitectura Minimalista)

Bienvenido a tu Bóveda de Trabajo con Inteligencia Artificial. Esta estructura está diseñada bajo la **Regla de las 3 Macro-Carpetas** para eliminar la fricción técnica y permitirte encontrar reportes, acuerdos y tareas en un solo clic.

---

## 🗺️ Mapa de Orientación Rápida

```text
📁 MI PROYECTO (Raíz)
 │
 ├── 🎯 00_Centro_de_Mando.md        <-- Dashboard general y brújula de acceso rápido
 │
 ├── 📁 01_Direccion_y_Estrategia/   <-- ¿Por qué lo hacemos y bajo qué reglas?
 │    ├── Alcance_y_Objetivos/       <-- Mandato, sponsor y límites innegociables
 │    ├── Decisiones_y_Acuerdos/     <-- Matriz de cambios y acuerdos auditables
 │    └── Aprendizajes_y_Conocimiento/ <-- Banco de lecciones aprendidas y Prompts
 │
 ├── 📁 02_Ejecucion_y_Seguimiento/  <-- ¿En qué estamos trabajando hoy?
 │    ├── Kanban_y_Tareas/           <-- Tablero Kanban (.base) y notas de tareas
 │    └── Sesiones_y_Borradores/     <-- Minutas de ideación y reflexiones con IA
 │
 └── 📁 03_Entregables_Finales/      <-- ¿Qué tengo que entregarle a mi jefe?
      ├── (Raíz)                     <-- Word (.docx), Markdown (.md), Excel, PPTX, HTML limpios
      └── Historico/                 <-- Versiones anteriores con diferencias en rojo
```

---

## 🧭 ¿Qué vas a encontrar en cada carpeta?

| Carpeta | Pregunta Clave | Qué contiene y qué vas a encontrar |
|---|---|---|
| **`🎯 00_Centro_de_Mando.md`** | *¿Dónde estoy parado?* | Tablero de resumen del proyecto, porcentaje de avance, fase activa y accesos directos a notas clave. |
| **`📁 01_Direccion_y_Estrategia/`** | *¿Por qué y bajo qué reglas?* | • **Alcance:** Definición del cliente/jefe y restricciones duras.<br>• **Decisiones:** Registro con fecha y hora (`YYYY-MM-DD HH:MM`) de cada acuerdo o cambio de números.<br>• **Aprendizajes:** Banco Zettelkasten de buenas prácticas, biblioteca de `Prompts/` sugeridos y lecciones aprendidas por preguntas o descuadres. |
| **`📁 02_Ejecucion_y_Seguimiento/`** | *¿En qué trabajamos hoy?* | • **Kanban:** Tablero visual interactivo en Obsidian Bases (`Tablero_Kanban.base`) y notas individuales de cada hito (`TAR_XX`).<br>• **Sesiones:** Resúmenes automáticos de debates, lluvias de ideas y trabajo en sucio (`Sesion_YYYY-MM-DD_HHmm_Tema.md`). |
| **`📁 03_Entregables_Finales/`** | *¿Qué le entrego a mi jefe?* | • **Escaparate Limpio:** Informes en Word (`.docx`), copias idénticas en Markdown (`.md`), modelos en Excel (`.xlsx`), diapositivas en PowerPoint (`.pptx`) y reportes web interactivos (`.html` en tema claro con letra grande).<br>• **Histórico:** Versiones pasadas en Markdown con cambios resaltados en rojo (`Historico/`). |

---

## 💡 Respuestas a Preguntas Habituales

### *"¿Y esta respuesta que recibo en el chat estará en la bóveda? ¿Dónde la encuentro?"*
* **Si fue una sesión de análisis o debate:** El agente la guarda automáticamente en `02_Ejecucion_y_Seguimiento/Sesiones_y_Borradores/Sesion_YYYY-MM-DD_HHmm_Tema.md`.
* **Si acordaron cambiar un número o alcance:** Queda asentada en `01_Direccion_y_Estrategia/Decisiones_y_Acuerdos/Matriz_de_Cambios_y_Acuerdos.md`.
* **Si fue un informe o entregable directivo:** Lo encuentras en `03_Entregables_Finales/` en formato Word y Markdown.
* **Si hiciste una pregunta para aclarar un descuadre o validar un cálculo:** El agente corrige el artefacto y crea una lección en `01_Direccion_y_Estrategia/Aprendizajes_y_Conocimiento/`.

### *"¿Cómo veo el flujograma metodológico de lo que está haciendo el arnés?"*
Puedes preguntarle directamente al agente: *"Dime qué estás haciendo"* o consultar el flujograma visual en:
👉 **`[.harness/Agentes/FLUJOGRAMA_ORQUESTADOR.md](file:///.harness/Agentes/FLUJOGRAMA_ORQUESTADOR.md)`**.
El arnés opera un ciclo transparente: **Diagnóstico $\to$ Plan Concertado $\to$ Especialista de Dominio $\to$ Compuerta Gauntlet (Calidad) $\to$ Auto-Escritura $\to$ Aprendizajes**.
