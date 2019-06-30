#Honestly this code is pretty messy but it does get the job done. would be good to have a fasta parser at the beginning to sort out the sequence (and allow multiple sequences to be analysed). Also want to get better at linking separate functions together. at the moment I have basically writted it as one big script but have defined each function separately. linking effectively will be my goal in the future.

sequence = input('enter sequence please: ')

"""
code to get a DNA sequence into a dictionary of reading frames containing codons 
these can then be iterated through attempting to create with no dependencies such as biopython.
"""

"""
reverse complement function- provides the reverse_complement when provided a DNA input as an argument

"""

def reverse_complement(DNA):
    DNA = DNA.upper()
    revcompDict = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}
    i = 1
    x = 0
    revseq = ''
    revcompseq = ''
    for i in range (1, len(DNA) + 1):
        revseq = DNA[-i]
        revcompseq = revcompseq + revcompDict[revseq]
    return revcompseq

reverse_complement(sequence)

"""
CODON_dictionary function- takes a DNA sequence as an input and provides a list of codons in ALL reading frames of a sequence including
reverse complement- outputs to a dictionary of form ORF[i]=['AAA','ATG', etc] where i is the reading frame
the reverse codons start from 4 and go to 6
"""

def CODON_LIST(DNA):
    DNA = DNA.upper()
    x = 0
    y = 3
    j = 1
    ORFs = {}
    codons = []
    while y <= (len(DNA)):
        codons.append(DNA[x:y])
        x = x + 3
        y = y + 3
        if y >= len(DNA)-2:
            ORFs[j] = codons
            if j < 3:
                codons = []
                x = 0 + j
                y = 3 + j
                j = j + 1
                continue
            else:
                break
    
    DNA = reverse_complement(DNA)
    x = 0
    y = 3
    j = 4
    codons = []
    while y <= (len(DNA)):
        codons.append(DNA[x:y])
        x = x + 3
        y = y + 3
        if y >= len(DNA)-2:
            ORFs[j] = codons
            if j < 6:
                codons = []
                x = 0 + j
                y = 3 + j
                j = j + 1
                continue
            else:
                break
    return (ORFs)

"""
the translate function is designed to work on any LIST OF CODONS in a dictionary format where the key is an 
integer representing the reading frame from 1 - 6. therefore it has the function to check if the reading frame
exists in the dictionary, translate the sequences to protein and output a protein sequence dictionary.
"""
CODON_LIST = CODON_LIST(sequence)

def TRANSLATE(CODON_LIST):
    protein_frame_dict = {}
    codon_table_DNA = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',}
    for i in range(1,7):
        frame = i
        codons = CODON_LIST[i]
        protein_list = []
        for codon in codons:
            next_protein = codon_table_DNA[codon]
            protein_list.append(next_protein)
        protein_frame_dict[frame] = protein_list
    return (protein_frame_dict)

AMINO_ACIDS = TRANSLATE (CODON_LIST)

"""
next translate then search backwards through list from list[-1] if stop codon then start recording in variable 
until M is reached in which case you record the ORF and continue. if list[0] or a stop is reached then break 
and start from new stop or iterate next ORF set.
"""
def ORF_FINDER(Amino_Acid_Dict):
    Final_ORFs = []
    for i in range(1,7):
        amino_acids = Amino_Acid_Dict[i]
        x = len (Amino_Acid_Dict[i]) + 1
        stop = ''
        start = ''
        for position in range(-1,-x,-1):
            ORF = ""
            amino_acid = amino_acids[position]
            #print (amino_acid) - to confirm correct aa's allocated
            if amino_acid == '_':
                stop = int(position)
                continue
            if stop == '':
                continue
            elif stop != '':
                if amino_acid == 'M':
                    start = int(position)
                    ORF = (amino_acids[start:stop])
                    joined_ORF = "".join(ORF)
                    Final_ORFs.append(joined_ORF)
                elif amino_acid != 'M':
                    continue
            continue
    
    return (Final_ORFs)
"""
Because of the mutable nature of the list object you can't directly use the set command (gives unordered)
but unique list of everything in a list so first needs to be converted to a tuple then a set then back to a
list to use the join method. unfortunate but necessary probably a more elegant way to do this.
"""

tupe = tuple (ORF_FINDER(AMINO_ACIDS))
sets = set (tupe)
lists = list (sets)
for i in lists:
    print (i)
