def binToNum(bin):
    number = ''
    for i in range(0, len(bin), 8):
        byt = bin[i:i+8]
        num = int(byt, 2)
        char = chr(num)

        number += char
    return number