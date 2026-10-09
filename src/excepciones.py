"""Excepciones personalizadas del proyecto."""


class DatosInvalidosError(Exception):
    """Se lanza cuando los datos de entrada no son válidos."""


class ModeloNoEntrenadoError(Exception):
    """Se lanza cuando se intenta predecir sin haber entrenado el modelo."""
