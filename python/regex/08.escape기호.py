import re

s1 = 'apple ki      i banana'
s2 = 'apple kiwi banana'
try:
    #match = re.search('ki\s+i', s1) # [ \n\r\t]i 이것만 찾아줌
    # match = re.search('\w+\s\w+', s2) # [k \n\r\t]i 이것만 찾아줌
    match = re.search('ki\Si', s2) #ki[^ \n\r\t]i
    match = re.search('(\S+)\s+(\S+i)', s2) #ki[^ \n\r\t]i
    print( match.group() )
    print(match.group(1))
    match = re.search('ki\Si', s2) #ki[^ \n\r\t]i
    print(match.group(2))
except Exception as err:
    print("Not Found")
