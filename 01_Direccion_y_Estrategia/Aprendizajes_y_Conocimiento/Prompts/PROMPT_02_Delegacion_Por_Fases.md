---
tipo: prompt
fecha: 2026-11-17 16:38
tema: "Patrón de prompt para delegar por fases"
tarea: TAR_07
estado: vigente
---

# Prompt 02: Delegación por fases

## Cuándo usarlo
Cuando un subagente escritor debe editar varios archivos y la decisión ya está tomada por el usuario.

## Por qué funciona
La sección "Decisión ya tomada" evita que el escritor reinterprete decisiones. La "Superficie permitida" deja fuera de alcance lo que no toca. Las tareas numeradas y la verificación con comandos hacen que el reporte se pueda comprobar, en lugar de aceptarse por confianza.

## Plantilla

```text
## Decisión ya tomada
{decisión aprobada por el usuario, con su identificador (p. ej. DEC-XX); no reabrirla}

## Superficie permitida
{rutas exactas o globs, uno por línea; cualquier otra ruta no se toca}

## Tareas
1. {tarea 1}
2. {tarea 2}

## Verificación
Ejecuta cada comando y reporta el resultado observado:
- {comando 1}: {resultado observado}

## Reporte corto
Máximo {N} líneas: archivos creados y editados, verificación, dudas.

## Key Learnings
1-5 aprendizajes factuales, o omitir el bloque si no hay ninguno.
```

## Enlaces
* Sesión: [[02_Ejecucion_y_Seguimiento/Sesiones_y_Borradores/Sesion_2026-11-17_1632_Plantilla_Limpia_y_Skills]]
* Aprendizaje de verificación: [[01_Direccion_y_Estrategia/Aprendizajes_y_Conocimiento/Aprendizaje_2026-11-17_1638_Verificar_Reportes_de_Subagentes]]
