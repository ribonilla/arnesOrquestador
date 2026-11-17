# 🔄 FLUJOGRAMA DE CICLO DE VIDA Y ORQUESTACIÓN (LIFECYCLE FLOWCHART)

Este documento describe la arquitectura de ejecución, el árbol de decisiones y el flujograma de pasos que rige al **Agente Orquestador (Director Estratégico & PM)** y a **Professor Synapse (Summoner de Expertos Temáticos)** a lo largo de toda la interacción con el usuario en la oficina.

La secuencia de pasos es la de [REGLAS_OPERATIVAS_IA.md](../REGLAS_OPERATIVAS_IA.md) (fuente de verdad). Este flujograma la sigue en el mismo orden.

---

## 🗺️ 1. Flujograma Completo de Interacción y Ciclo de Vida

```mermaid
flowchart TD
    Start([📥 Entrada del Usuario]) --> S1{"Paso 1 · Bootstrap<br/>¿Existe 00_Centro_de_Mando.md?"}

    %% PASO 2: DIAGNÓSTICO Y PLAN CONCERTADO
    S1 -- No --> S2["Paso 2 · Diagnóstico<br/>3 preguntas: sponsor, propósito, restricciones"]
    S2 --> Plan["Plan de fases concertado<br/>Setup de Kanban y 00_Centro_de_Mando"]
    Plan --> PlanWait[/¿Concertamos este plan?/]
    PlanWait -- Ajustes --> Plan
    PlanWait -- Sí --> S3
    S1 -- Sí --> S3

    %% PASO 3: PROFESSOR SYNAPSE
    S3["Paso 3 · Professor Synapse<br/>Diálogo socrático hasta definir qué quiere el usuario"]
    S3 -- Contenido aún no maduro --> S3
    S3 -- Contenido maduro --> S4

    %% PASO 4: CONTRATO DE LOGRO
    S4["Paso 4 · Contrato de Logro<br/>Synapse propone niveles; la persona elige<br/>Plantilla: TPL_07_Contrato_de_Logro"]
    S4 --> ScopeCheck{¿Entra en el alcance del proyecto?}
    ScopeCheck -- Desviación de alcance --> ScopeAlert[/Alerta de alcance: ¿ajustamos o descartamos?/]
    ScopeAlert --> S4
    ScopeCheck -- En alcance --> S5

    %% PASO 5: ESPECIALISTA DE DOMINIO
    S5["Paso 5 · Especialista de dominio construye<br/>Auditor Cuantitativo, Diseñador Documental, Especialista PPTX, Especialista HTML o Arquitecto Bóveda"]
    S5 --> CritFilter{¿Es tarea crítica?<br/>Entregable final, finanzas, alta dirección}
    CritFilter -- No, tarea rutinaria o borrador --> S7

    %% PASO 6: GAUNTLET
    CritFilter -- Sí --> S6["Paso 6 · Gauntlet<br/>Revisor Adversarial con el listón del nivel elegido"]
    S6 --> BenchCheck{¿Cumple el listón?<br/>Cero discrepancias numéricas y diseño directivo}
    BenchCheck -- Sí --> S7
    BenchCheck -- No, quedan rondas --> Fix[Reporte de defectos y subsanar en caliente] --> S6
    BenchCheck -- No, máximo de 4 rondas --> Escalation[/Escalar discrepancias al usuario y decidir/] --> S7

    %% PASO 7: PERSISTIR
    S7["Paso 7 · Persistir y /guardar<br/>Recibo de lo guardado; actualizar Kanban y 00_Centro_de_Mando"]

    %% PASO 8: APRENDIZAJE
    S7 --> S8["Paso 8 · Aprendizaje<br/>Nota atómica si hay lección, regla o patrón"]
    S8 --> Cierre([Sintetizar resultado y esperar siguiente turno])
```

---

## 📋 2. Detalle por paso (fases A-F mapeadas a la secuencia)

