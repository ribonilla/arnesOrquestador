# Instalación de skills recomendadas

## ¿Qué son las skills?

Las skills son paquetes de instrucciones que enseñan a la herramienta de IA a hacer tareas concretas, por ejemplo crear un Word o un Excel con buen formato. Se instalan desde catálogos oficiales. Este arnés **no trae ni copia** estos archivos.

## ¿Por qué el arnés funciona sin ellas?

Sin skills, el arnés funciona en **modo básico**:

- Documentos de Office y PDF: la IA escribe el contenido, pero sin el formato automático. Puede hacer falta más revisión manual.
- Obsidian: sin el plugin de Obsidian, las notas se escriben en Markdown normal.

Instalar las skills mejora el resultado, pero no es obligatorio para trabajar.

## Skills recomendadas

| Skill | Para qué sirve | Cómo instalar | Tipo |
|---|---|---|---|
| Documentos Word, Excel, PowerPoint y PDF | Crear y editar documentos de Office y PDF con formato profesional | `/plugin marketplace add anthropics/skills` y luego `/plugin install document-skills@anthropic-agent-skills` | Recomendada |
| Obsidian | Crear notas con el formato de Obsidian | `/plugin marketplace add kepano/obsidian-skills` y luego `/plugin install obsidian@obsidian-skills` | Recomendada si usan una bóveda de Obsidian |
| Diseño y HTML | Crear páginas y visuales con diseño cuidado | Escribir `/plugin`, elegir "Browse and install plugins" y buscar `frontend-design` | Opcional |

La instalación la hace la persona usuaria, escribiendo los comandos en el chat, uno por uno y en orden. El arnés no instala nada por su cuenta.

## Cómo verificar

Escribir `/plugin list`. Deben aparecer las skills instaladas. Si no aparecen, repetir la instalación de esa skill.

## Avisos

- Estas instrucciones se revisan antes de cada cambio grande. Si un comando falla, usar la dirección completa del repositorio: https://github.com/anthropics/skills o https://github.com/kepano/obsidian-skills.
- Licencia: las skills de documentos de Anthropic tienen licencia "source-available"; quien las instala acepta sus términos.
