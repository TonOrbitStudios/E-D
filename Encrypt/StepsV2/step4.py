import Variables.variables
import random

vowels = Variables.variables.vowels
consonants = Variables.variables.consonants
numbersEven = Variables.variables.numbers_even
numbersOdd = Variables.variables.numbers_odd
specialCharacters = Variables.variables.special_chars
current = Variables.variables.current

def rpcFrmTxtV2(frmTxt):
    nwTxt = ''

    for char in frmTxt:
        if char == '-':
            if random.randint(1, 2) == 1:
                if random.randint(1, 2) == 1:
                    nwTxt += random.choice(consonants)
                else:
                    nwTxt += random.choice(consonants).lower()
            else:
                nwTxt += random.choice(numbersOdd)
        elif char == '.':
            if random.randint(1, 2) == 1:
                if random.randint(1, 2) == 1:
                    nwTxt += random.choice(vowels)
                else:
                    nwTxt += random.choice(vowels).lower()
            else:
                nwTxt += random.choice(numbersEven)
    return nwTxt    