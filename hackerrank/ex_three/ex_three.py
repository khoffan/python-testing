def caesarCipher(s, k):
    ceasar = k%26
    fs = ""
    if s == '' or len(s) > 100 or k > 100:
        return ''
    for i in s:
        if ord(i)>=97 and ord(i)<=(122-ceasar):
            fs+=chr(ord(i)+ceasar)
        elif ord(i) > (122-ceasar) and ord(i)<=122:
            fs+=chr(ord(i)-26+ceasar)
        elif ord(i)>=65 and ord(i)<=(90-ceasar):
            fs+=chr(ord(i)+ceasar)
        elif ord(i) > (90-ceasar) and ord(i)<=90:
            fs+=chr(ord(i)-26+ceasar)
        else:
            fs+=i
    return fs

s = 'Power-to-yourself'
print(caesarCipher(s,4))