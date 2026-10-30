# Feature: Sello de Fecha y Hora en Anotaciones del Arnés

**Estado:** Completado (2026-10-20 20:27)
**Origen:** El usuario detectó que las decisiones y acuerdos solo registran fecha (no hora), lo que impide distinguir múltiples avances en un mismo día.
**Fuente de verdad:** raíz del repo (`.harness/`, `AGENTS.md`, `GEMINI.md`, `CLAUDE.md`, `01_Direccion_y_Estrategia/...`). `dist/` es una copia empaquetable que se re-sincroniza al final.

## Cambios
1. `REGLAS_OPERATIVAS_IA.md` — Regla de Oro #1: exigir fecha Y hora (`YYYY-MM-DD HH:MM`) en decisiones, acuerdos, sesiones (cuerpo) y aprendizajes.
2. Plantillas `TPL_03` (sesión), `TPL_04` (matriz), `TPL_06` (zettelkasten), `TPL_00` (centro de mando): reemplazar `{{FECHA_HOY}}` / `Fecha` por `{{FECHA_Y_HORA}}` / `Fecha y Hora`.
3. `AGENTS.md`, `GEMINI.md`, `CLAUDE.md` — bullet de trazabilidad con fecha+hora para decisiones/acuerdos/aprendizajes.
4. Matriz real `01_Direccion_y_Estrategia/Decisiones_y_Acuerdos/Matriz_de_Cambios_y_Acuerdos.md` — columna `Fecha y Hora`, nota de entradas legacy, y DEC-16 con sello real.
5. Re-sincronizar `dist/Starter_Kit_Arnes/` desde la raíz y regenerar `dist/Starter_Kit_Arnes_Universal.zip`.

## Convención de sello temporal
- Formato: `YYYY-MM-DD HH:MM`.
- Sesiones: `Sesion_YYYY-MM-DD_HHmm_Tema.md` (nombre de archivo) + misma fecha/hora en el cuerpo.
- Decisiones/acuerdos: columna `Fecha y Hora` en la matriz.
- Aprendizajes: `fecha_hora_creacion` en frontmatter.

## Verificación
- `grep` de `HH:MM` / `FECHA_Y_HORA` en plantillas y reglas.
- `diff` raíz vs dist (deben coincidir en los archivos editados).
- Integridad del zip (28 entradas esperadas).
