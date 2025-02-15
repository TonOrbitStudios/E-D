from Decodificate import decodificateLevelOneToText

from Steps import step1
from Steps import step2
from Steps import step3
from Steps import step4
from Steps import step5

from Variables import variables
start = variables.start

txtEcyLvlTwo = input(f'{start}Enter a level 2 encripted text: ')

if txtEcyLvlTwo != '':
    frm = step1.encLvlTwoToFrm(txtEcyLvlTwo)
    print(f'{start}Formated text: {frm}')

    bin = step2.frmToBin(frm)
    print(f'{start}Binary text: {bin}')

    num = step3.binToNum(bin)
    print(f'{start}Numbers: {num}')

    list = step4.numToList(num)
    print(list)

    text = step5.listOfNumToText(list)
    print(f'{start}Text encrryption 1: {text}')

    txt = decodificateLevelOneToText.encLvlTwoToText(text)
    print(f'{start}Text: {txt}')

    