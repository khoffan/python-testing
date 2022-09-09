# star pattren
def stiarcase(n, ch):
    i=0
    while(i<=n+1):
        pattern = " "*(n-i) + ch *i
        i+=1
    return " "+pattern

