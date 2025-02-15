from Variables import variables

def encLvlOneToFrm(elo):
    frm = ''
    for letter in elo:
        if letter.upper() in variables.consonants:
            frm += '-'
        elif letter.upper() in variables.vowels:
            frm += '.'
    return frm