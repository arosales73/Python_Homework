#    # código

**Ejemplo: **

a=2
b=2
if a >  b :
    print ( ' b es mayor que b ' )
elif a <  b :
    print ( ' a es menor que b ' )
else :
    print ( 'a es igual a b' )		#a es igual a b

###  condiciones anidadas. Las condiciones pueden ser anidadas
a=2
b=3
c=4
if a >  b :
    if a>c:
        print('a es el valor mayor')		#No imprime nada


Podemos evitar escribir una condición anidada usando el operador lógico _and_ .
###  Condición si y el operador lógico y
a=2
b=3
c=4
if (a>b) and (a>c):
    print('a es el valor mayor')
elif (b>a) and (b>c):
    print('b es el valor mayor')
else:
        print ('c es el valor mayor')		#c es el valor mayor

###  Condición si y el operador lógico o

a=2
b=2
c=4
if ((a==b) or (a==c)):
    print('a es igual a otro numero')		# a es igual a otro numero
