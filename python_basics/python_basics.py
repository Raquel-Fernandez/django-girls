# OPERADORES
# suma
2 + 3
# resta
8 - 5
# multiplicacion
3 * 4
# division
10 / 5
#exponencial
2 ** 3

# CADENAS DE CARACTERES
"Hola"
"Hola" + "mundo"
"Runnin' down the hill"
# caracter de escape
'Runnin\' down the hill'
# poner un texto en mayusculas
"Hola".upper()
# longitud de una cadena
len("Hola")
# longitud de un numero
len(str(3412))

# DECLARAR UNA VARIABLE
name = "Roberto"
x = 3
y = 2
# imprimir una variable
print(name)
print(x+y)

# LISTAS
# lista vacia
[]
# ejemplo lista
lottery = [24, 12, 4, 3, 52, 34]
# longitud de una lista
len(lottery)
# ordenar una lista de menor a mayor
lottery.sort()
# invertir el orden de la lista, mostrando de mayor a menor
lottery.reverse()
# añadir un nuevo valor a la lista
lottery.append(172)
# mostrar solo el primer numero de la lista
lottery[0]
# eliminar un elemento de la lista
lottery.pop(0)

# DICCIONARIOS
# diccionario vacio
{}
participant = {'name': 'Ana', 'country': 'Spain', 'favorite_numbers': [7, 13, 18]}
# imprimir un valor del diccionario
print(participant['name'])
# agregar un nuevo valor al diccionario
participant['favorite_language'] = 'Python'
# longitud de un diccionario
len(participant)
# eliminar un elemento del diccionario
participant.pop('favorite_numbers')
# cambiar un valor de un elemento del diccionario
participant['country'] = 'Portugal'

# COMPARACION
5 > 2 #true
3 < 1 #false
5 > 2 * 2 #true
1 == 1 #true
5 != 2 # true
6 > 2 and 2 < 3 #true
3 > 2 or 2 < 1 #true

# BUCLES
# bucle if else
if 3 > 2:
    print('Is true!')
else:
    print('Is false!')
# elif para añadir mas condiciones en el bucle
volume = 57
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("Me duelen las orejas! :(")
# bucle for
# range crea una lista de numeros en serie. En este caso, va de 1 a 9
for i in range(1, 10):
    print(i)

# FUNCIONES
# declarar una funcion
def hi():
    print('Hi there!')
    print('How are you?')
# ejecutar la funcion
hi()
# funciones con parametros
def hi(name):
    print('Hi ' + name + '!')
hi('Marta')

# bucle for usando la funcion recien creada
girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    hi(name)
    print('Next girl')
