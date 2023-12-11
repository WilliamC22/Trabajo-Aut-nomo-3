import random

# Lista de dibujos del ahorcado
ahorcado_dibujos = [
    '''
    +---+
    |   |
        |
        |
        |
        |
    =========''',
    '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''',
    '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''',
    '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========''',
    '''
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
    =========''',
    '''
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
    =========''',
    '''
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
    ========='''
]

# Función para obtener una palabra aleatoria del conjunto de palabras
def obtener_palabra():
    palabras = ['python', 'programacion', 'ordenador', 'desarrollo', 'tecnologia', 'inteligencia']
    return random.choice(palabras)

# Función para mostrar la palabra con letras adivinadas y guiones para letras no adivinadas
def mostrar_palabra_oculta(palabra, letras_adivinadas):
    resultado = ''
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra + ' '
        else:
            resultado += '_ '
    return resultado

# Función principal del juego
def juego_ahorcado():
    print('¡Bienvenido al Juego del Ahorcado!')
    palabra_a_adivinar = obtener_palabra()
    letras_adivinadas = set()
    intentos_restantes = len(ahorcado_dibujos) - 1

    while True:
        print(ahorcado_dibujos[intentos_restantes])
        print('Palabra a adivinar:', mostrar_palabra_oculta(palabra_a_adivinar, letras_adivinadas))

        # Verificar si se adivinó la palabra
        if mostrar_palabra_oculta(palabra_a_adivinar, letras_adivinadas).replace(' ', '') == palabra_a_adivinar:
            print('¡Felicidades! Has adivinado la palabra:', palabra_a_adivinar)
            break

        # Verificar si se agotaron los intentos
        if intentos_restantes == 0:
            print('¡Oh no! Has agotado tus intentos. La palabra era:', palabra_a_adivinar)
            break

        letra_ingresada = input('Ingresa una letra: ').lower()

        # Validar la entrada del usuario
        if len(letra_ingresada) != 1 or not letra_ingresada.isalpha():
            print('Por favor, ingresa una sola letra válida.')
            continue

        # Verificar si la letra ingresada ya fue adivinada anteriormente
        if letra_ingresada in letras_adivinadas:
            print('Ya has ingresado esa letra. Intenta con otra.')
            continue

        letras_adivinadas.add(letra_ingresada)

        # Verificar si la letra ingresada no está en la palabra a adivinar
        if letra_ingresada not in palabra_a_adivinar:
            intentos_restantes -= 1
            print('Letra incorrecta. Te quedan', intentos_restantes, 'intentos.')

    print('Gracias por jugar al Ahorcado!')

# Iniciar el juego
if __name__ == "__main__":
    juego_ahorcado()
