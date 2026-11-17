---
tipo: aprendizaje
fecha: 2026-11-17 18:49
tema: "El clasificador de permisos bloquea commit y push combinados"
tarea: TAR_07
estado: vigente
---

# Aprendizaje: el clasificador de permisos bloquea commit y push combinados

## Qué pasó
Un comando que combinaba `git commit` y `git push` fue bloqueado por el clasificador de permisos.

## Qué aprendimos
Separar los pasos funcionó: primero el commit, después el push, pidiendo aprobación explícita para este último. Al planear comandos de publicación, conviene dividirlos desde el inicio.
