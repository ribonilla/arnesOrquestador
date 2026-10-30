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
        n_unique = df[col].nunique(dropna=False)
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
        missing_keys = [k for k in keys if k not in df.columns]
        if missing_keys:
            print(f"  ❌ Error: Columnas no encontradas en el archivo: {missing_keys}")
            return
            
        comp_unique = df.duplicated(subset=keys).sum()
        if comp_unique == 0:
            print(f"  ✅ Llave Compuesta {keys} es 100% ÚNICA ({total_rows} filas únicas).")
        else:
            print(f"  ❌ Llave Compuesta {keys} tiene {comp_unique} duplicados sobre {total_rows} filas.")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python audit_table_cardinality.py <archivo> [col1,col2]")
        sys.exit(1)
    audit_file(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
