def caesarCipher(s, k):
    # Write your code here
    k = k%26
    fs = ""
    for i in s:
        if ord(i)>=97 and ord(i)<=(122-k):
            fs+=chr(ord(i)+k)
        elif ord(i) > (122-k) and ord(i)<=122:
            fs+=chr(ord(i)-26+k)
        elif ord(i)>=65 and ord(i)<=(90-k):
            fs+=chr(ord(i)+k)
        elif ord(i) > (90-k) and ord(i)<=90:
            fs+=chr(ord(i)-26+k)
        else:
            fs+=i
    return fs