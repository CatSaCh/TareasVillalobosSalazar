# Trabajo extra clase semana 4
# Hacer un programa que genere la serie de Fibonacci
# hasta cierta cantidad de veces. Retorna una lista.


# Genera la serie de Fibonacci n veces
def fibonacci_series(n):
    series = []
    a, b = 0, 1
    while len(series) < n:
        series.append(a)
        a, b = b, a + b
    return series

# Ejemplo


n = 10
print("Los primeros", n, "números de la serie de Fibonacci son:",
      fibonacci_series(n))
