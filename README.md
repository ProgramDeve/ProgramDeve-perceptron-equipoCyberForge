## Integrantes

| Nombre | Código | Rol |
|---|---|---|
| Jorge Alvaro Turpo Chilo | 76147024 | Líder |
| Juan Gustavo Segura Villegas | (código) | Desarrollador |
| Katsumi Albert Mamani Corrales | 74842690 | Desarrollador |
| Emanuel Paz Mottoccanchi | (código) | Desarrollador |

## Resultados

Métricas de los 3 modelos sobre datos/pacientes.csv:

| Modelo | Accuracy | Error | Matriz de confusión |
|---|---|---|---|
| Modelo 1 (tasa 0.01) | 0.867 | 0.133 | [[34, 4], [11, 64]] |
| Modelo 2 (tasa 0.5, decaimiento 0.1) | 0.876 | 0.124 | [[37, 1], [13, 62]] |
| Modelo 3 (features: concavidad, puntos_concavos, area, textura) | 0.92 | 0.08 | [[35, 3], [6, 69]] |

### Análisis

**1. ¿Por qué los Modelos 1 y 2 daban igual antes de la Tarea 4, si sus tasas eran distintas?**

Porque el Perceptrón clásico converge a la misma frontera de decisión si los datos son linealmente separables, sin importar la tasa de aprendizaje (mientras sea positiva). La tasa solo afecta la velocidad de convergencia, no el resultado final. Al agregar el decaimiento, la tasa efectiva cambia a lo largo de las épocas y el modelo llega a una solución distinta.

**2. ¿Qué cambió con las features del Modelo 3 y por qué?**

El Modelo 3 usa features más informativas para este problema: concavidad, puntos_concavos, area y textura. Estas variables separan mejor las clases (maligno vs benigno) porque describen la irregularidad del contorno del tumor. El accuracy sube de 0.876 a 0.92.

**3. Los errores por época nunca llegan a 0: ¿qué dice eso sobre si los datos son linealmente separables?**

Que los datos NO son perfectamente separables linealmente. El Perceptrón solo garantiza convergencia cuando los datos son separables linealmente. Como los errores oscilan sin llegar a 0, hay puntos mal clasificados que ninguna recta puede separar de forma perfecta.

**4. En este problema, ¿qué error es más grave, un falso positivo o un falso negativo?**

Un **falso negativo** es más grave. Un falso negativo significa clasificar un tumor maligno como benigno (o al revés, según la codificación), lo que llevaría a no tratar a un paciente enfermo. Un falso positivo solo implicaría pruebas adicionales. En salud, siempre se prioriza minimizar los falsos negativos.