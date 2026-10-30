# 💬 Banco de Prompts y Patrones de Interacción (Prompt Engineering Asistido)

Esta carpeta almacena registros atómicos que documentan **cómo formula el usuario sus instrucciones habitualmente**, cuál es la **versión optimizada (prompt de alto impacto)** recomendada, y **por qué** funciona mejor.

---

## 🎯 Propósito y Filosofía
El usuario no tiene por qué memorizar la arquitectura interna de la bóveda, ni saber qué script o carpeta debe invocarse. Sin embargo, una solicitud vaga (ej. *"guarda en la bóveda"*) produce resultados dispersos.

Cada nota en esta carpeta:
1. **Analiza el prompt natural del usuario:** Qué quiso decir en lenguaje cotidiano.
2. **Entrega la reformulación sugerida:** Un prompt enriquecido con contexto, rol, restricciones y formato de salida.
3. **Explica la ganancia de calidad:** Qué riesgos se mitigan y qué valor gana la interacción.
4. **Alimenta al arnés:** Le enseña al agente cómo interpretar intenciones cotidianas para actuar proactivamente con máximo detalle sin esperar a que el usuario conozca la fontanería interna.

---

## 📂 Formato Estándar de Nota de Prompt

Cada nota debe seguir la estructura:
- `Frontmatter YAML` con tipo `patron-prompt`, categoría, intención y etiquetas.
- **Contexto e Intención:** Qué necesita lograr el usuario en su flujo de trabajo.
- **Expresión Habitual (Entrada Cruda):** Cómo lo pide normalmente en el chat.
- **Formulación Sugerida de Alto Impacto:** Versión optimizada con estructura directiva.
- **Análisis de Valor Agregado:** Por qué la versión enriquecida genera mejores entregables.
- **Mapeo Automático del Arnés:** Qué acciones internas toma el agente ante esa instrucción.
