#enter file details and open
f = open ('Inputs/rosalind_dna.txt', 'r')
dnaseq = (f.read())
print (dnaseq)
#create output directory
o = open ('Outputs/O_rosalind_dna.txt.txt', 'w')
a = dnaseq.count('A')
c = dnaseq.count('C')
t = dnaseq.count('T')
g = dnaseq.count('G')
sa = str(a)
sc = str(c)
sg = str(g)
st = str(t)
print (sa + ' ' + sc + ' ' + sg + ' ' + st)
x = sa + ' ' + sc + ' ' + sg + ' ' + st
y = str(x)
o.write(y)
