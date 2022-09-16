# star pattren
def stiarcase(n, ch):
    pattern = []
    space = ' ' * len(ch)

    if 0< n <=30:
        for i in range(1,n+1):
            step = (space * (n-i))+(ch * i)
            pattern.append(step)
        return pattern
    else:
        return pattern    
# print(stiarcase(5,"#"))
