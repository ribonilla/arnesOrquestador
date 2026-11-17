---
name: web_storytelling
description: "Generación de presentaciones y reportes interactivos en formato One-Pager / Slide Deck HTML responsive con animaciones sutiles, métricas destacadas y diseño premium."
---

# 🌐 SKILL: PRESENTACIONES Y REPORTES INTERACTIVOS EN HTML

Esta skill dota al **Especialista en Storytelling Web** de los estándares y plantillas para maquetar reportes ejecutivos interactivos en formato web (`.html`) listos para compartir o proyectar en comités y reuniones de alta dirección.

---

## 📌 Principios de Diseño y Estándares Obligatorios

1. **Tema Claro por Defecto (Light Theme by Default):**
   * Por defecto, toda presentación o reporte HTML generado debe utilizar una paleta corporativa clara:
     - Fondo principal claro: `#F8FAFC` o `#FFFFFF`.
     - Tarjetas y contenedores: `#FFFFFF` con bordes sutiles `#E2E8F0` y sombras suaves.
     - Texto de alto contraste: `#0F172A` o `#1E293B` para lectura diáfana.
   * Si la interfaz incluye alternador (*theme toggle*), el tema por defecto al cargar siempre debe ser claro, permitiendo cambiar a modo oscuro únicamente si el usuario lo desea.

2. **Tipografía Grande y Legible (Piso Tipográfico Cómodo):**
   * **Cero necesidad de zoom excesivo:** La presentación debe poder leerse sin esfuerzo desde proyectores o monitores corporativos.
   * **Escala Tipográfica Recomendada:**
     - Título principal (`h1` / Portada): `2.5rem` a `3.2rem` (40px a 52px).
     - Subtítulos de sección (`h2`): `1.75rem` a `2.25rem` (28px a 36px).
     - Encabezados de tarjetas (`h3`): `1.25rem` a `1.5rem` (20px a 24px).
     - **Texto de cuerpo y párrafos (`p`, `li`):** Mínimo **`1.125rem` a `1.2rem` (18px a 19px)** con `line-height: 1.6` a `1.7`.
     - Números y KPIs destacados: `2.5rem` a `3.5rem` (40px a 56px) en peso *bold/extrabold*.
     - Notas al pie / metadatos mínimos: Mínimo `0.95rem` (15px) (nunca microletras ilegibles).

3. **Diseño Responsive y Viewport 16:9:**
   * Adaptable tanto a pantallas panorámicas (16:9) como a tabletas y dispositivos móviles.
   * Navegación asistida por teclado (flechas $\leftarrow$ / $\rightarrow$ o barra espaciadora) para transicionar entre diapositivas o bloques de contenido.

4. **Componentes Clave:**
   * Tarjetas de KPIs destacados con métricas directivas.
   * Bloques de comparación antes/después o escenarios.
   * Cronogramas interactivos y acordeones para desglosar detalles sin saturar la pantalla.
   * Descargo de responsabilidad / Aviso de Auditoría Humana al cierre.

5. **Cero Servidores (Zero-Server Architecture):**
   * Archivo único `.html` 100% autocontenido (HTML + CSS + JavaScript vanilla inline).
   * Se abre inmediatamente haciendo doble clic en Chrome, Edge, Safari o Firefox, sin requerir Node.js ni servidores locales.
