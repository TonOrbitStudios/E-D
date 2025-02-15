from StepsV2 import step1v2
from Variables import variables

prt = ''
numPrt = 0
numOfGlobPrt = 0

for letter in variables.letters:
    prt = step1v2.fndPrtFrsLetCncWith(letter)
    print(f'\033[32m[L3TT0PRT]\033[34m==>\033[36m For letter\033[0m {letter}, \033[36mexists:\033[0m {prt}')
    numPrt = len(prt)
    print(f'\033[32m[L3TT0PRT]\033[34m==>\033[36m For letter\033[0m {letter}, \033[36mexists:\033[0m {numPrt} \033[36mNumber of ports\033[0m')
    numOfGlobPrt += numPrt

print(f'\033[32m[L3TT0PRT]\033[34m==> \033[36mNumber total of ports:\033[0m {numOfGlobPrt}')
