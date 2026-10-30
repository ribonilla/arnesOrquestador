---
title: "Lección de Arquitectura: Experiencia de Usuario en Bóvedas de IA y Protocolo Gauntlet Riguroso"
fecha: 2026-10-13
tipo: leccion-aprendida-arquitectura
modulo: "Arnés Metodológico de IA (Harness Engine)"
estado: integrado-en-core
tags:
  - ux-vault-design
  - minimalismo-obsidian
  - gauntlet-4-bloques
  - revisor-adversarial
  - living-document
---

# 🧠 Lección de Arquitectura: UX en Bóvedas de IA y Rigor Adversarial

> **Problema Detectado en Pruebas de Usuario:**
> 1. Los usuarios finales sufrían de parálisis de navegación ante un árbol de carpetas sobrecargado con nombres técnicos (PARA, Zettelkasten, numeración 01 a 06).
> 2. Al activar el control de calidad, los LLMs tendían a la complacencia superficial cuando se les pedía "ser un abogado del diablo", aprobando errores numéricos o formatos ilegibles.

---

## 🏛️ 1. Principio de Experiencia de Usuario: La Regla de las 3 Macro-Carpetas

Un profesional de oficina no busca taxonomías metodológicas; busca respuestas a 3 preguntas operativas básicas:

```text
1. "¿Por qué y bajo qué reglas hacemos esto?"  --> 01_Direccion_y_Estrategia/
2. "¿En qué estamos trabajando hoy?"           --> 02_Ejecucion_y_Seguimiento/
3. "¿Qué tengo que enviarle a mi jefe/comité?" --> 03_Entregables_Finales/
```

### Reglas de Diseño de Bóveda:
* **Separación de Taller vs. Escaparate:** Las sesiones de debate y borradores viven en `02_Ejecucion_y_Seguimiento/Sesiones_y_Borradores/`. El escaparate (`03_Entregables_Finales/`) solo contiene archivos vigentes limpios.
* **Preservación Histórica sin Ruido:** Los archivos Word (`.docx`) nunca deben duplicarse como obsoletos en la raíz. Solo existe UN Word definitivo. Los históricos y diffs en color rojo (`<span style="color:#DC2626;">`) se preservan exclusivamente en Markdown dentro de `Historico/`.

---

## 🔬 2. Principio del Revisor Adversarial: Cero Analogías y Fórmula de 4 Bloques

Para evitar que el agente apruebe ciegamente por apariencia estética:
1. **Erradicación de Términos Blandos:** Se sustituye "Abogado del Diablo" por **Revisor Adversarial (*Adversarial Auditor / Harsh Critic*)**.
2. **Plantilla Canónica de 4 Bloques:**
   * **`[TAREA]`:** Definición inequívoca del producto.
   * **`[MÉTODO]`:** Loop cerrado disociado (`Planificar -> Construir -> Auditar dinámicamente -> Subsanar`). Prohibición explícita: *"No me entregues la primera versión"*.
   * **`[LISTÓN]`:** Criterio binario ejecutable (ej. correr script `audit_excel.py` para contrastar contra el modelo canónico o `audit_pptx_fonts.py` para validar piso de 22pt).
   * **`[ENTREGABLE]`:** Destino limpio en `03_Entregables_Finales/` y acta de dictamen en `01_Direccion_y_Estrategia/Decisiones_y_Acuerdos/`.

---

## 🔍 3. El Sub-Rol: Auditor de Bóveda & Chief of Staff

El agente no es solo un redactor; es el **relator auditable del proyecto**:
* Ante preguntas del usuario (*"¿Qué acordamos?", "¿Por qué cambió este número?"*), rastrea la bóveda y responde con citaciones exactas (`[[DEC-XX]]`, `[[Sesion_...]]`).
* Genera informes de acuerdos y control de cambios a demanda de manera persistente.
