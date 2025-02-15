from Variables import letters
from Variables import variables

def listOfNumToText(num_list):
    text = ''

    for number in num_list:
        found = False  # Para saber si encontramos la letra correspondiente

        for letter in variables.letters:
            letter = letter.lower()  # Convertir a minúscula

            if hasattr(letters, letter):  # Verifica si la lista existe en letters.py
                listLetter = getattr(letters, letter)  # Obtiene la lista de números
                print(f"Buscando {number} en {letter}: {listLetter}")  # Depuración

                if number in listLetter:
                    text += letter.upper()  # Agregar la letra en mayúscula
                    print(f"Encontrado: {number} -> {letter.upper()}")  # Depuración
                    found = True
                    break  # Salir del loop cuando encontramos la letra
            
        if not found:
            print(f"No se encontró el número {number}")  # Indica si un número no está en ninguna lista

    return text

# Lista de prueba con números
numeros = [139, 7003, 777, 17500, 6697, 750, 9101, 10051, 10081, 540, 7009, 2430, 135, 2608, 2608]
resultado = listOfNumToText(numeros)

print(f"\nEl texto generado es: {resultado}")
