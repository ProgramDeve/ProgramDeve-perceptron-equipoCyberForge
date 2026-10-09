# Changelog

Formato: cada versión lista lo que se agregó (`Agregado`), lo que se corrigió (`Corregido`) y lo que cambió (`Cambiado`).

## [0.9.1] - 2026-10-09

### Corregido
- Se evita la división entre cero en `estandarizar()` cuando la desviación estándar es 0 (caso `hospital_b.csv`, columna `textura`).
- El Modelo 1 ahora obtiene 0.917 de accuracy con `hospital_b.csv` (antes bajaba a 0.417 por los valores `nan`).

## [0.9.0]

### Agregado
- Carga, limpieza, estandarización y división de los datos.
- Perceptrón simple con entrenamiento por épocas.
- Modelos 1 y 2 en `main.py`, evaluados con accuracy.