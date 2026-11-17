---
tipo: aprendizaje
fecha: 2026-11-17 16:38
tema: "La configuración local de Obsidian no se versiona"
tarea: TAR_07
estado: vigente
---

# Aprendizaje: La configuración local de Obsidian no se versiona

## Qué pasó
`.obsidian/appearance.json` provocó revisiones repetidas del hook de revisión, por un cambio sin valor para el arnés.

## Qué aprendimos
La configuración local de la bóveda no pertenece al repositorio. Se dejó de rastrear el archivo y se agregó a `.gitignore` (commit `f2e3e83` en el repo). El archivo local sigue en disco.

## Cómo aplicarlo
Antes de versionar archivos de configuración de un editor, preguntar si aportan valor al arnés. Si no lo aportan, excluirlos con `.gitignore`.

## Enlaces
* Sesión: [[02_Ejecucion_y_Seguimiento/Sesiones_y_Borradores/Sesion_2026-11-17_1632_Plantilla_Limpia_y_Skills]]
* Retiros: [[01_Direccion_y_Estrategia/Decisiones_y_Acuerdos/Registro_de_Retiros_2026-11-17]]
