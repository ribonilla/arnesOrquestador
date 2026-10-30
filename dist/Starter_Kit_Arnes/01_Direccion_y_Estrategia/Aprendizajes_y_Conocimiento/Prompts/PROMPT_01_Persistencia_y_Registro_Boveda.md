---
title: "Patrón de Prompt: De 'Guarda en la Bóveda' a Persistencia Estructurada y Auditable"
fecha: 2026-10-29 12:30
tipo: "patron-prompt"
categoria: "persistencia-y-trazabilidad"
intencion: "Registrar acuerdos, minutas o entregables sin forzar al usuario a conocer la estructura de carpetas"
tags:
  - prompts
  - ingenieria-de-prompts
  - auto-escritura
  - boveda-obsidian
---

# 💬 Patrón de Prompt: Persistencia Estructurada vs. "Guarda en la Bóveda"

> **Premisa Fundamental:**
> El usuario **no tiene ni debe por qué conocer la arquitectura de carpetas de la bóveda**. Sin embargo, cuando dice únicamente *"guarda en la bóveda"*, se pierde la oportunidad de calificar la naturaleza de la información (¿es una decisión definitiva, una sesión exploratoria o una regla de negocio reutilizable?).

---

## 🗣️ 1. Expresión Habitual del Usuario (Entrada Cruda)

```text
"Guarda esto en la bóveda"
"Por favor archiva lo que acabamos de hablar"
```

### ¿Qué ocurre internamente si no se optimiza?
* El agente suele volcar todo en una sola nota genérica o preguntar con indecisión dónde guardarlo.
* Se mezclan decisiones vinculantes con borradores o ideas sueltas.
* Se pierde el sello de tiempo (`YYYY-MM-DD HH:MM`) y la clasificación automática en las 3 macro-carpetas.

---

## 🚀 2. Formulación Sugerida de Alto Impacto (Prompt Enriquecido)

Si el usuario desea sugerir o pedirle al sistema un registro impecable, la formulación sugerida es:

```text
"Registra los acuerdos y conclusiones de esta sesión diferenciando:
1. Decisiones vinculantes y compromisos adquiridos (con fecha, responsable y justificación).
2. Tareas resultantes para el tablero de seguimiento.
3. Lecciones o criterios que deban quedar como regla de oro para futuros trabajos."
```

---

## 💎 3. ¿Por qué es mejor la formulación sugerida?

| Dimensión | Entrada Cruda ("Guarda en la bóveda") | Formulación Sugerida |
|---|---|---|
| **Claridad de Destino** | Ambiguo (¿Borrador, acuerdo o entregable?) | Conduce al destino exacto: `Decisiones/`, `Kanban/` y `Aprendizajes/`. |
| **Trazabilidad** | Texto plano sin responsables ni causas. | Matriz con responsable, fecha y criterio de cambio. |
| **Reusabilidad** | Se archiva y se olvida en un archivo suelto. | Queda indexado como nota atómica en el banco Zettelkasten. |
| **Carga Cognitiva** | El usuario debe revisar luego qué se guardó. | El agente responde con enlaces exactos a cada nota creada. |

---

## 🤖 4. Mapeo Automático del Arnés (Comportamiento del Agente)

Aun cuando el usuario utilice la frase corta cotidiana (*"guarda en la bóveda"*), el arnés está configurado para:
1. **Interpretar la naturaleza del contenido:**
   - Si hubo debate/análisis $\to$ Escribe en `02_Ejecucion_y_Seguimiento/Sesiones_y_Borradores/Sesion_YYYY-MM-DD_HHmm_Tema.md`.
   - Si hubo cambio de criterio o números $\to$ Asienta en `01_Direccion_y_Estrategia/Decisiones_y_Acuerdos/Matriz_de_Cambios_y_Acuerdos.md`.
   - Si hubo una lección o resolución de duda $\to$ Crea nota atómica en `01_Direccion_y_Estrategia/Aprendizajes_y_Conocimiento/`.
2. **Presentar al usuario la síntesis con enlaces directos:** Notificando exactamente dónde quedó registrado cada aspecto sin obligarlo a conocer rutas técnicas.
