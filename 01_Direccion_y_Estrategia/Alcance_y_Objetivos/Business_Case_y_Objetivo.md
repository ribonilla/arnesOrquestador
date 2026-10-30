# 🏛️ Business Case y Fundamentos Estratégicos del Arnés

**Proyecto:** Construcción del Arnés de Gestión de Decisiones y Entregables con IA  
**Sponsor:** Ricardo Bonilla  
**Fecha:** 2026-10-08

---

## 1. El Mandato y Problema a Resolver

En la interacción diaria de profesionales corporativos y académicos con herramientas de IA generativa se presentan 3 problemas críticos:

1. **Amnesia Operativa y Dispersión:** Cada chat de IA empieza desde cero. No hay continuidad entre sesiones de trabajo complejas ni registro de los acuerdos previos.
2. **Falta de Trazabilidad y Riesgo ante Auditorías:** Cuando la IA propone cambios a textos o números, el colaborador no tiene un registro estructurado del *por qué* se tomó la decisión, exponiéndose ante jefes, comités o auditorías.
3. **Fricción Técnica y Sobrecarga Cognitiva:** Los entornos complejos con scripts o excesivas carpetas confunden al usuario no técnico. Se requiere un sistema que funcione con solo copiar y pegar, manteniendo el orden de forma autónoma.

---

## 2. Propuesta de Valor y Solución

Construir un **Arnés Operativo Universal (PARA + Zettelkasten + IA)** que actúe como un **Chief of Staff / Director Estratégico** con un staff de agentes especializados:

* **Arquitectura Zero-Lock-in:** 100% Markdown nativo, ejecutable en cualquier agente CLI (Gemini, Claude, Pi, Antigravity) o chats Web.
* **Auto-Escritura Proactiva:** La IA escribe automáticamente los avances, el Kanban y las decisiones en la bóveda sin que el usuario tenga que ordenarlo.
* **Staff de Especialistas Invocables:** Orquestador PM, Arquitecto de Bóveda, Controller Kanban, Auditor Financiero, Diseñador Word, Diseñador Visual PPTX, Storyteller Web y Abogado del Diablo.

---

## 3. Delimitación del Alcance (Scope)

### ✅ Dentro del Alcance
* Motor técnico aislado en `.harness/`.
* Estructura funcional de carpetas (`00_Centro_de_Mando.md` a `06_Zettelkasten_Conocimiento/`).
* Plantillas maestras de inicio, sesiones, decisiones y notas atómicas.
* Protocolos de auto-bootstrap para activación inmediata.
* Catálogo formal de Staff de Agentes y Skills.

### ❌ Fuera del Alcance
* Runtimes obligatorios pesados (Node.js/Python) que impidan la portabilidad en usuarios de oficina.
* Modificación invasiva de archivos personales de usuario (Word, Excel) fuera de la bóveda de trabajo.
