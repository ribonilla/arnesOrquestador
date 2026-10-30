# Propuesta de Mejora al Arnés Universal: Protocolo Mandatorio de Cardinalidad y Llaves Primarias para Tablas

> **Para:** Diseñador / Mantenedor del Arnés Universal (Decision & Deliverable Harness)  
> **De:** Director Estratégico & Chief of Staff (Antigravity AI)  
> **Fecha:** 2026-10-13 (Incorporado: 2026-10-14)  
> **Estado:** ✅ Aprobada e Incorporada en el Arnés (DEC-15)  
> **Módulo Impactado:** `.harness/REGLAS_OPERATIVAS_IA.md`, `.harness/Agentes/FLUJOGRAMA_ORQUESTADOR.md`, `AGENTS.md`, `GEMINI.md` y `.harness/tools/audit_table_cardinality.py`

---

## 1. Justificación y Contexto del Hallazgo (Caso de Estudio)

Durante la reconciliación multifuente de un caso financiero-académico de 4 tablas desconectadas (CRM con 5.200 registros y 4.200 personas únicas; Becas con 2.330 registros; ERP con 4.610 facturas; LMS con 2.327 matriculados), se evidenció un fallo estructural atribuible al comportamiento autónomo del modelo de lenguaje:

### El Síndrome de la "Inferencia Prematura de Entidad"
1. **La IA asumió una Primary Key simple incorrecta:** Al ver nombres de personas y números de identificación en las cuatro tablas, el modelo asumió que la entidad de análisis era el *Estudiante* (`doc` o `Cédula`), cuando en realidad la entidad atómica del negocio era la *Transacción de Postulación/Curso* (`ID_Inscripcion` o la tupla compuesta `Documento + Curso`).
2. **Impacto en los resultados:**
   * **Inflado de falsos positivos en Cobro Excesivo (195 vs 71 reales):** Un estudiante se postuló dos veces (una sin beca y otra con beca). Al cruzar por cédula simple, la factura plena se emparejó erróneamente con la beca del segundo intento.
   * **Pérdida de anomalías reales en Aula Sin Pago (7 vs 10 reales):** Estudiantes inscritos en múltiples cursos pagaron el Curso A pero ingresaron al aula del Curso B. Al cruzar por cédula simple, el sistema vio que la persona tenía "algún pago" en la institución y descartó la alerta.
   * **Descuentos no autorizados (106 vs 93 reales):** Duplicidad por homonimia de cédula en múltiples trámites.

---

## 2. Diagnóstico: El Vacío en el Arnés Actual

El arnés genérico actual posee excelentes directrices de:
* Formato de entregables (Word bimodal, PowerPoint $\ge$ 16pt, HTML interactivo).
* Verificación pasiva y activa de ejecución (validación sintáctica de scripts, fórmulas).

Sin embargo, **carece de un *Quality Gate* previo a la manipulación de datos tabulares**. Actualmente, el arnés permite que el agente comience a programar cruces (`pandas.merge`, `SQL JOIN`, `BUSCARV / XLOOKUP`) sin antes obligarlo a validar formalmente la estructura dimensional de las fuentes.

---

## 3. Especificación Técnica de la Mejora para el Arnés Genérico

Se propone incorporar en `.harness/REGLAS_OPERATIVAS_IA.md` una regla innegociable denominada:

```markdown
### 🛡️ PROTOCOLO MANDATORIO: AUDITORÍA DE CARDINALIDAD Y LLAVES PRIMARIAS (GATE 0 DE DATOS)
Antes de ejecutar cualquier unión, cruce, consolidación, fórmula o cálculo sobre dos o más tablas de datos (CSV, Excel, SQL, JSON), el agente TIENE PROHIBIDO escribir código de cruce hasta haber ejecutado y documentado el siguiente protocolo en una nota de sesión:
```

### Paso 1: Perfilamiento de Cardinalidad por Tabla
Para cada fuente involucrada en el problema, el agente debe inspeccionar y reportar:
* **Número total de filas ($N$).**
* **Candidatas a Clave Primaria (PK):** Verificar unicidad absoluta (`unique_count == N`).
  * Si ninguna columna simple es única, identificar la **Llave Compuesta Mínima** que garantice unicidad (ej. `(ID_Persona, ID_Item)`).
  * Reportar el porcentaje de duplicidad de las claves simples (ej. *"La cédula tiene 1.000 repeticiones ($N:M$)"*).

