---
tipo: contrato_logro
fecha: {{FECHA}}
tema: {{TEMA}}
tarea: {{TAR_ID}}
estado: propuesto
nivel_logro: {{NIVEL}}
---

# Contrato de Logro: {{TEMA}}

Define qué significa "listo" para esta tarea antes de construirla. El nivel elegido fija el listón del Gauntlet ([[.harness/templates/PLANTILLA_GAUNTLET_PROMPT]]) y se guarda en la tarea como `nivel_logro`.

Cada criterio se responde Pasa o No pasa. Un "No pasa" en cualquier criterio del nivel elegido impide cerrar la tarea.

---

## 🟢 Óptimo

- **Qué significa:** entrega sólida con revisión mínima. Cubre lo pedido, sin extras.
- **Para qué sirve:** borradores, consultas rápidas o entregables que se revisarán después.
- **Rondas del Gauntlet:** exactamente 2.

**Criterios (Pasa / No pasa):**
- [ ] El entregable responde a la solicitud escrita y al Business Case vigente.
- [ ] Las cifras clave pueden rastrearse a su fuente.
- [ ] No quedan textos ni números marcados como pendientes.

---

## 🔵 Profesional (por defecto)

- **Qué significa:** entrega revisada por el Revisor Adversarial, lista para un comité.
- **Para qué sirve:** la mayoría de entregables de trabajo ante dirección.
- **Rondas del Gauntlet:** entre 2 y 4 (mínimo 2, máximo 4).

**Criterios (Pasa / No pasa):**
- [ ] Cumple todos los criterios de Óptimo.
- [ ] Cero discrepancias numéricas entre el entregable y su fuente o modelo.
- [ ] Cero números fijos en celdas o cálculos que deberían depender de fórmulas, cuando aplique.
- [ ] Respeta el formato acordado (tipo de archivo, plantilla y extensión).
- [ ] Si es un documento, responde las 5 preguntas del marco ejecutivo.

---

## 🔴 Retador (auditoría activa)

- **Qué significa:** el listón actual del arnés, con auditoría ejecutable en frío.
- **Para qué sirve:** entregables finales, cifras que se deciden con base en ellas o presentaciones de alta dirección.
- **Rondas del Gauntlet:** entre 2 y 4 (mínimo 2, máximo 4), con auditoría activa en cada ronda.

**Criterios (Pasa / No pasa), preset Retador:**
- [ ] Gate 0 de Datos completado antes de cualquier cruce: cardinalidad, PK verificada y relación 1:1, 1:N o N:M declarada.
- [ ] Excel aprobado por `.harness/tools/audit_excel.py`, sin números fijos en celdas de cálculo y sin violar aforos o techos de capacidad.
- [ ] PPTX aprobado por `.harness/tools/audit_pptx_fonts.py`, con piso tipográfico de 16pt y textos encapsulados en formas nativas.
- [ ] HTML con viewport 16:9, navegación por flechas y espacio, y `@media print` limpio.
- [ ] El Revisor Adversarial no deja discrepancias abiertas tras la última ronda.

---

## 🧠 Propuesta de Synapse

Solicitud: {{SOLICITUD_RESUMIDA}}

- **Óptimo:** {{PROPUESTA_OPTIMO}}
- **Profesional:** {{PROPUESTA_PROFESIONAL}}
- **Retador:** {{PROPUESTA_RETADOR}}

¿Cuál nivel quieres? (Óptimo, Profesional o Retador). Si no eliges, usamos Profesional.

---

## ✅ Aprobación

- **Estado:** `propuesto` (cambia a `aprobado` o `editado` al decidir)
- **Nivel elegido:** {{NIVEL}}
- **Fecha y hora de decisión:** {{FECHA_HORA_DECISION}} (formato `YYYY-MM-DD HH:MM`, con `date +%Y-%m-%d %H:%M`)
