#open files and set variables
f = open ('Inputs/Input_BS_4_DNA_fin.txt', 'r')
rf1 = f.readlines()[0]
f.close()
f = open ('Inputs/Input_BS_4_DNA_fin.txt', 'r')
rf2 = f.readlines()[1]
f.close()
#define string length
lenf = len (rf1)
#set initial Hamming to 0
ham = 0
#check that above worked
print ('sequence 1 is {}'.format(rf1))
print ('sequence 2 is {}'.format(rf2))
print ('length is {}'.format(lenf))
#iterate for each position in string i from position 0 to last (lenf -1)
for i in range (0, lenf-1):
    if rf1[i] == rf2[i]:
        ham = ham
    elif rf1[i] != rf2[i]:
        ham = ham + 1
        
print ('hamming distance is {}'.format(ham))

