import re
s1 = 'apple kiwi banana straw'
s2 = 'apple kiwi banana application'
try:
    #match = re.search('ap+le|straw|melon', s1)
    #print( match.group() )
    #my = re.findall('ap+le|straw|melon', s1)
    #print(my)
    #matchs = re.finditer('ap+le|straw|melon', s1)
    #for m in matchs:
    #    print( m )
    my = re.findall('ap[a-z]+', s2)
    print(my)
except Exception as err:
    print("Not Found")
