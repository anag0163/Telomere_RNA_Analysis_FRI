from Bio import SeqIO #import necessary library

# Define the input sequences
seq1 = SeqIO.SeqRecord("aactcgggggtgtggggttgagattgcgcacaagttttcttaaaccctaaaccgcttctgtaatcagaagatttgtgaaaggggtggtttgtccggtgttttcccctttaaaaaaagaaacaccgatgcctgttgtgtctatctcaaagttgaatatatctccctggcaagtttgtaggtagtgccattgacatgaaaattgtcttgtggtcacttcattcctcgcttgccaagcactcccattttttt")
seq2 = SeqIO.SeqRecord("tcgggggtgtggggttgagattgcacataaatattgttaaaccctaaaccacttctgtaaccagaaggtttgtggtaggggtggtttgtccggtgtttccccctttaaaaaaagaaacaccgatgcctgccgtgtgtatctcaaagttgattatatatcccctggcaagtttgtaggtagtgccattggcatgaaaaatgtcttgtggtcacttcattcctcgcttgccaagcacctccaatttttt")
sequences = [seq1, seq2]

#get the minimum length of all the sequences
seq_lengths = [len(s) for s in sequences]
min_length = min(seq_lengths)

#trim all sequences to the minimimum length (form of alignment)
sequences = [s[:min_length] for s in sequences]

# Convert the sequences to uppercase
sequences = [s.upper() for s in sequences]

# Create a list to hold the conserved sequence
conserved = []

# Iterate over each position in the sequences
for i in range(min_length):

    # Get the nucleotides at this position in all sequences
    nucleotides = [s[i] for s in sequences]

    # If all nucleotides are the same, add the nucleotide to the conserved sequence
    if len(set(nucleotides)) == 1:
        conserved.append(nucleotides[0])

    # Otherwise, add a gap character to the conserved sequence
    else:
        conserved.append("-")
conserved_seqs = []

# Initialize a variable to keep track of the current conserved sequence
current_conserved = ""

# Iterate over each character in the conserved sequence
for c in conserved:

    # If the character is a gap, add the current conserved sequence to the list and reset it
    if c == "-":
        if len(current_conserved) >= 5:
            conserved_seqs.append(current_conserved)
        current_conserved = ""

    # Otherwise, add the character to the current conserved sequence
    else:
        current_conserved += c

# If there's still a conserved sequence at the end, add it to the list
if len(current_conserved) >= 5:
    conserved_seqs.append(current_conserved)

# Print the conserved sequences
print(conserved_seqs)