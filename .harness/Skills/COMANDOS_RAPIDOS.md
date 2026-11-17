# GUÍA DE COMANDOS RÁPIDOS Y ATAJOS DEL ARNÉS

Puedes escribir estos comandos en tu chat con la IA (o pedírselos en lenguaje natural) para ejecutar acciones operativas instantáneas. Los comandos marcados como *propuesto* aún no están definidos en `.harness/REGLAS_OPERATIVAS_IA.md`.

---

### 1. `/iniciar` (Crear o Iniciar Proyecto)
* **Qué hace:** Diagnostica contexto $\to$ Diseña el Plan de Fases $\to$ Concierta contigo $\to$ Monta el Kanban (tablero de tareas por columnas) y el Dashboard (panel resumen) en Obsidian.
* **Ejemplo:** `/iniciar Expansión de Servicios de Consultoría B2B`

---

### 2. `/sesion` (Retomar Trabajo del Día)
* **Qué hace:** La IA lee el Kanban actual en `02_Ejecucion_y_Seguimiento/Kanban_y_Tareas/Tablero_Kanban.base`, resume el estado y arranca con la tarea en curso.
* **Ejemplo:** `/sesion`

---

### 3. `/decision` (Registrar Decisión / Cambio de Alcance)
* **Qué hace:** Registra de inmediato en `01_Direccion_y_Estrategia/Decisiones_y_Acuerdos/Matriz_de_Cambios_y_Acuerdos.md` qué se modificó, por qué se hizo y quién lo aprobó, con fecha y hora (`YYYY-MM-DD HH:MM`).
* **Ejemplo:** `/decision El sponsor pidió reducir el plazo a 4 semanas y recortar la fase de pruebas piloto.`

---

### 4. `/reporte-jefe` (Generar Resumen Ejecutivo para Reunión)
* **Qué hace:** Genera un informe ejecutivo de 3 párrafos y lo guarda en `03_Entregables_Finales/`.
* **Ejemplo:** `/reporte-jefe`

---

### 5. `/abogado-diablo` (Simular Objeciones de Comité)
* **Qué hace:** Invoca al modo *Abogado del Diablo* (un revisor que ataca tu propuesta para encontrar sus puntos débiles) para que cuestione tu propuesta actual, buscando huecos en los números, riesgos legales o preguntas difíciles de la junta directiva.
* **Ejemplo:** `/abogado-diablo Evaluemos la propuesta comercial antes de enviársela al cliente.`

---

### 6. `/auditar-vault` (Auditar la Bóveda)
* **Qué hace:** Activa el rol de Auditor de Bóveda (la bóveda es la carpeta de notas de Obsidian del proyecto). Rastrea sesiones, acuerdos y versiones para responder qué cambió, por qué y quién lo pidió, citando notas exactas.
* **Ejemplo:** `/auditar-vault ¿Por qué cambió la cifra del presupuesto?`

---

### 7. `/informe-acuerdos` (Informe Formal de Acuerdos)
* **Qué hace:** Genera un documento formal con el historial de acuerdos y lo guarda en `01_Direccion_y_Estrategia/Decisiones_y_Acuerdos/Informe_de_Acuerdos_YYYY-MM-DD.md`.
* **Ejemplo:** `/informe-acuerdos`

---

### 8. `/gauntlet` (Blindaje Adversarial de Entregable Crítico) *(propuesto)*
* **Qué hace:** Activa manualmente la compuerta Gauntlet (una revisión adversarial que mide el entregable contra un listón observable, con entre 2 y 4 rondas de corrección).
* **Ejemplo:** `/gauntlet Audita la propuesta económica y el modelo financiero para detectar discrepancias antes de la firma.`

---

### 9. `/experto [Dominio]` (Invocar Mentor Temático con Professor Synapse) *(propuesto)*
* **Qué hace:** Professor Synapse (el mentor metodológico del arnés) convoca a un especialista de dominio a medida para debatir y co-diseñar el contenido de fondo paso a paso.
* **Ejemplo:** `/experto Especialista en Ciberseguridad ISO 27001 para auditar nuestras políticas de acceso remoto.`

---

### 10. `/capitalizar` (Guardar Aprendizaje Zettelkasten) *(propuesto)*
* **Qué hace:** Extrae un aprendizaje metodológico, criterio corporativo validado o plantilla útil (Zettelkasten es un sistema de notas atómicas enlazadas) y crea una nota atómica en `01_Direccion_y_Estrategia/Aprendizajes_y_Conocimiento/`.
* **Ejemplo:** `/capitalizar Principio: En B2B la venta se cierra con la reportería para el comprador, no con las funciones del usuario.`

---

### 11. `/guardar [sesion|decisiones|aprendizajes|tareas]` (Guardar en la Bóveda con Recibo)
* **Qué hace:** Guarda en la bóveda lo de la conversación (sesión, decisiones, aprendizajes, tareas y entregables) y entrega un recibo con cada archivo escrito, su acción y si quedó verificado. Sin ámbito, guarda todo. Procedimiento completo: `.harness/Skills/GUARDAR_BOVEDA.md`.
* **Ejemplo:** `/guardar decisiones`
