from Variables import letters
from Variables import variables

def listOfNumToText(num_list):
    text = ''

    num_list = list(map(int, num_list))
    for number in num_list:

        for letter in variables.letters.lower():
            letter = letter.lower()

            if hasattr(letters, letter):
                listLetter = getattr(letters, letter)

                if number in listLetter:
                    text += letter.upper()
                    break


    return text
