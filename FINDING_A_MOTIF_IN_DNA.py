f = open ('Inputs/Motifs_in_DNA.txt', 'r')
seq = f.readlines()[0].rstrip("\n")
f.close()
f = open ('Inputs/Motifs_in_DNA.txt', 'r')
motif = f.readlines()[1].rstrip("\n")
f.close()
o = open ('Outputs/Motifs_in_DNA.txt', 'w')

print (seq)
print (motif)

x = 0
y = int (len (motif))

for i in seq:
    if seq [x:y] == motif:
        o.write (str (x + 1) + ' ')
    x = x + 1
    y = y + 1
o.close()

final = open ('Outputs/Motifs_in_DNA.txt', 'r')
print (final.read())
final.close()
