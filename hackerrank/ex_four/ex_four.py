from itertools import combinations

def alternate(s):
    # Write your code here
    maxlen = 0
    for a, b in combinations(set(s), 2):
        alts = ''.join([c for c in s if c in (a,b)])
        if not (a*2 in alts or b*2 in alts) and len(alts) > maxlen:
            maxlen = len(alts)
    return maxlen

