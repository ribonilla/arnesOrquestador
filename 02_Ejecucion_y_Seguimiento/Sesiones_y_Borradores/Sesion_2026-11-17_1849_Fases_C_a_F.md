---
tipo: sesion
fecha: 2026-11-17 18:49
tema: "Fases C a F de TAR_07: contrato de logro, Gauntlet, bootstrap, /guardar y licencia"
tarea: TAR_07
estado: vigente
---

# Sesión: Fases C a F de TAR_07

## Objetivo de la Sesión
Completar las fases C a F de [[02_Ejecucion_y_Seguimiento/Kanban_y_Tareas/Tareas/TAR_07_Plantilla_Limpia_y_Skills|TAR_07]] y dejar la bóveda lista para retomar.

## Trabajo Realizado
- **Contrato de Logro (Fase C):** niveles de logro y `TPL_07_Contrato_de_Logro.md`.
- **Gauntlet (Fase C):** entre 2 y 4 rondas, con Circuit Breaker tras la ronda 4. El nivel Óptimo también exige 2 rondas.
- **Bóveda navegable (Fase D):** bootstrap con esqueleto 01/02/03, plantillas sin prefijo TPL_ e índices con Bases y bloque "Dónde quedé".
- **Comando `/guardar` (Fase E):** procedimiento en `.harness/Skills/GUARDAR_BOVEDA.md` con recibo verificable.
- **Dependencias (Fase F):** `requirements.txt` con openpyxl, pandas y python-pptx; Python mínimo 3.12; licencia MIT.
- **Publicación:** push de `main` y zip de descarga actualizado.

## Decisiones
- [[01_Direccion_y_Estrategia/Decisiones_y_Acuerdos/Matriz_de_Cambios_y_Acuerdos|DEC-33]]: Gauntlet con 2 a 4 rondas.
- [[01_Direccion_y_Estrategia/Decisiones_y_Acuerdos/Matriz_de_Cambios_y_Acuerdos|DEC-34]]: nivel Óptimo con 2 rondas.
- [[01_Direccion_y_Estrategia/Decisiones_y_Acuerdos/Matriz_de_Cambios_y_Acuerdos|DEC-35]]: licencia MIT.
- [[01_Direccion_y_Estrategia/Decisiones_y_Acuerdos/Matriz_de_Cambios_y_Acuerdos|DEC-36]]: correo personal fuera de portada y pies públicos; titulares no verificables retirados.
- [[01_Direccion_y_Estrategia/Decisiones_y_Acuerdos/Matriz_de_Cambios_y_Acuerdos|DEC-37]]: bóveda de trabajo en `boveda/`, ignorada por git.
- [[01_Direccion_y_Estrategia/Decisiones_y_Acuerdos/Matriz_de_Cambios_y_Acuerdos|DEC-38]]: bootstrap con esqueleto y plantillas sin prefijo TPL_.
- [[01_Direccion_y_Estrategia/Decisiones_y_Acuerdos/Matriz_de_Cambios_y_Acuerdos|DEC-39]]: Python mínimo 3.12.
- [[01_Direccion_y_Estrategia/Decisiones_y_Acuerdos/Matriz_de_Cambios_y_Acuerdos|DEC-40]]: comando `/guardar` con recibo verificable.
- [[01_Direccion_y_Estrategia/Decisiones_y_Acuerdos/Matriz_de_Cambios_y_Acuerdos|DEC-41]]: dependencias en `requirements.txt`, sin instalación automática.

## Pendientes
- Pruebas de instalación de skills en Gemini CLI, Codex, Pi y macOS.
- Render visual de los Mermaid en Obsidian, confirmado por el usuario.
- Revisión de los criterios de Óptimo y Profesional de `TPL_07_Contrato_de_Logro.md`.

## Aviso
La página de Netlify debe volver a arrastrarse, porque `index.html` cambió. El zip local no necesita subirse.

---

Auditoría humana: verifica las cifras clave antes de tomar decisiones ejecutivas.
