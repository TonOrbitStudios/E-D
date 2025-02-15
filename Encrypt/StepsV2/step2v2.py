def numToBinV2(text):
    result = []
    
    for char in text:
        if isinstance(char, str) and len(char) == 1:
            result.append(format(ord(char), '08b'))
        else:
            result.append(char)
    return ''.join(result)
