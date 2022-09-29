import re

def alternatingCharacters(s):
    # Write your code here
    ptn = r"([A-Z])(?!\1)"
  
    m2  = re.findall(ptn, s)
     
    result = len(s)- len(m2)
    return result
