---
tipo: prompt
fecha: 2026-11-17 16:38
tema: "Prueba de instalación de skills en sandbox"
tarea: TAR_07
estado: vigente
---

# Prompt 03: Prueba de instalación de skills en sandbox

## Cuándo usarlo
Para probar la instalación de skills de un motor sin ensuciar la configuración real del usuario.

## Por qué aislar
Aislar HOME no basta para OpenCode: leyó skills globales del usuario. Revisar las skills globales antes de dar por buena la prueba.

## Plantilla

```text
Prueba de instalación de skills en sandbox.

1. Crea una carpeta temporal vacía {carpeta_temporal}.
2. Apunta HOME y USERPROFILE a {carpeta_temporal} para esta sesión.
3. Lista las skills del repositorio sin instalar: npx skills add {repo} -l
4. Instala por motor, uno a la vez: npx skills add {repo} -a {motor} -s {skill} --copy -y
5. Verifica OpenCode: opencode debug skill
6. Verifica la instalación: npx skills list

Reporta por motor: comando exacto, resultado observado y rutas creadas.
Si OpenCode muestra skills fuera de {carpeta_temporal}, repórtalo como contaminación del sandbox.
No modifiques el repositorio ni la configuración real del usuario.
```

## Enlaces
* Sesión: [[02_Ejecucion_y_Seguimiento/Sesiones_y_Borradores/Sesion_2026-11-17_1632_Plantilla_Limpia_y_Skills]]
* Aprendizaje: [[01_Direccion_y_Estrategia/Aprendizajes_y_Conocimiento/Aprendizaje_2026-11-17_1638_Instalacion_Skills_Multi_Motor]]
* Decisión: DEC-31 en [[01_Direccion_y_Estrategia/Decisiones_y_Acuerdos/Matriz_de_Cambios_y_Acuerdos]]
