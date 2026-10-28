
file_path = r"D:\amrin\sequence.fasta"
fasta = open(file_path, "r")

results = []
name, sequence = "", ""

for line in fasta:
    line = line.strip()

    if line.startswith(">"):
        if sequence:
            length = len(sequence)
            gc = round((sequence.upper().count("G") + sequence.upper().count("C")) / length * 100, 2)
            results.append((name, sequence, length, gc))

        name, sequence = line[1:], ""

    else:
        sequence += line

if sequence:
    length = len(sequence)
    gc = round((sequence.upper().count("G") + sequence.upper().count("C")) / length * 100, 2)
    results.append((name, sequence, length, gc))

fasta.close()
