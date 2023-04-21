# ejemplo de definición de una función que permite sumar dos numero
def suma(a, b):
    return a + b

print(suma(9,3)) # imprime = 12


# función con múltiples parámetros con una sentencia de retorno
def multiplicacion(val1, val2,val3):
  return val1 * val2 * val3

print(multiplicacion(3, 5, 2))  # muestra 30 

def Intercambiar(mayor,menor):
    if mayor<menor:
        return menor,mayor
    else:
        return mayor,menor

#funcion recursiva que dado un número va imprimir hasta ese número
def cuenta_atras(num):
    num -= 1
    if num > 0:
        print(num)
        cuenta_atras(num)
    else:
        print("Boooooooom!")
    print("Fin de la función", num)

cuenta_atras(5)

# funcion recursiva para el factorial de un número
def factorial(num):
    print("Valor inicial ->",num)
    if num > 1:
        num = num * factorial(num -1)
    print("valor final ->",num)
    return num

print(factorial(5))
