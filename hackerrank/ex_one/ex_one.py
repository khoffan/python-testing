def funnyString(s):
    # Write your code here
    r = s[::-1]
    for i in range(s):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(r[i]) - ord(r[i-1])):
            return 'Not Funny'
        else:
            return "Funny"

