import time

from StepsV2 import step0
from StepsV2 import step1v2
from StepsV2 import step2v2
from StepsV2 import step3v2
from StepsV2 import step4

from Variables import variables

from Codificate import codificateToBinStep1

if variables.continueToStepTwo == 'y':
    continueToCifrateTwo = input('[3NCR1PT3N]==> Recived encription 1, continue to encription 2? [Y/n]: ')
    if continueToCifrateTwo == '':
        continueToCifrateTwo = 'y'
    while(True):
        if continueToCifrateTwo == 'y':
            startTime = time.time()
            txtv2 = codificateToBinStep1.txtRplFrm
            print('[3NCR1PT3N]==> Recibed text: ', txtv2)
            prt = step0.txtToPrt(txtv2)
            prtInt = ' '.join(prt)
            print('[3NCR1PT3N]==> Converted text on port(s): ', prtInt)
            prtCad = ' '.join(map(str, prt))
            prtBin = step2v2.numToBinV2(prtCad)
            print('[3NCR1PT3N]==> Ports to binary: ', prtBin)
            prtBinFrm = step3v2.binToFrmV2(prtBin)
            print('[3NCR1PT3N]==> Ports (bin) to formated: ', prtBinFrm)
            prtBinFrmCif = step4.rpcFrmTxtV2(prtBinFrm)
            print('[3NCR1PT3N]==> Formated to encrypted: ', prtBinFrmCif)
            lenOfOriginalTxt = len(codificateToBinStep1.txt)
            lenOfEncriptedOneTxt = len(txtv2)
            lenOfEncriptedTwoTxt = len(prtBinFrmCif)
            print(f'[3NCR1PT3N]==> Lenght of the original text: {lenOfOriginalTxt}, the lenght of encrypted 1 text is: {lenOfEncriptedOneTxt} and the lenght of encrypted 2 text is: {lenOfEncriptedTwoTxt}')
            endTime = time.time()
            executionTime = endTime - startTime
            print(f'[3NCR1PT3N]==> Time of executing encryption 2: {executionTime} seconds.')
            break
        elif continueToCifrateTwo == 'n':
            print('[3NCR1PT3N]==> Canceled encrypted 2')
            break
        else: 
            print('[3NCR1PT3N]==> Error, the promt is not y/n')
