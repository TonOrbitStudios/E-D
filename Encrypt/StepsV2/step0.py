import random
from StepsV2 import step1v2

def txtToPrt(txtv2):
    prts = []
    for letter in txtv2:
        result = step1v2.fndPrtFrsLetCncWith(letter) or []

        if result:
            elegido = str(random.choice(result))
            prts.append(elegido)
        else:
            prts.append(result)

    return prts


