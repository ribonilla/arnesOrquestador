---
tipo: aprendizaje
fecha: 2026-11-17 16:38
tema: "Skills de terceros fuera del repositorio"
tarea: TAR_07
estado: vigente
---

# Aprendizaje: Skills de terceros fuera del repositorio

## Qué pasó
Las skills propias de `.harness/Skills/` (docx, pdf, pptx, xlsx, web) se retiraron de la plantilla. Los usuarios del arnés no son profesionales de IA, así que no deben depender de archivos de terceros copiados al repositorio.

## Qué aprendimos
Las skills de Anthropic para documentos son source-available, por lo que no se redistribuyen desde el repositorio. Se decidió el modo básico: el arnés funciona sin skills y su bootstrap revisa si faltan.

## Cómo aplicarlo
Para usuarios no técnicos, dar una guía de instalación con un comando por herramienta en lugar de versionar archivos de terceros en el repositorio.

## Enlaces
* Sesión: [[02_Ejecucion_y_Seguimiento/Sesiones_y_Borradores/Sesion_2026-11-17_1632_Plantilla_Limpia_y_Skills]]
* Decisión: DEC-30 en [[01_Direccion_y_Estrategia/Decisiones_y_Acuerdos/Matriz_de_Cambios_y_Acuerdos]]
* Retiros: [[01_Direccion_y_Estrategia/Decisiones_y_Acuerdos/Registro_de_Retiros_2026-11-17]]
