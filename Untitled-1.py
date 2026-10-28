
# Open
file_path = r"D:\amrin\sequence.fasta"
output_path = r"D:\amrin\results.csv"
fasta = open(file_path, "r")

# Name
fasta.seek(0)
for line in fasta:
    if line.startswith(">"):
        Name = line[1:].strip()
        print(Name)

# Length
fasta.seek(0)
for line in fasta:
    line = line.strip()
    if not line.startswith(">") and line:
        Seq = line
        Length = len(Seq)
        print(Length)

# gC
fasta.seek(0)
for line in fasta:
    line = line.strip()
    if not line.startswith(">") and line:
        Seq = line.upper()
        GC = (Seq.count("G") + Seq.count("C")) / len(Seq) * 100
        print(round(GC, 2), "%")
# Amino
translator = {
    "GCA": "A", "GCC": "A", "GCG": "A", "GCT": "A",
    "AGA": "R", "AGG": "R", "CGA": "R", "CGC": "R",
    "CGG": "R", "CGT": "R", "GAC": "D", "GAT": "D",
    "AAC": "N", "AAT": "N", "TGC": "C", "TGT": "C",
    "GAA": "E", "GAG": "E", "CAA": "Q", "CAG": "Q",
    "GGA": "G", "GGC": "G", "GGT": "G", "GGG": "G",
    "CAC": "H", "CAT": "H", "ATA": "I", "ATC": "I",
    "ATT": "I", "TTA": "L", "TTG": "L", "CTA": "L",
    "CTC": "L", "CTG": "L", "CTT": "L", "AAA": "K",
    "AAG": "K", "ATG": "M", "TTC": "F", "TTT": "F",
    "CCA": "P", "CCC": "P", "CCG": "P", "CCT": "P",
    "AGC": "S", "AGT": "S", "TCA": "S", "TCC": "S",
    "TCG": "S", "TCT": "S", "ACA": "T", "ACC": "T",
    "ACG": "T", "ACT": "T", "TGG": "W", "TAC": "Y",
    "TAT": "Y", "GTA": "V", "GTC": "V", "GTG": "V",
    "GTT": "V", "TAA": "*", "TAG": "*", "TGA": "*"
}


# Amino
fasta.seek(0)
Name = ""
Seq = ""

for line in fasta:
    line = line.strip()

    if line.startswith(">"):
        if Seq:
            Protein = ""
            for i in range(0, len(Seq) - 2, 3):
                Codon = Seq[i:i+3]
                Protein += translator.get(Codon, "?")
            print(Protein)

        Name = line[1:]
        Seq = ""

    else:
        Seq += line.upper()

if Seq:
    Protein = ""
    for i in range(0, len(Seq) - 2, 3):
        Codon = Seq[i:i+3]
        Protein += translator.get(Codon, "?")
    print(Protein)


# Print all
fasta.seek(0)
Name = ""
Seq = ""
Results = []

for line in fasta:
    line = line.strip()

    if line.startswith(">"):
        if Name:
            Length = len(Seq)
            GC = round((Seq.count("G") + Seq.count("C")) / Length * 100, 2) if Length else 0

            Protein = ""
            for i in range(0, len(Seq) - 2, 3):
                Codon = Seq[i:i+3]
                Protein += translator.get(Codon, "?")

            print("Name:", Name)
            print("Sequence:", Seq)
            print("Length:", Length)
            print("GC:", GC, "%")
            print("Protein:", Protein)
            print("-" * 40)

            Results.append([Name, Length, GC, Protein])

        Name = line[1:]
        Seq = ""

    else:
        Seq += line.upper()

if Name:
    Length = len(Seq)
    GC = round((Seq.count("G") + Seq.count("C")) / Length * 100, 2) if Length else 0

    Protein = ""
    for i in range(0, len(Seq) - 2, 3):
        Codon = Seq[i:i+3]
        Protein += translator.get(Codon, "?")

    print("Name:", Name)
    print("Sequence:", Seq)
    print("Length:", Length)
    print("GC:", GC, "%")
    print("Protein:", Protein)
    print("-" * 40)

    Results.append([Name, Length, GC, Protein])


# CSV
fasta.close()
import csv
with open(output_path, "w", newline="", encoding="utf-8-sig") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["id", "length", "gc_percent", "AA Sequence"])
    writer.writerows(Results)

print("Results saved to:", output_path)

