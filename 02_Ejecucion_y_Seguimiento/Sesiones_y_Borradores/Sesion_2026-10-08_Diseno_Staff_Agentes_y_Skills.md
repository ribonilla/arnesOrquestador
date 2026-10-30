# 💡 Sesión de Diseño: Arquitectura del Staff de Agentes, Skills y Scripts

**Fecha:** 2026-10-08  
**Participantes:** Ricardo Bonilla (Sponsor/Director) & Antigravity (Senior Architect)  
**Tema:** Definición del Staff de Agentes Especializados, Matriz de Skills y Gobernanza de Scripts

---

## 🔍 1. Necesidad y Contexto del Debate

El usuario identificó que para que el Arnés funcione a nivel profesional, el Agente no puede ser una figura monolítica genérica. Se requiere un **Orquestador Principal (Project Manager & Sparring)** que mantenga la disciplina operativa y un **Staff de Agentes Especialistas** que aporten competencias específicas de gestión, diseño, auditoría y comunicación.

---

## 👥 2. Definición del Staff de Agentes Especializados

```text
               🧙‍♂️ AGENTE ORQUESTADOR (Director Estratégico & PM)
                                     │
     ┌───────────────┬───────────────┼───────────────┬───────────────┐
     ▼               ▼               ▼               ▼               ▼
🏛️ Arquitecto   📋 Controller   📊 Auditor      📄 Diseñador    🎨 Especialista
  Bóveda          Kanban          Cuantitativo    Documental       Visual & PPTX
 (PARA/Zettel)   (Tareas)        (Financiero)    (Word/Minto)   / 🌐 Storytelling
```

1. **🧙‍♂️ Agente Orquestador (Director Estratégico & PM):**
   * *Misión:* Conducir el proyecto, evitar divagaciones, alertar salidas de alcance y orquestar a los especialistas.
2. **🏛️ Arquitecto de Bóveda (PARA / Zettelkasten):**
   * *Misión:* Estructurar el Business Case, interconectar notas y capitalizar aprendizajes atómicos sin duplicar.
3. **📋 Controller de Proyecto & Kanban:**
   * *Misión:* Mover las tareas en el tablero Kanban (`Por Hacer`, `En Progreso`, `Bloqueado`, `Hecho`) y actualizar el Centro de Mando.
4. **📊 Auditor Cuantitativo y Financiero:**
   * *Misión:* Auditar tablas de costos, presupuestos, flujos de caja, ROI, matrices de riesgo y consistencia numérica.
5. **📄 Diseñador Documental (Word & Memorandos):**
   * *Misión:* Estructurar informes ejecutivos de 1 a 3 páginas con principio de Minto y tono corporativo de alta dirección.
6. **🎨 Especialista en Diseño Visual & Presentaciones (PPTX):**
   * *Misión:* Diseñar la arquitectura de diapositivas, títulos de acción y guías de oratoria para comités directivos.
7. **🌐 Especialista en Storytelling Web (Executive HTML Slides):**
   * *Misión:* Generar presentaciones interactivas en formato web/HTML para lectura fluida en navegadores.
8. **😈 Abogado del Diablo (Simulador de Comité):**
   * *Misión:* Stress-test de propuestas antes de la entrega final para anticipar objeciones y puntos ciegos.

---

## 🛠️ 3. Matriz de Skills (Transversales vs. Particulares)

* **Skills Transversales (Todos los agentes):**
  * `trazabilidad-decisiones`: Registro obligatorio de cambios en la matriz de auditoría.
  * `persistencia-obsidian`: Escritura y lectura nativa en Markdown sin dejar datos sueltos en el chat.
  * `control-de-alcance`: Validación de que la tarea no rompa las restricciones del sponsor.

* **Skills Particulares:**
  * *Diseñador Visual:* `generacion-pptx-markdown` y `guia-oratoria`.
  * *Auditor Financiero:* `modelado-financiero-unit-economics` y `analisis-sensibilidad`.
  * *Especialista Web:* `executive-presentation-html` (presentaciones interactivas en HTML).

---

## ⚙️ 4. Gobernanza de Scripts y Zero-Fricción

* El usuario final **no escribe código ni comandos de consola**.
* El Agente Orquestador o el especialista correspondiente ejecuta los scripts necesarios en segundo plano y deposita el producto terminado directamente en `05_Entregables/`.

---

## 🚀 5. Próxima Tarea en el Kanban
* [x] Documentar esta sesión en la bóveda de Obsidian.
* [ ] Actualizar `.harness/Agentes/EXPERTOS_Y_ROLES.md` con las especificaciones del nuevo Staff de 8 roles.
