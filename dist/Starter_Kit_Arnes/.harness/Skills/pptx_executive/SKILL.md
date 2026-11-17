# 🎨 SKILL: GENERACIÓN Y EDICIÓN PROFESIONAL DE PRESENTACIONES PPTX

Esta skill dota al **Especialista en Diseño Visual & PPTX** de los estándares y reglas técnicas para crear presentaciones ejecutivas `.pptx` sin errores de formato ni corrupción de archivos.

---

## 📌 1. Principios de Diseño Ejecutivo para Diapositivas

1. **Títulos de Acción (Action Titles):** Cada diapositiva debe tener un título que enuncie una conclusión o mensaje clave, no una simple etiqueta (ej. *"El canal B2B reduce el CAC en un 35%"* en lugar de *"Análisis de Canales"*).
2. **Jerarquía Visual y Densidad Controlada:** Máximo 1 idea principal por slide, apoyada por 3 bloques o tarjetas visuales.
3. **Notas de Oratoria (Speaker Notes):** Cada diapositiva debe incluir notas para el expositor con el guion verbal, datos de soporte y respuestas a posibles preguntas de la audiencia.

---

## 🛠️ 2. Reglas Técnicas de Generación (.pptx / pptxgenjs / python-pptx)

* **Relación de Aspecto:** Siempre usar formato panorámico `16:9` (`LAYOUT_16x9` = 10" × 5.625" o `LAYOUT_WIDE` = 13.3" × 7.5").
* **Colores Hexadecimales:** En bibliotecas de generación directa, los colores hex van sin `#` ni canal alfa de 8 dígitos (ej. `color: "1E293B"`).
* **Gráficos Nativos:** Priorizar gráficos nativos de PowerPoint (`addChart`) sobre capturas de imagen estáticas para permitir que el usuario edite los datos en Excel/PowerPoint.
* **Manejo de Viñetas y Listas:** Usar espaciado de párrafo (`paraSpaceAfter`) en lugar de saltos de línea dobles para evitar huecos antiestéticos.
* **Notas del Expositor:** Insertar como metadato nativo de notas (`slide.addNotes("...")`), nunca como cuadros de texto flotantes dentro de la diapositiva.

---

## 📋 3. Plantilla Markdown de Entrega Previa (Estructura de Deck)

Cuando el usuario solicite una presentación antes de compilar el `.pptx`, entregar el guion en este formato dentro de `05_Entregables/`:

```markdown
# 📊 [Título del Deck / Presentación]

---

### Diapositiva 1: Portada
* **Título:** [Título Ejecutivo de Alto Impacto]
* **Subtítulo:** [Propósito y Audiencia]
* **Speaker Notes:** "Buenos días comité, hoy presentamos..."

---

### Diapositiva 2: Situación y Oportunidad
* **Título de Acción:** [Mensaje principal contundente]
* **Estructura Visual:** 3 Columnas (Problema actual | Costo de no actuar | Oportunidad)
* **Datos Clave:** [Cifras destacadas]
* **Speaker Notes:** "Como pueden observar en la columna izquierda..."
```
