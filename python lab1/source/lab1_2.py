file1 = "file1.txt"
file2 = "file2.txt"

# File2 list
file2WordsList = []
# File1 list
file1WordsList = []

# Opening the File and splitting it and reading each word
with open(file2) as f:
    # The below piece of code will gets us the file2 words list in an array in lowercase
    file2WordsList = f.read().lower().split()

with open(file1) as f:
    # The below piece of code will gets us the file1 words list in an array
    file1WordsList = f.read().split()

# Opening File1 with write access
file1Out = open(file1, 'w')

# Looping file1 list and checking whether file1 word is present in file2
for file1Word in file1WordsList:
    if file1Word.lower() not in file2WordsList:
        # Writing to the file if file1 word is not present in file2
        file1Out.write(file1Word+" ")