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
    