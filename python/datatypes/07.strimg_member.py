s1 = '   abc   '
s2 = '###abc---'
s3 = '000 111 222'
s4 = '000-111-222'
s5 = 'i like python like program'
#white space: ' ', \n, \t, \r
# s2 =s1.strip()
print( s1.strip()) #ctrl + q (다큐먼트)
print( s2.strip('#-'))
print( s3.split() )
print( s4.split('-') )
print( s5.replace('like','love'))
