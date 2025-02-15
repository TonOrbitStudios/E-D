from Variables import letters
from Variables import variables

def fndPrtFrsLetCncWith(letter):
    letter = letter.upper()
    if letter in variables.letters:
        return getattr(letters, letter.lower())
