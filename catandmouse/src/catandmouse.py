from cgitb import reset


def cat_and_mouse(x: int ,y:int,z:int):
    distanceA = abs(x - z)
    distanceB = abs(y - z)
    if distanceA > distanceB:
        return 'Cat B'
    elif distanceA < distanceB:
        return 'Cat A'
    else:
        return 'Mouse C'
 
# if __name__ == '__main__':
#     line_st = input("Enter a b c: ")
#     line = map(int,line_st.split())

#     result = cat_and_mouse(*line)
#     print("result",result)
