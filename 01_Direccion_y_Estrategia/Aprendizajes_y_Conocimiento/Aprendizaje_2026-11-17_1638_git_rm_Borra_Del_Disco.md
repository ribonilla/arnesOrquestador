---
tipo: aprendizaje
fecha: 2026-11-17 16:38
tema: "git rm borra también del disco"
tarea: TAR_07
estado: vigente
---

# Aprendizaje: `git rm` borra también del disco

## Qué pasó
Al retirar archivos de la plantilla con `git rm` (commit `a91aec3`), también se borraron del disco `dist/` y los entregables del curso. Se perdió el acceso local a esos archivos hasta restaurarlos desde main en el commit `a183958`.

## Qué aprendimos
`git rm` elimina el archivo del disco además de dejar de rastrearlo. Para solo dejar de versionar un archivo y conservarlo en disco, usar `git rm --cached`.

## Cómo aplicarlo
Antes de retirar archivos de la plantilla, decidir si deben quedar en disco. Si deben conservarse, usar `git rm --cached` y revisar el resultado con `git status`.

## Enlaces
* Sesión: [[02_Ejecucion_y_Seguimiento/Sesiones_y_Borradores/Sesion_2026-11-17_1632_Plantilla_Limpia_y_Skills]]
* Decisión: DEC-28 en [[01_Direccion_y_Estrategia/Decisiones_y_Acuerdos/Matriz_de_Cambios_y_Acuerdos]]
* Retiros: [[01_Direccion_y_Estrategia/Decisiones_y_Acuerdos/Registro_de_Retiros_2026-11-17]]
