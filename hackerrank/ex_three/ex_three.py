def caesarCipher(s, k):
    encrypt = ''
    charmap = 'abcdefghijklmnopqrstuvwxyz'
    k %26
    en_map = charmap[k:] + charmap[:k]

    charmap += charmap.upper()
    en_map += en_map.upper()
    for ch in s:
        newch = ch
        index = charmap.find(ch)
        if index >= 0:
            newch = en_map[index]
        encrypt += newch
    return encrypt