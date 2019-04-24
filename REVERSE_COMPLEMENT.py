f = open ('Inputs/Input_BS_3.txt', 'r')
fread = f.read()
lenf = len (fread)
r = open ('Inputs/Input_BS_3_rev.txt', 'w')
i = 1
x = 0
for i in range (1, lenf + 1):
    r.write (fread[-i])
r.close()
f2 = open ('Inputs/Input_BS_3_rev.txt', 'r')
o = open ('Outputs/Output_BS_3_rev_comp.txt', 'w')
f2read = f2.read()
print (f2read)
i = len (f2read)
for i in f2read:
    if i == 'A':
        o.write ('T')
    elif i == 'T':
        o.write ('A')
    elif i == 'G':
        o.write ('C')
    elif i == 'C':
        o.write ('G')
o.close()
