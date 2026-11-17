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
El listón se fija con el nivel elegido en el Contrato de Logro (paso 4 de la secuencia; plantilla pendiente, Fase C).
Criterios binarios de rechazo inmediato (Pasa / No Pasa):
- Hojas de Cálculo (.xlsx): Cero discrepancias numéricas contra el modelo formal. Cero números fijos quemados en celdas de cálculo. Cero violaciones de aforos físicos o techos de capacidad. Auditoría activa aprobada con `.harness/tools/audit_excel.py`.
- Tablas y cruces (.xlsx, .csv, bases de datos), Gate 0 de Datos antes de cualquier unión, cruce o cálculo relacional: (1) perfilar cardinalidad y verificar unicidad de la PK candidata; si no hay PK simple, identificar la clave compuesta mínima (script `.harness/tools/audit_table_cardinality.py`); (2) declarar la relación 1:1, 1:N o N:M; queda prohibido unir por la clave del lado "Muchos" sin regla de desambiguación (agrupación previa, filtro temporal o clave compuesta); (3) alinear la granularidad del entregable: entidad agregada o transaccional.
- Presentaciones (.pptx): Piso tipográfico absoluto de 16pt en cuerpo de texto, celdas y notas directivas. Textos 100% encapsulados en formas nativas (cero cuadros flotantes desalineados). Auditoría activa aprobada con `.harness/tools/audit_pptx_fonts.py`.
- Presentaciones Web (.html): Viewport panorámico 16:9, navegación nativa con flechas de teclado y espacio, barra de avance visual y reglas de impresión limpia (`@media print`).
- Documentos Ejecutivos (.docx / .md):
  * **Framework de las 5 Preguntas:** (1) ¿Cuál es la Situación Actual? (contexto y cifras de negocio), (2) ¿Qué Genera esta Situación? (causas raíz), (3) ¿Qué Podemos Hacer? (opciones viables), (4) ¿Qué se Hizo o se Propone Hacer? (recomendación y plan), (5) Escenarios de Salida, Beneficios y Riesgos (matriz de impacto). Cero fórmulas crudas o tecnicismos innecesarios.
  * **Entrega Bimodal:** El Word (.docx) es la versión final limpia. Simultáneamente se genera la réplica exacta en Markdown (.md).
  * **Histórico y Diff:** Todo histórico vive en Markdown en `03_Entregables_Finales/Historico/` con marcado explícito de cambios en rojo (<span style="color:#DC2626;">). La versión vigente en Markdown encabeza con `🟢 VERSIÓN VIGENTE - Iteración N.N` e incluye una Tabla de Historial de Iteraciones (fecha, solicitante, qué cambió y justificación). Alternativa al rojo: alertas `[!WARNING]`.
  * **Descargo de Auditoría Humana Obligatorio:** Todo entregable en chat, Word, Markdown y hojas de cálculo cierra con este aviso, sin modificarlo:
  > ⚠️ **Aviso de Auditoría:** *Este entregable ha sido verificado dinámicamente por el arnés, pero no reemplaza el criterio experto. Es indispensable que el usuario revise supuestos, valores y fórmulas clave antes de su presentación o toma de decisiones. En caso de discrepancia, solicite una corrección de escenario.*

[ENTREGABLE]:
1. Artefacto final aprobado en `03_Entregables_Finales/{NOMBRE_ARCHIVO}`.
2. Certificado de auditoría y dictamen de aprobación asentado en `01_Direccion_y_Estrategia/Decisiones_y_Acuerdos/`.
3. Fallas y lecciones del ciclo registradas en `01_Direccion_y_Estrategia/Decisiones_y_Acuerdos/Matriz_de_Cambios_y_Acuerdos.md` o en `01_Direccion_y_Estrategia/Aprendizajes_y_Conocimiento/`.
================================================================================
```

---

## ⚙️ Guía de Uso para el Orquestador

1. **Cuándo emitir este prompt:** Ante cualquier tarea crítica: entregables finales, modelos financieros, análisis cuantitativos, balances de carga, hojas de cálculo, memorandos ejecutivos para comités o presentaciones institucionales (criterio de REGLAS #4).
2. **Cómo reportar al usuario:**
   * El Orquestador no muestra las quejas intermedias a menos que se active el *Circuit Breaker* (2 iteraciones fallidas).
   * Cuando el Revisor Adversarial emite el dictamen `✅ APROBADO`, el Orquestador entrega el artefacto final con el resumen de las pruebas en frío que superó.
