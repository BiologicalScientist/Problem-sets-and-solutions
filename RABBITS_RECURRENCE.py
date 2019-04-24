#parameters
n = int(input ('n: '))
k = int(input ('k: '))
#initial state
pair = 0
newborns = 1
pregnant = 0

for i in range (0, n-1):
    #number of pregnant rabbits = number of breeding pairs from previous month (needs to come first)
    preg = pair
    print (preg)
    #number of pairs = the number of pairs + the number of newborns from previous month
    pair = pair + newborns
    print (pair)
    #number of newborns = number of pregnant rabbits (this month) giving birth
    newborns = preg * k
    print (newborns)
total = pair + newborns
print ('total number of rabbits after {} months is {}'.format(n, total))
