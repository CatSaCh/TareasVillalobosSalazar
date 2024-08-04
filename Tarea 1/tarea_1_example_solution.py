# Tarea 1
# Método operation_selector

def operation_selector(num1, num2, op):
    ERROR_INVALID_TYPE_NUM = -50
    ERROR_INVALID_TYPE_OP = -60
    ERROR_INVALID_OP = -70
# Se definen los códigos de error

# Verificar si num1 y num2 son enteros y que no sea un booleano
    if not (isinstance(num1, int) and isinstance(num2, int)):
        return (ERROR_INVALID_TYPE_NUM, None)
    if (isinstance(num1, bool) or isinstance(num2, bool)):
        return (ERROR_INVALID_TYPE_NUM, None)
# Verificar si op es un string
    if not isinstance(op, str):
        return (ERROR_INVALID_TYPE_OP, None)

# Verificar si op es uno de los caracteres válidos
    if op not in ('+', '-', '*', '&'):
        return (ERROR_INVALID_OP, None)

# Realizar la operación según el valor de op
    result = None
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '&':
        result = num1 & num2  # And lógico

    # Devolver el código de éxito y el resultado de la operación
    return (0, result)

# Ejemplos de uso
# print(operation_selector(5, 3, '+'))  # (0, 8)
# print(operation_selector(5, 3, '-'))  # (0, 2)
# print(operation_selector(5, 3, '*'))  # (0, 15)
# print(operation_selector(5, 3, '&'))  # (0, 1)
# print(operation_selector(5, '3', '+'))  # (1, None)
# print(operation_selector(5, 3, 'add'))  # (3, None)
# print(operation_selector(5, 3, 4))  # (2, None)

# Calculadora de promedio

# Funcion para calcular promedio


def calculo_promedio(lista_valores):
    suma = 0
# Para sumar elementos de la lista
# Verificar cantidad de elementos menor a 10
    if len(lista_valores) <= 10:
# Verificar que todos los elementos sean numeros
        for i in lista_valores:
            if (type(i) is int) or (type(i) is float):
                suma += i
            else:
                return -80, None
        return 0, suma/(len(lista_valores))
    else:
        return -90, None

# Ejemplo de prueba
# lista_valores=[10, 10, 10, 1, 1, 1, 1]
# estado, result = calculo_promedio(lista_valores)
