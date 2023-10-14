### Challenges ###
"""
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

"""
def fizzbuzz():
    for n in range(1,101):

        if n % 3 == 0 and n % 5 == 0:
            print('fizzbuzz\n')
        elif n % 3 == 0:
            print('fizz\n')
        elif(n % 5 == 0):
            print('buzz\n')
        else:
            print(f'{n}\n')

"""
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan. 
 * - Dos palabras exactamente iguales no son anagrama. ✔

"""

def is_anagram(word: str, other_word: str) -> bool:
    if word.lower() == other_word.lower():
        return False
    if sorted(word.lower()) == sorted(other_word.lower()):
        return True
    else:
        return False
    
"""

 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...

"""

def fibonacci():
    inicial = 0
    siguiente = 1
    for index in range(50):
        print(siguiente)
        fib = inicial + siguiente
        inicial = siguiente
        siguiente = fib


"""

 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.

"""
import math
def is_prime(number):
    if number < 2:
        return False
    for n in range(2,int(math.sqrt(number)) + 1):
        if number % n == 0:
            return False
    return True


def print_numbers():
    for n in range(101):
        if is_prime(n) == True:
            print(n)

