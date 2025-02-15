import Variables.variables
import random

vowels = Variables.variables.vowels
consonants = Variables.variables.consonants
numbersEven = Variables.variables.numbers_even
numbersOdd = Variables.variables.numbers_odd
specialCharacters = Variables.variables.special_chars
current = Variables.variables.current

def rpcFrmTxt(frmTxt):
    nwTxt = ''

    for char in frmTxt:
        if char == '-':
            nwTxt += random.choice(consonants)
        elif char == '.':
            nwTxt += random.choice(vowels)
        elif char == '_':
            nwTxt += random.choice(current)
        else:
            nwTxt += random.choice(specialCharacters)
    return nwTxt          