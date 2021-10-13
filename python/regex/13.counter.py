from collections import Counter
myList =['aa','bb','cc','aa','aa','bb']
c = Counter(myList)
print( c )
print( c.most_common() )
print( c.most_common(1) )
