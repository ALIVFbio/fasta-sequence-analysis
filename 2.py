file_path = r"D:\amrin\sequence.fasta"
output_path = r"D:\amrin\output.csv"

sequences = []         

with open(file_path, "r") as fasta:
    name = ""
    sequence = ""

    for line in fasta:
        line = line.strip()

        if line.startswith(">"):
            if sequence:
                sequences.append((name, sequence))
            name = line[1:]
            sequence = ""
        else:
            sequence += line
    if sequence:
        sequences.append((name, sequence))
Results = []
for name, sequence in sequences:
    length = len(sequence)
    Seq = sequence.upper()
    gc = (Seq.count("G") + Seq.count("C")) / length * 100
    Codon_Table = {
    "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
    "TAT": "Y", "TAC": "Y", "TAA": "*", "TAG": "*",
    "TGT": "C", "TGC": "C", "TGA": "*", "TGG": "W",
    "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}
    amino_acid = ""
    for i in range(0, len(Seq) - 2, 3):
        Codon = Seq[i:i+3]
        amino_acid += Codon_Table.get(Codon, "X")
    print("Name:", name)
    print("Sequence:", sequence)
    print("Length:", length)
    print("GC:", (gc), "%")
    print("Amino acid:", amino_acid)
    print("-" * 40)

    Results.append([name, length, (gc), amino_acid])
import csv
with open(output_path, "w", newline="", encoding="utf-8-sig") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["id", "length", "gc_percent", "amino_acid"])
    writer.writerows(Results)

print("Results saved to:", output_path)