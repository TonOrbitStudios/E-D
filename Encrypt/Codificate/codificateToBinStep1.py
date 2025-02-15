import time

from Steps import step1
from Steps import step2
from Steps import step3
from Variables import variables

txt = input('[3NCR1PT3N]==> Enter a string text: ')
while(True):
    confirm = input(f'[3NCR1PT3N]==> Your text is: "{txt}", it\'s correct? [Y/n]: ')
    if confirm == '':
        confirm = 'y'
    if confirm.lower() == 'y':
        startTime = time.time()
        txtBin = step1.txtToBin(txt)
        print('[3NCR1PT3N]==> Binary: ', txtBin)
        txtFrm = step2.binToFrm(txtBin)
        print('[3NCR1PT3N]==> Formated: ', txtFrm)
        txtRplFrm = step3.rpcFrmTxt(txtFrm)
        print('[3NCR1PT3N]==> Encrypted: ', txtRplFrm)
        lenOfOriginalTxt = len(txt)
        lenOfEncriptedOneTxt = len(txtRplFrm)
        print(f'[3NCR1PT3N]==> Lenght of the original text: {lenOfOriginalTxt}, and the lenght of encrypted 1 text is: {lenOfEncriptedOneTxt}')
        endTime = time.time()
        executionTime = endTime - startTime
        print(f'[3NCR1PT3N]==> Time of executing encryption 1: {executionTime} seconds.')
        break
    elif confirm.lower() == 'n':
        
        print('[3NCR1PT3N]==> Encryption canceled.')
        variables.continueToStepTwo = 'n'
        break
    else:
        print('[3NCR1PT3N]==> Invalid y/n argument')





