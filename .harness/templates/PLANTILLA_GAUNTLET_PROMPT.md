# 🛡️ PLANTILLA CANÓNICA: PROTOCOLO GAUNTLET LOOP
## Estructura de 4 Bloques: [TAREA] + [MÉTODO] + [LISTÓN] + [ENTREGABLE]

Esta plantilla estandariza el llamado exacto y riguroso para la ejecución adversarial en tareas críticas del arnés. Se prohíben términos analógicos débiles; el rol evaluador opera formalmente como **Revisor Adversarial (*Adversarial Auditor / Harsh Critic*)**.

---

## 📋 Estructura Textual Obligatoria

```text
================================================================================
🛡️ ACTIVACIÓN FORMAL: PROTOCOLO GAUNTLET LOOP
================================================================================

[TAREA]:
Diseña y desarrolla de forma autónoma: {DESCRIPCIÓN_EXACTA_DEL_REQUERIMIENTO}.
Construye los artefactos necesarios garantizando rigor técnico, integridad matemática y estándar ejecutivo de nivel directivo.

[MÉTODO]:
Trabaja en loop cerrado: planifica, construye, audita dinámicamente, corrige y repite.
NO ME ENTREGUES LA PRIMERA VERSIÓN.
Opera bajo una disociación estricta de dos roles técnicos independientes:

1. CONSTRUCTOR (BUILDER):
   - Especialista técnico del dominio pertinente ({ROL_ESPECIALISTA}).
   - Responsable de estructurar la propuesta, programar modelos, redactar informes y diseñar entregables según las especificaciones del proyecto.

2. REVISOR ADVERSARIAL (ADVERSARIAL AUDITOR / HARSH CRITIC):
   - Auditor técnico e independiente que NO participó en la construcción del artefacto.
   - Su único objetivo es buscar fallos técnicos, numéricos y de formato a propósito, como si su incentivo fuera rechazar y tumbar el entregable.
   - TIENE PROHIBIDO APROBAR POR APARIENCIA: No evalúa texto superficial. En hojas de cálculo debe ejecutar scripts de evaluación dinámica en frío; en presentaciones debe auditar jerarquía y contenedores; en documentos debe cotejar trazabilidad total de fuentes.
   - El bucle repite internamente: si el Revisor Adversarial detecta un fallo, el Constructor refactoriza de inmediato (máximo 2 rondas de corrección interna antes de escalar al usuario).

[LISTÓN OBSERVABLE]:
Un entregable definitivo que firmaría sin tocar una sola coma el directivo o auditor más exigente e implacable de la organización.
Criterios binarios de rechazo inmediato (Pasa / No Pasa):
- Hojas de Cálculo (.xlsx): Cero discrepancias numéricas contra el modelo formal. Cero números fijos quemados en celdas de cálculo. Cero violaciones de aforos físicos o techos de capacidad. Auditoría activa aprobada con `.harness/tools/audit_excel.py`.
- Presentaciones (.pptx): Piso tipográfico absoluto de 16pt en cuerpo de texto, celdas y notas directivas. Textos 100% encapsulados en formas nativas (cero cuadros flotantes desalineados). Auditoría activa aprobada con `.harness/tools/audit_pptx_fonts.py`.
- Presentaciones Web (.html): Viewport panorámico 16:9, navegación nativa con flechas de teclado y barra de avance visual.
- Documentos Ejecutivos (.docx / .md):
  * **Framework de las 5 Preguntas:** (1) ¿Cuál es la Situación Actual?, (2) ¿Qué Genera esta Situación?, (3) ¿Qué Podemos Hacer?, (4) ¿Qué se Hizo o se Propone Hacer?, (5) Escenarios de Salida, Beneficios y Riesgos. Cero fórmulas crudas o tecnicismos innecesarios.
  * **Entrega Bimodal:** El Word (.docx) es la versión final limpia. Simultáneamente se genera la réplica exacta en Markdown (.md).
  * **Histórico y Diff:** Todo histórico vive en Markdown en `03_Entregables_Finales/Historico/` con marcado explícito de cambios en rojo (<span style="color:#DC2626;">).
  * **Descargo de Auditoría Humana Obligatorio:** Todo artefacto debe incluir al final el aviso recordando al usuario la validación de cifras clave antes de la toma de decisiones.

[ENTREGABLE]:
1. Artefacto final aprobado en `03_Entregables_Finales/{NOMBRE_ARCHIVO}`.
2. Certificado de auditoría y dictamen de aprobación asentado en `01_Direccion_y_Estrategia/Decisiones_y_Acuerdos/`.
================================================================================
```

---

## ⚙️ Guía de Uso para el Orquestador

1. **Cuándo emitir este prompt:** Ante cualquier solicitud que involucre modelos financieros, balances de carga, memorandos ejecutivos para comités o presentaciones institucionales.
2. **Cómo reportar al usuario:**
   * El Orquestador no muestra las quejas intermedias a menos que se active el *Circuit Breaker* (2 iteraciones fallidas).
   * Cuando el Revisor Adversarial emite el dictamen `✅ APROBADO`, el Orquestador entrega el artefacto final con el resumen de las pruebas en frío que superó.
