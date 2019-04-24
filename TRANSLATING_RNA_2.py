codon_table_RNA = {
    'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
    'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',
    'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
    'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
    'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
    'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
    'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
    'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
    'UAC':'Y', 'UAU':'Y', 'UAA':'_', 'UAG':'_',
    'UGC':'C', 'UGU':'C', 'UGA':'_', 'UGG':'W',}
f = open ('Inputs/split_RNA_trips.txt', 'r')
seq = f.read()
#need to separate triplets into list
#['AUG', 'GCC', etc]
z = int (len (seq) / 3)
x = 0
y = 3
trip = []
for i in range (0,z):
    l = (seq [x:y])
    trip.append(l)
    x = x + 3
    y = y + 3
print (trip)
len (seq)
o = open ('Outputs/Translated_RNA.txt', 'w')
for i in trip:
    if codon_table_RNA[i] == '_':
        o.close()
    elif codon_table_RNA[i] != '_':
        o.write(codon_table_RNA[i])
o.close()
final = open('Outputs/Translated_RNA.txt', 'r')
print (final.read())
final.close()
