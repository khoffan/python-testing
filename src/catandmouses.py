def cat_and_mouse(x: int, y: int, z: int):
    if x > 100 or y > 100 or z > 100:
        return ''
    else:
        distanceA = abs(x - z)
        distanceB = abs(y - z)

        if distanceA > distanceB:
            return 'Cat B'
        if distanceA < distanceB:
            return 'Cat A'
        elif distanceA == distanceB:
            return 'Mouse C'


# if __name__ == '__main__':
#     line_st = input("Enter a b c: ")
#     line = map(int,line_st.split())

#     result = cat_and_mouse(*line)
#     print("result",result)
