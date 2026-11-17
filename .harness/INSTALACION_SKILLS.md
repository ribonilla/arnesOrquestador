# Instalación de skills recomendadas

## ¿Qué son las skills?

Son paquetes de instrucciones que enseñan a la herramienta de IA a hacer tareas concretas, por ejemplo crear un Word o un Excel con buen formato. Se descargan desde catálogos públicos con un comando. Este arnés **no trae ni copia** estos archivos: la instalación la haces tú.

## ¿Funciona el arnés sin skills?

Sí, en **modo básico**:

- Documentos de Office y PDF: la IA escribe el contenido, pero sin formato automático. Hace falta más revisión manual.
- Obsidian: las notas se escriben en Markdown normal, sin los atajos del plugin.

Instalar las skills mejora el resultado, pero no es obligatorio.

## Paso 1: prerrequisitos

Necesitas **Node.js** (que incluye `npx`) y **Python**. Abre una terminal y sigue el sistema operativo que tengas.

**Windows (PowerShell):**

```powershell
winget install OpenJS.NodeJS.LTS
winget install Python.Python.3.12
```

Cierra la terminal y ábrela de nuevo.

**macOS:** primero instala Homebrew desde https://brew.sh y después:

```bash
brew install node python
```

*Esta parte no la probamos en macOS.*

Verifica que todo quedó instalado. Deben aparecer tres números de versión:

```bash
node -v
npx -v
python --version
```

Si alguno no aparece, repite su instalación antes de seguir.

## Paso 2: elige tu herramienta

Usa el identificador de la tabla en el comando del paso 3.

| Herramienta | Identificador (`-a`) | Estado de la prueba |
|---|---|---|
| Claude Code | `claude-code` | Instalación probada |
| OpenCode | `opencode` | Instalación probada |
| Antigravity (comando `agy`) | `antigravity` | Instalación probada |
| Gemini CLI | `gemini-cli` | Pendiente de probar |
| Codex | `codex` | Pendiente de probar |
| Pi | pendiente | Sin probar |

## Paso 3: instalar las skills

Abre la terminal **dentro de la carpeta de tu proyecto** y ejecuta los dos comandos, cambiando `TU-HERRAMIENTA` por el identificador del paso 2.

**Documentos Word, Excel, PowerPoint, PDF y diseño (recomendada):**

```bash
npx skills add anthropics/skills -a TU-HERRAMIENTA -s docx -s pdf -s pptx -s xlsx -s frontend-design --copy -y
```

**Obsidian (recomendada si usas una bóveda de Obsidian):**

```bash
npx skills add kepano/obsidian-skills -a TU-HERRAMIENTA -s obsidian-markdown --copy -y
```

Ejemplo para Antigravity:

```bash
npx skills add anthropics/skills -a antigravity -s docx -s pdf -s pptx -s xlsx -s frontend-design --copy -y
```

Las skills quedan dentro de tu carpeta de proyecto, no en el repositorio del arnés.

## Paso 4: verificar

```bash
npx skills list
```

Deben aparecer `docx`, `pdf`, `pptx`, `xlsx`, `frontend-design` y `obsidian-markdown`. Si alguna falta, repite su comando del paso 3.

## Avisos de seguridad

- Las skills **se ejecutan con los permisos completos de tu herramienta de IA**. Instala solo las de esta lista.
- Las skills de documentos de Anthropic tienen licencia "source-available": al instalarlas aceptas sus términos.
- Si un comando falla, usa la dirección completa del repositorio: https://github.com/anthropics/skills o https://github.com/kepano/obsidian-skills.

## Estado de la prueba

Probado en Windows con Node 22 y Python 3.12, en una carpeta temporal aislada:

- `npx skills add` con varios motores a la vez, usando `--copy`: funciona.
- OpenCode lista las skills instaladas en el proyecto.
- `npx skills list` muestra las skills instaladas.

Pendiente: uso real de las skills dentro de Antigravity, Gemini CLI, Codex y Pi, y prueba en macOS.
