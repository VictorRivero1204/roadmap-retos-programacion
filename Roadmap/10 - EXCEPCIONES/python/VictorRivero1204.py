"""
Ejercicio
"""

try:
    print(10/1)
    print([1, 2, 3, 4][4])
except Exception as e:
    print(f"Se ha producido un error: {e} {type(e).__name__}")

"""
Extra
"""

class StrTypError(Exception):
    pass

def process_params(parameters: list):

    if len(parameters) < 3:
        raise IndexError()
    elif parameters[1] == 0:
        raise ZeroDivisionError()
    elif type(parameters[2]) == str:
        raise StrTypError("El tercer elemento no puede ser una cadena de texto")

    print(parameters[2])
    print(parameters[0]/parameters[1])
    print(parameters[2] + 5)

try:
    process_params([1, 2, 3, 4])
except IndexError as e:
    print("El numero de elementos de la lista no puede ser mayor de dos.")
except ZeroDivisionError as e:
    print("El segundo elemento de la lista no puede ser un cero.")
except StrTypError as e:
    print(f"{e}")
except Exception as e:
    print(f"Se ha producido un error inesperado: {e}")
else:
    print("No se han producido errores.")
finally:
    print("El programa finaliza sin detenerse")