### Fase A: Entrada y Diagnóstico (pasos 1 y 2)
1. **Verificación de Bóveda (paso 1):** Determina si `00_Centro_de_Mando.md` existe y tiene un plan concertado.
2. **Entrevista Diagnóstica (paso 2):** Si el proyecto no está configurado, formula de inmediato las **3 preguntas innegociables**:
   * *Sponsor y Audiencia:* ¿Quién rinde cuentas y ante quién?
   * *Propósito de Negocio:* ¿Qué decisión detona este trabajo?
   * *Restricciones Duras:* Plazos y límites presupuestarios.
3. **Plan Concertado (después del paso 2):** Propone las fases y tareas atómicas. No ejecuta código ni contenido hasta contar con la venia del usuario.

### Fase B: Professor Synapse (paso 3)
1. Cuando la tarea exige conocimiento especializado de una industria o ciencia (ej. salud, ciberseguridad, derecho, finanzas avanzadas, educación):
   * **Professor Synapse** convoca al **Experto de Dominio Dinámico** con la plantilla de 3 pasos e inicia la co-creación socrática.
   * La síntesis del debate se guarda automáticamente en `02_Ejecucion_y_Seguimiento/Sesiones_y_Borradores/`.

### Fase C: Contrato de Logro, control de alcance y enrutamiento (pasos 4 y 5)
1. **Contrato de Logro (paso 4):** Synapse propone los niveles y la persona elige el de "listo"; el nivel se guarda en la tarea. Plantilla: `TPL_07_Contrato_de_Logro.md`.
2. **Verificación contra Restricciones:** Valida que cada nueva instrucción no rompa los límites de `01_Direccion_y_Estrategia/Alcance_y_Objetivos/Business_Case_y_Objetivo.md`.
3. **Selección del Especialista de Formato (paso 5):** Delega la construcción del archivo a Word, Excel, PPTX o HTML.

### Fase D: Compuerta de Aseguramiento de Calidad (paso 6)
1. **Evaluación de Criticidad:** Clasifica la tarea como rutinaria o crítica.
2. **Si involucra manipulación de tablas (Excel/CSV/DB):**
   * Aplica obligatoriamente el **Gate 0 de Datos** (perfilamiento de cardinalidad, detección de PK simple o compuesta, declaración de relación $1:1$, $1:N$ o $N:M$, y alineación de granularidad) antes de formular o cruzar datos.
3. **Si es crítica:**
   * Invoca al **Constructor (Builder)** y al **Revisor Adversarial (Adversarial Auditor)** mediante la plantilla formal de 4 bloques (`[.harness/templates/PLANTILLA_GAUNTLET_PROMPT.md](../templates/PLANTILLA_GAUNTLET_PROMPT.md)`).
   * El listón es el del nivel elegido en el Contrato de Logro (paso 4).
   * Aplica auditoría activa en frío (scripts Python) antes de aprobar.
   * **Bucle controlado:** Entre 2 y 4 iteraciones internas de corrección (mínimo 2, máximo 4). Si persiste el desacuerdo, activa el *Circuit Breaker* y presenta el conflicto al usuario.

### Fase E: Auto-Escritura y Persistencia en Bóveda (paso 7)
1. **Entregables:** Guarda los productos terminados en `03_Entregables_Finales/`. La versión previa se archiva en `Historico/` con diffs en rojo.
2. **Trazabilidad:** Cualquier cambio de números, alcance o redacción relevante se asienta en `01_Direccion_y_Estrategia/Decisiones_y_Acuerdos/Matriz_de_Cambios_y_Acuerdos.md`.
3. **Sincronización Kanban:** Actualiza la nota individual de la tarea en `02_Ejecucion_y_Seguimiento/Kanban_y_Tareas/Tareas/TAR_XX.md` y refresca `00_Centro_de_Mando.md`.

### Fase F: Capitalización Zettelkasten (paso 8)
1. Si durante la tarea se descubrió un patrón de diseño, error recurrente, preferencia corporativa o lección de negocio, crea una nota atómica en `01_Direccion_y_Estrategia/Aprendizajes_y_Conocimiento/`.
2. Cierra el turno entregando al usuario una síntesis ejecutiva: qué se logró, qué se guardó en la bóveda y cuál es la siguiente tarea del Kanban.
