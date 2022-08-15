# star pattren
def stiarcase(number, ch):
    k = number 
    for i in range(0, number):
        # process each column
        for j in range(0, k):
            # print space in pyramid
            print(end=" ")
        k = k-1
        for j in range(0, i + 1):
            # display star
            print(ch, end="")
        print(" ")


stiarcase(4, '#')
