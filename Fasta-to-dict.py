#!/home/andrew/anaconda3/bin/python

"""
This code takes input of a fasta file and converts it to a dictionary of {header: sequence} pairs
input required is including path
"""

import sys
fasta_file = open(filename, 'r') #open file in read mode
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

print (FASTA_DICT)
