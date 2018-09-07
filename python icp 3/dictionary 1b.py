import csv
from collections import Counter

wordfreq = {}
with open("codon.tsv") as tsvfile:
  reader = csv.reader(tsvfile, delimiter='\t')
  for row in reader:
    try:
        wordfreq[row[0]] = row[1]
    except:
      pass
while True:
  output = input(" Enter the input sequence: ")
  if len(output)%3 != 0 :
    print("Input Sequence is not valid")
    continue

  codons = [output[i:i+3] for i in range(0, len(output), 3)]
  print("The individual codon sequence is: ", codons)
  try:
    codon_names = list(map(lambda x: wordfreq[x], codons))
    break
  except:
    print("The codon sequence doesnot match with tsv file. Please give one other sequence")

name_counts = Counter(codon_names)
print("The names and count of codons: ", name_counts)