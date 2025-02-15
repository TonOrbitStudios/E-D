from Variables import variables
def encLvlTwoToFrm(txtEnc):
    frm = ''
    for letter in txtEnc:
        if letter in variables.numbers_even or letter.upper() in variables.vowels:
            frm += '.'
        elif letter in variables.numbers_odd or letter.upper() in variables.consonants:
            frm += '-'
    return frm