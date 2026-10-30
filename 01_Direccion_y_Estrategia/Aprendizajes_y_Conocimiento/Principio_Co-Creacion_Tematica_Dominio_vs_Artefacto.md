# 🧠 Principio de Co-Creación Temática: Separación entre Dominio y Artefacto

**Fecha:** 2026-10-11  
**Categoría:** Arquitectura de Agentes / Interacción Humano-IA  
**Contexto:** Arnés PARA-Zettelkasten  
**ID Relacionado:** DEC-14  

---

## 📌 Enunciado del Principio
> **"Nunca delegues la construcción de un artefacto formal a un LLM sin antes haber atravesado una fase socrática de maduración temática del contenido."**

---

## 🔍 El Problema Resuelto
La mayoría de los sistemas multiagente cometen el error de pasar directamente de la instrucción del usuario a la generación del documento final (Word, PowerPoint, Excel). Esto genera:
1. **Complacencia temprana:** El modelo produce documentos con formato impecable pero contenido superficial, lleno de lugares comunes o alucinaciones metodológicas.
2. **Desconexión de dominio:** Los agentes especializados en formato (como un redactor Minto o un diseñador PPTX) carecen de profundidad en temas complejos (ciberseguridad, finanzas actuariales, regulación bancaria, pedagogía).

---

## 🛠️ La Solución Arquitectónica (Patrón Synapse de 3 Capas)
Se divide la interacción en tres capas estrictamente diferenciadas:

1. **Capa 1: Gestión y Gobierno (🧙‍♂️ Agente Orquestador):**
   * Controla el tiempo, los plazos, las notas en Obsidian y el tablero Kanban.
2. **Capa 2: Co-Creación Temática (🧙🏾‍♂️ Professor Synapse & Experto Dinámico):**
   * Convoca dinámicamente al experto exacto del dominio requerido mediante la plantilla de 3 pasos.
   * Modela el problema con el usuario de forma socrática, paso a paso, debatiendo hipótesis y validando fórmulas.
   * La síntesis se persiste en la bitácora (`03_Sesiones_e_Ideacion/`).
3. **Capa 3: Producción y Blindaje de Artefactos (Especialistas + Gauntlet Loop):**
   * Solo cuando el contenido técnico está maduro, el especialista en formato empaqueta el producto final (DOCX, PPTX, XLSX, HTML).
   * La compuerta **Gauntlet Loop** (Harsh Critic / Abogado del Diablo) audita el resultado con un límite de 2 iteraciones.

---

## 🔗 Notas Relacionadas
* [[Principio_Delimitacion_Negativa_de_Alcance|Principio de Delimitación Negativa de Alcance]]
* [[04_Decisiones_y_Trazabilidad/Matriz_de_Cambios_y_Acuerdos|DEC-14: Integración de Professor Synapse]]
* [[.harness/Agentes/FLUJOGRAMA_ORQUESTADOR|Flujograma del Orquestador y Ciclo de Vida]]
