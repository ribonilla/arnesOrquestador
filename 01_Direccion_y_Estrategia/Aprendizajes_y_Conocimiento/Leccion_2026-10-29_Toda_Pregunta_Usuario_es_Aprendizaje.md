---
title: "Principio de Aprendizaje Continuo: Toda Pregunta o Discrepancia del Usuario es Objeto de Aprendizaje"
fecha: 2026-10-29 12:30
tipo: "leccion-aprendida-arquitectura"
modulo: "Arnés Metodológico de IA (Harness Engine)"
estado: "integrado-en-core"
tags:
  - aprendizaje-continuo
  - preguntas-usuario
  - auditoria-cognitiva
  - validacion-discrepancias
  - zettelkasten
---

# 🧠 Principio de Aprendizaje Continuo: Toda Interacción con Preguntas es un Aprendizaje

> **Regla de Operación:**
> Cada vez que el usuario realiza una pregunta para **comprender, aclarar, cuestionar o validar** una respuesta o un cálculo recibido (por ejemplo: *"no me cuadró la celda de Excel con el valor de pantalla"* o *"¿por qué tomaste este supuesto?"*), **dicha interacción es obligatoriamente objeto de una nota de aprendizaje en la bóveda**.

---

## 🔍 1. El Problema Detectado en Sesiones Reales

En la práctica habitual con LLMs ocurren dos fallas silenciosas:
1. **La disculpa efímera:** Ante una observación del usuario (*"no me cuadró el Excel"*), el modelo responde: *"Tienes toda la razón, discúlpame, hay un error en la fórmula..."*, corrige el valor en el chat y el conocimiento se pierde en cuanto finaliza la sesión.
2. **La aclaración no capitalizada:** Si el usuario estaba equivocado por un malentendido de supuestos y el agente le explica la razón correcta, el usuario aprende momentáneamente pero el sistema no documenta la fuente de confusión. En el siguiente proyecto, otro usuario (o el mismo) tropezará con la misma duda.

---

## 🏛️ 2. Protocolo de Captura de Aprendizajes por Preguntas

Ante cualquier pregunta, duda o reporte de descuadre del usuario, el agente debe activar un ciclo de tres pasos:

```text
[Pregunta / Descuadre del Usuario]
               │
               ▼
   [Análisis Técnico y Causa Raíz]
         │                 │
         ▼                 ▼
[Usuario tiene razón]   [Usuario tenía duda conceptual]
         │                 │
  (Error de cálculo/     (Definición ambigua/
   fórmula en artefacto)  supuesto implícito)
         │                 │
         └────────┬────────┘
                  ▼
   [Creación Inmediata de Nota Atómica]
   01_Direccion_y_Estrategia/Aprendizajes_y_Conocimiento/
```

### Escenario A: El usuario tiene la razón (Hallazgo de Error)
* **Acción en el entregable:** Corregir inmediatamente la fórmula o dato en el archivo correspondiente (`.xlsx`, `.docx`, `.pptx`, `.html`).
* **Acción en Aprendizajes:** Generar nota atómica documentando:
  - *Qué preguntó/notó el usuario.*
  - *Causa raíz técnica del error (fórmula circular, rango desfasado, supuesto omitido).*
  - *Cómo se corrigió y qué regla de validación debe aplicarse para evitar su reaparición.*

### Escenario B: El usuario tenía una duda o concepción distinta (Clarificación de Regla de Negocio)
* **Acción en el diálogo:** Explicar con evidencia técnica y pedagógica por qué el cálculo es correcto, validando primero que la duda era razonable.
* **Acción en Aprendizajes:** Documentar la aclaración como **Criterio de Negocio / Glosario Operativo**:
  - *Qué causó la aparente discrepancia.*
  - *Cuál es la definición canónica acordada.*
  - *Cómo presentar el dato en futuros reportes para que sea auto-explicativo y no genere suspicacias.*

---

## 📂 3. Campos Mínimos de la Nota de Aprendizaje por Pregunta

Toda nota generada por este detonante debe registrar:
1. **Fecha y Hora (`YYYY-MM-DD HH:MM`)** en el frontmatter.
2. **Pregunta / Inquietud Original del Usuario.**
3. **Diagnóstico Técnico y Validación de Causa.**
4. **Veredicto y Acción Tomada** (Corrección de artefacto o precisión de criterio).
5. **Regla de Blindaje Futuro** (Para el staff de agentes y usuarios futuros).
