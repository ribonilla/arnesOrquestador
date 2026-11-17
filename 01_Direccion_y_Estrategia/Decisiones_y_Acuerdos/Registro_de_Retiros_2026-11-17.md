---
tipo: registro
fecha: 2026-11-17 16:38
tema: "Registro de retiros y restauraciones de la plantilla"
tarea: TAR_07
estado: vigente
---

# Registro de retiros y restauraciones (2026-11-17)

Comandos generales de recuperación desde la rama de la bóveda (`dev-vault`):
* Restaurar a la carpeta de trabajo: `git restore --source=dev-vault -- <ruta>`
* Ver el contenido sin restaurar: `git show dev-vault:<ruta>`

Decisiones relacionadas: DEC-28 (plantilla limpia), DEC-30 (sin skills de terceros), DEC-32 (bóveda en carpeta aparte), en [[01_Direccion_y_Estrategia/Decisiones_y_Acuerdos/Matriz_de_Cambios_y_Acuerdos]].

| Qué | Dónde estaba | Por qué | Estado | Cómo recuperarlo |
| --- | --- | --- | --- | --- |
| `00_Centro_de_Mando.md` | Raíz de la bóveda | Bóveda viva de la plantilla (DEC-28) | Retirado de la plantilla | `git show dev-vault:00_Centro_de_Mando.md` |
| `Business_Case_y_Objetivo.md` | `01_Direccion_y_Estrategia/Alcance_y_Objetivos/` | Bóveda viva de la plantilla (DEC-28) | Retirado de la plantilla | `git restore --source=dev-vault -- 01_Direccion_y_Estrategia/Alcance_y_Objetivos/Business_Case_y_Objetivo.md` |
| Lecciones, Mejoras, Principios, PROPUESTA y `PROMPT_01` de Aprendizajes | `01_Direccion_y_Estrategia/Aprendizajes_y_Conocimiento/` | Bóveda viva de la plantilla (DEC-28) | Retirado de la plantilla | `git restore --source=dev-vault -- 01_Direccion_y_Estrategia/Aprendizajes_y_Conocimiento/` |
| Matriz de decisiones | `01_Direccion_y_Estrategia/Decisiones_y_Acuerdos/` | Bóveda viva de la plantilla (DEC-28) | Retirado de la plantilla | `git restore --source=dev-vault -- 01_Direccion_y_Estrategia/Decisiones_y_Acuerdos/Matriz_de_Cambios_y_Acuerdos.md` |
| Kanban y `TAR_01` a `TAR_06` | `02_Ejecucion_y_Seguimiento/Kanban_y_Tareas/` | Bóveda viva de la plantilla (DEC-28) | Retirado de la plantilla | `git restore --source=dev-vault -- 02_Ejecucion_y_Seguimiento/Kanban_y_Tareas/` |
| Sesiones previas | `02_Ejecucion_y_Seguimiento/Sesiones_y_Borradores/` | Bóveda viva de la plantilla (DEC-28) | Retirado de la plantilla | `git restore --source=dev-vault -- 02_Ejecucion_y_Seguimiento/Sesiones_y_Borradores/` |
| Curso_Wiki (md y html) | `03_Entregables_Finales/` | Entregable del curso que el sitio de Netlify usa | Restaurado (commit `a183958`) | Ya en la plantilla. Respaldo: `git show dev-vault:03_Entregables_Finales/Curso_Wiki_Ejecutivo_Arnes_IA.md` |
| Flujograma de Ciclo de Vida | `03_Entregables_Finales/` | Entregable que el sitio de Netlify usa | Restaurado (commit `a183958`) | Ya en la plantilla. Respaldo: `git show dev-vault:03_Entregables_Finales/Flujograma_Orquestador_y_Ciclo_de_Vida.md` |
| Manual de Uso (html) | `03_Entregables_Finales/` | Entregable que el sitio de Netlify usa | Restaurado (commit `a183958`) | Ya en la plantilla. Respaldo: `git show dev-vault:03_Entregables_Finales/Manual_de_Uso_del_Arnes.html` |
| `odd/tasks/fecha-hora-anotaciones.md` | `odd/tasks/` | Tarea de desarrollo, no de la plantilla | Retirado de la plantilla | `git restore --source=dev-vault -- odd/tasks/fecha-hora-anotaciones.md` (solo existe en `dev-vault`) |
| `dist/Starter_Kit_Arnes/` (copia del kit) | `dist/` | Duplicado del kit, retirado del rastreo | Restaurado (commit `a183958`) para el sitio de Netlify | Ya en la plantilla. Los archivos sin rastrear `dist/Starter_Kit_Arnes/01_*`, `02_*` y `03_*` no están en git: no tienen recuperación por git |
| Skills propias `.harness/Skills/{docx,pdf,pptx,xlsx,web}` | `.harness/Skills/` | Archivos de terceros no redistribuibles (DEC-30) | Retirado de la plantilla (commit `d45bdad`) | `git restore --source=d45bdad^ -- .harness/Skills/<skill>` |
| `.obsidian/appearance.json` | `.obsidian/` | Revisiones repetidas del hook por un cambio sin valor para el arnés | Sin tocar en disco (solo dejó de rastrearse, commit `f2e3e83`) | El archivo local sigue en disco. Para volver a rastrearlo, quitar la regla de `.gitignore` y ejecutar `git add` |
| `.gitignore` | Raíz | Se agregaron reglas `*-ribonilla.*` y `.atl/` | Sin tocar (ningún archivo retirado) | `git show cf3ada1 -- .gitignore` muestra el cambio |

Ver también: [[01_Direccion_y_Estrategia/Aprendizajes_y_Conocimiento/README|Aprendizajes de la sesión]] y [[02_Ejecucion_y_Seguimiento/Sesiones_y_Borradores/Sesion_2026-11-17_1632_Plantilla_Limpia_y_Skills|Sesión 2026-11-17]].