### Paso 2: Matriz de Relación y Cardinalidad entre Tablas
Antes de cualquier `JOIN` / `MERGE`, declarar formalmente el tipo de relación entre los pares de tablas:
* $1:1$ (Uno a Uno)
* $1:N$ (Uno a Muchos)
* $N:M$ (Muchos a Muchos)

> **Regla de Bloqueo del Arnés:** Si la relación es $1:N$ o $N:M$, el agente **no puede** realizar cruces basados en la clave del lado "Muchos" sin una regla de desambiguación explícita (ej. llave compuesta, agrupamiento previo o filtro temporal).

### Paso 3: Declaración Explícita de la Granularidad del Entregable
El agente debe contrastar la solicitud del usuario con la realidad de los datos:
* Si el usuario pide: *"Un listado de clientes/estudiantes"*, pero los datos revelan que la entidad atómica es transaccional (compras, inscripciones, contratos), el agente debe:
  1. Identificar si el entregable debe ser a nivel **Persona** (agregando métricas consolidadas) o a nivel **Transacción** (un registro por postulación/compra).
  2. Documentar la decisión en la nota de sesión antes de generar el archivo.

---

## 4. Hook de Automatización para el Arnés (`audit_table_cardinality.py`)

Para que el arnés no dependa únicamente de la buena voluntad del LLM, se propone añadir una herramienta genérica en `.harness/tools/audit_table_cardinality.py`.

### Script Propuesto:
```python
#!/usr/bin/env python3
"""
Harness Tool: Auditor de Cardinalidad y Llaves Primarias
Evalúa archivos de datos (CSV, XLSX) y detecta duplicidades, candidatas a PK y riesgos de cruce N:M.
"""
import sys
import pandas as pd

def audit_file(filepath, key_cols=None):
    if filepath.endswith('.csv'):
        df = pd.read_csv(filepath)
    else:
        df = pd.read_excel(filepath)
        
    total_rows = len(df)
    print(f"=== Auditoría de Fuente: {filepath} ({total_rows} filas) ===")
    
    # 1. Evaluar columnas individuales candidatas a PK
    pk_candidates = []
    for col in df.columns:
        n_unique = df[col].nunique()
        if n_unique == total_rows:
            pk_candidates.append(col)
        elif n_unique > total_rows * 0.7:
            print(f"  ⚠️ Columna '{col}' tiene {n_unique} valores únicos sobre {total_rows} filas ({total_rows - n_unique} duplicados). NO es PK simple.")
            
    if pk_candidates:
        print(f"  ✅ Candidatas a Llave Primaria Simple: {pk_candidates}")
    else:
        print("  🚨 ALERTA: No existe Llave Primaria simple. Requiere Llave Compuesta.")
        
    # 2. Evaluar llave compuesta si fue provista
    if key_cols:
        keys = [k.strip() for k in key_cols.split(',')]
        comp_unique = df.duplicated(subset=keys).sum()
        if comp_unique == 0:
            print(f"  ✅ Llave Compuesta {keys} es 100% ÚNICA.")
        else:
            print(f"  ❌ Llave Compuesta {keys} tiene {comp_unique} duplicados.")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python audit_table_cardinality.py <archivo> [col1,col2]")
        sys.exit(1)
    audit_file(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
```

---

## 5. Beneficios para Futuras Implementaciones del Arnés

1. **A prueba de sesgos del modelo:** Obliga a cualquier agente que opere dentro del arnés a realizar un diagnóstico relacional riguroso antes de procesar tablas.
2. **Independiente de la industria:** Funciona exactamente igual para bancos (cuentas vs transacciones), retail (clientes vs tickets de compra), salud (pacientes vs citas médicas) o educación (estudiantes vs asignaturas).
3. **Cero fricción con el usuario de negocio:** Evita que el usuario tenga que dar especificaciones matemáticas o de bases de datos relacionales; el arnés se encarga de proteger la integridad del dato de oficio.

---

> 📌 **Ubicación:** Esta propuesta queda archivada en `01_Direccion_y_Estrategia/Aprendizajes/PROPUESTA_MEJORA_ARNES_CARDINALIDAD_Y_LLAVES.md` para ser incorporada al repositorio maestro del Arnés Universal.
