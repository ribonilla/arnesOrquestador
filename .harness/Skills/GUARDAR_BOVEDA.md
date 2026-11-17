# Procedimiento: /guardar (persistir la conversación en la bóveda)

> Es un procedimiento en texto, no una skill instalable. Cualquier motor (Claude, Gemini, Codex, Pi, OpenCode) lo sigue leyendo este archivo.

## Cuándo se ejecuta

- Al escribir `/guardar`, con o sin ámbito: `/guardar sesion|decisiones|aprendizajes|tareas`.
- Al cerrar un tema de trabajo.
- Antes de cerrar la sesión.

Sin ámbito, ejecuta los pasos a, b, c, d, e y f. Con ámbito, ejecuta solo el paso del ámbito (`sesion` = a, `decisiones` = b, `aprendizajes` = c, `tareas` = d) y el paso f.

## Antes de escribir

Si no existe `00_Centro_de_Mando.md` en la raíz del proyecto, o faltan las carpetas `01_Direccion_y_Estrategia/`, `02_Ejecucion_y_Seguimiento/` o `03_Entregables_Finales/`, **no crees nada**. Indica que falta el bootstrap (`.harness/REGLAS_OPERATIVAS_IA.md`, paso 1) y detente.

## Pasos, en orden

**a. Nota de sesión.** Ruta: `02_Ejecucion_y_Seguimiento/Sesiones_y_Borradores/Sesion_YYYY-MM-DD_HHmm_Tema.md`, a partir de `.harness/Plantillas/TPL_03_Nota_Sesion_Ideacion.md`. Si ya guardaste una sesión en esta conversación, **actualízala** en la misma ruta; no crees otra. La fecha y hora del nombre se repiten en el cuerpo.

**b. Decisiones.** Añade filas nuevas en `01_Direccion_y_Estrategia/Decisiones_y_Acuerdos/Matriz_de_Cambios_y_Acuerdos.md` (si no existe, créala desde `.harness/Plantillas/TPL_04_Matriz_de_Cambios_y_Acuerdos.md`). Cada fila lleva sello `YYYY-MM-DD HH:MM` y el ID `DEC-NN` con NN = último número + 1. Para saber el último, ejecuta `rg -o "DEC-\d+" <ruta de la matriz>`; si no hay ninguno, usa `DEC-01`. No reescribas filas existentes: un cambio nuevo es una fila nueva. Si la plantilla trae la fila de ejemplo `DEC-01` y no corresponde a un acuerdo real, reemplázala por tus filas.

**c. Aprendizajes.** Una nota atómica por aprendizaje, a partir de `.harness/Plantillas/TPL_06_Nota_Zettelkasten.md`. Ruta: `01_Direccion_y_Estrategia/Aprendizajes_y_Conocimiento/Aprendizaje_YYYY-MM-DD_HHmm_Tema.md`. La plantilla no trae el frontmatter estándar: antepón el bloque de la sección "Frontmatter" de `GUIA_ESTRUCTURA_BOVEDA.md`.

**d. Tareas.** Si hubo tareas nuevas o cambios de estado, crea o actualiza `02_Ejecucion_y_Seguimiento/Kanban_y_Tareas/Tareas/TAR_XX_Nombre.md` y `02_Ejecucion_y_Seguimiento/Kanban_y_Tareas/Tablero_Kanban.base`.

**e. Entregables.** Para cada `.docx` en la raíz de `03_Entregables_Finales/`, comprueba que existe su gemelo `.md` con el mismo nombre base (`fd -e docx -d 1 . 03_Entregables_Finales`). Si falta, créalo como copia exacta. Si no puedes, decláralo como pendiente en el recibo.

**f. Dónde quedé.** Actualiza la sección "🧭 Dónde quedé" de `00_Centro_de_Mando.md` (última sesión, última decisión, tarea en curso, último entregable) y su campo `ultimo_repaso`.

## Frontmatter estándar

Toda nota nueva o actualizada lleva estos cinco campos, con el formato de `GUIA_ESTRUCTURA_BOVEDA.md`:

```yaml
---
tipo: sesion
fecha: "2026-11-17 10:30"
tema: "Revisión del flujo de aprobación"
tarea: TAR_03
estado: cerrado
---
```

`estado` es `cerrado` si la nota está completa, `borrador` si quedó parcial y `pendiente` si falta un dato.

## Recibo (obligatorio)

Al terminar, entrega el recibo con esta tabla, con una fila por cada archivo escrito (ruta relativa a la raíz del proyecto):

| Archivo | Acción (creado/actualizado) | Verificado (sí/no) |
|---|---|---|
| `02_Ejecucion_y_Seguimiento/Sesiones_y_Borradores/Sesion_2026-11-17_1030_Tema.md` | creado | sí |

Reglas del recibo:

1. **Verificado = sí** solo si, al leer el archivo de vuelta, existe y tiene el frontmatter estándar (`tipo`, `fecha`, `tema`, `tarea`, `estado`). La matriz de decisiones no tiene frontmatter: en su caso verifica que la fila nueva existe con su `DEC-NN` y su sello.
2. **Lo que no se guardó** va debajo de la tabla, con su causa. Si no hay nada pendiente, escribe "Nada pendiente".
3. **Un fallo no se oculta.** Va en la tabla con "no" y la causa.

## Límite honesto

El agente escribe a partir de lo que tiene en el contexto. En conversaciones largas, lo más antiguo puede estar resumido o perdido. Si el recibo no cubre algo que se habló al inicio, dilo. Por eso conviene ejecutar `/guardar` al cerrar cada tema y antes de cerrar la sesión.
