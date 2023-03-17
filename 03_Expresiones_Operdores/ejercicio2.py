#Expresiones y Operadores

#Operadores

# + Este es el operador de suma y realiza la funcion de adicionar un operando al otro.
a = 7 + 3
print(a)  # Resultado = 10
a = 5
b = 3
c = a + b
print(c)	# Resultado = 8
print(3+4) 	# Resultado = 7
# - Este es el operador de resta y realiza la funcion de sustentar un operando de otro.
a = 6 - 2
print(a)	# Resultado = 4
a = 5
b = 3
c = a - b	
print(c) 	# Resultado = 2
print(2-6)	# Resultado = -4

# * Este es el operador de multiplicación y realiza la función de aumentar un operando en función de otro operando.
a = 3 * 4
print(a)	# REsultado =12
a = 6
b = 3
c = a * b
print(c)	#Resultado = 18
print(5*7)	#Resultado = 35

# / Este es el operador de división y realiza la función de seccionar un operando en función de otro operando.
a = 6 / 2
print(a)	#Resultado = 3
a = 5
b = 3
c = a / b
print(c)	#Resultado = 1.6666666667
print(10/3)	#Resultado = 3.3333333335


# % Este es el operador de módulo y realiza la función de regresar el residuo de una división.
a = 8 % 4
print(a)	#Resultado = 0
a = 9
b = 2
c = a % b	#Resultado = 1
print(c)
print(6%3)	#Resultado = 0

# ** Este es el operador de exponencial y permite obtener la potencia de un operando en función de otro operando.
a = 3 ** 3
print(a) 	#Resultado = 27
a = 2
b = 4
c = a ** b
print(c)	#Resultado = 16
print(4**3)	#Resultado = 64

#expresiones relacionales
# < Este es el operador de menor que, y se utiliza en las expresiones relacionales para saber si un operando es menor a otro operando.
a = 3 < 3
print(a)	#Resultado = False	Type Bool
a = 2
b = 4
c = a < b
print(c)	#Resultado = True	Type Bool
print(4<3)	#Resultado = False	Type Bool


# > Este es el operador de mayor que, y se utiliza en las expresiones relacionales para saber si un operando es mayor a otro operando.
a = 4 > 2
print(a)	#Resultado = True
a = 5
b = 7
c = a > b	#Resultado = False
print(c)
print(9>2)	#Resultado = True

# == Este es el operador de igual que, y se utiliza en las expresiones relacionales para saber si un operando es igual a otro operando.

a = 5 == 5
print(a)	# True
a = 6
b = 9
c = a == b
print(c)	# False
print(6==2)	# False

# != Este es el operador desigual que, y se utiliza en las expresiones relacionales para saber si un operando es diferente a otro operando.
a = 4 != 2
print(a)	#Resultado = True
a = 5
b = 3
c = a != b	#Resultado = True
print(c)
print(8!=8)	#Resultado = False

# <= Este es el operador de menor igual que, y se utiliza en las expresiones relacionales para saber si un operando es menor o igual a otro operando.
a = 5 <= 3
print(a)	#Resultado = False
x = 7
y = 5
z = x <= y	#Resultado = False
print(z)
print(9<=4)	#Resultado = False

# >= Este es el operador de mayor igual que, y se utiliza en las expresiones relacionales para saber si un operando es mayor igual a otro operando.
a = 2 >= 8
print(a)	#Resultado = False
a = 3
b = 4
c = a >= b	#Resultado = False
print(c)
print(7>=3)	#Resultado = True

# Expresiones lógicas.
# not- Este es el operador lógico para realizar una negación, si el operando no se encuentra en el otro operando, la expresión se cumple y resulta en True, caso contrario, si la expresión no se cumple el resultado es False.
print(not 5>6)	#Resultado = True
print(not 5>4)	#Resultado = False

# and- Este es el operador lógico para realizar una conjugación, si cualquiera de los operadores presentes no se cumple en la expresión lógica, esto resulta en False, caso contrario, si toda la expresión lógica de conjugación se cumple el resultado es True.
print(4-1==3 and 5>6)		#Resultado = False
print(6+7 > 11 and 3==3)	#Resultado = True

# or- Este es el operador lógico para realizar una conjugación, si cualquiera de los operadores presentes no se cumple en la expresión lógica, esto resulta en False, caso contrario, si toda la expresión lógica de conjugación se cumple el resultado es True.
print(4-1==3 or 5>6)		#Resultado = True
print(6+7 > 11 or 3==3)		#Resultado = True

#Expresiones de caracter
import re
frase = "Tengo 2 hijos que tienen 15 y 11 años"
patron = '[0-9]+' #Esta es una expresión regular
re.findall(patron, frase)	#Resultado ['2','15','12']
