import csv
def csvWrite():
    fp = open('my.csv', 'w')
    fp = open('my.csv', 'w', newline='')
    wr = csv.writer(fp)
    wr.writerow( ['aa', 10, 20] )
    wr.writerow( ['bb', 30, 40] )
    wr.writerow( ['bb', 50, 60] )
    fp.close()

fp = open('my.csv')
rd = csv.reader(fp)
for a, b, c in rd:
    print(a, b, c)
