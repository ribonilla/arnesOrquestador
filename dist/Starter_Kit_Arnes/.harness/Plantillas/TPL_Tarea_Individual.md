---
tipo: "tarea"
estado: "{{ESTADO}}" # "1_Por_Hacer" | "2_En_Progreso" | "3_Bloqueado" | "4_Completado"
prioridad: "{{PRIORIDAD}}" # "Alta" | "Media" | "Baja"
fase: "{{FASE}}"
asignado: "{{AGENTE_O_RESPONSABLE}}"
fecha_limite: "{{FECHA_LIMITE}}"
tags:
  - tarea
  - proyecto
---

# 📌 {{TITULO_TAREA}}

> **Objetivo de la Tarea:**
> {{DESCRIPCION_CLARA_DEL_RESULTADO_ESPERADO}}

---

## 🛠️ Criterios de Aceptación / Definición de Hecho (DoD)
- [ ] Criterio 1: {{CRITERIO_1}}
- [ ] Criterio 2: {{CRITERIO_2}}

---

## 📝 Notas y Evidencias
* Entregable o documento generado: [[05_Entregables/{{ARCHIVO}}|{{ARCHIVO}}]]
