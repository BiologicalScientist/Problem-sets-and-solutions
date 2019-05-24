# open FASTA file and splite into headers and sequences dictionary from previous code

fasta_file = open('Inputs/GC_content.txt', 'r') #open file in read mode
FASTA_DICT = {} #initialise dictionary object

for line in fasta_file: #iterate through the lines in the fasta file
    line = line.rstrip() #remove the newline character from the end of the line
    
    if line[0] == '>':
        seq_name = line[1:]
        FASTA_DICT[seq_name] = '' # create empty entry in dictionary value 
    elif line[0] != '>':
        sequence = line
        FASTA_DICT[seq_name] = FASTA_DICT[seq_name] + sequence
        
fasta_file.close()

# compute GC content and print maximum on screen
maxGC = 0 #initialise maximum GC variable (needs to be outside of for loop)
for header in FASTA_DICT.keys(): #take the key from the dictionary FASTA_DICT and store as header variable
    GC = 0 # initialise GC variable
    sequence = FASTA_DICT[header] # take the value for the header key in FASTA_DICAT and store sequence variable
    length = len (sequence) #take length of the sequence variable (total sequence length)
    for nucleotide in sequence: #iterate through each nucleotide in the sequence variable
        if nucleotide == 'C':
            GC = GC + 1
        if nucleotide == 'G':
            GC = GC + 1 # if the nucleotide is a G or C then increase GC count by 1 else continue to next variable
        if nucleotide not in ['A', 'T', 'C', 'G']:
            print (header, 'contains invalid sequence')
        else: 
            continue
    GC_percent = (GC / length) * 100
    if GC_percent > maxGC:
        maxGC = GC_percent
        maxGCstr = str(maxGC)
        maxsequence = header
    else:
        continue

    
print (maxsequence)
print (maxGCstr)        
