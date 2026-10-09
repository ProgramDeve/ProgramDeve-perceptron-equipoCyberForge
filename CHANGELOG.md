# Changelog

Formato: cada versión lista lo que se agregó (Agregado), lo que se corrigió (Corregido) y lo que cambió (Cambiado).

## [1.0.0] - 2026-10-09

### Agregado
Excepciones personalizadas: DatosInvalidosError y ModeloNoEntrenadoError.
Validaciones en cargar_datos, Perceptron.__init__ y Perceptron.predecir.
Métricas error_clasificacion y matriz_confusion.
Parámetro decaimiento en Perceptron (tasa adaptativa por época).
Modelo 3 con features configurables vía --features.

### Cambiado
main.py refactorizado: función evaluar_modelo y constante EPOCAS.
Estilo del código alineado a PEP 8 (flake8 sin errores).
Modelo 2 ahora usa tasa 0.5 con decaimiento 0.1 (accuracy pasa de 0.867 a 0.876).

### Corregido
División entre cero en estandarizar() (hospital_b.csv ya no produce nan).

## [0.9.1] - 2026-10-09

### Corregido
Se evita la división entre cero en estandarizar() cuando la desviación estándar es 0 (caso hospital_b.csv, columna textura).
El Modelo 1 ahora obtiene 0.917 de accuracy con hospital_b.csv (antes bajaba a 0.417 por los valores nan).

## [0.9.0]

### Agregado
Carga, limpieza, estandarización y división de los datos.
Perceptrón simple con entrenamiento por épocas.
Modelos 1 y 2 en main.py, evaluados con accuracy.