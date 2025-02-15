from StepsV2 import step1
from StepsV2 import step2
from StepsV2 import step3

from Variables import variables
start = variables.start

def encLvlTwoToText(encLvlTwo):
    frm = step1.encLvlOneToFrm(encLvlTwo)
    print(f'{start}Formated text: {frm}')

    bin = step2.frmToBin(frm)
    print(f'{start}Binary text: {bin}')

    num = step3.binToNum(bin)
    return num

    

    