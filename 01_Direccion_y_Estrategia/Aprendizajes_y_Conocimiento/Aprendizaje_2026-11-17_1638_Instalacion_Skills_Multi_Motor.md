---
tipo: aprendizaje
fecha: 2026-11-17 16:38
tema: "Instalación de skills para varios motores"
tarea: TAR_07
estado: vigente
---

# Aprendizaje: Instalación de skills para varios motores

## Qué pasó
Se probó `npx skills add <repo> -a <motor> --copy -y` en carpeta temporal con Claude Code, OpenCode y Antigravity (`agy`). Quedan pendientes Gemini CLI, Codex y Pi.

## Qué aprendimos
El comando deja las skills en `.agents/skills` (universal) y en `.claude/skills` (Claude Code). Aislar HOME no aísla OpenCode por completo: leyó skills globales del usuario, así que la prueba no es limpia.

## Cómo aplicarlo
Al probar la instalación de un motor, revisar sus skills globales antes de dar por buena la prueba. Usar el prompt de prueba en sandbox y verificar con `opencode debug skill` y `npx skills list`.

## Enlaces
* Sesión: [[02_Ejecucion_y_Seguimiento/Sesiones_y_Borradores/Sesion_2026-11-17_1632_Plantilla_Limpia_y_Skills]]
* Decisión: DEC-31 en [[01_Direccion_y_Estrategia/Decisiones_y_Acuerdos/Matriz_de_Cambios_y_Acuerdos]]
* Prompt: [[01_Direccion_y_Estrategia/Aprendizajes_y_Conocimiento/Prompts/PROMPT_03_Prueba_De_Instalacion_Skills]]
