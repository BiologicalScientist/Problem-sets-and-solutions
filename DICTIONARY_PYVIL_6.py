f = open("Inputs/input_6-2.txt", 'r')
o = open("Outputs/output_6.txt", 'w')
read1 = (f.read().strip('\n'))
read2 = read1.split(' ')
dict1 = {}
for i in read2:
    dict1[i] = read2.count(i)
print (dict1)

for i in dict1:
    o.write (i + ' ' + str(dict1[i]) + '\n')
o.close
o = open("Outputs/output_6.txt", 'r')
print (o.read())
o.close()

