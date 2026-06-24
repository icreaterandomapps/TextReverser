TEX = input("Put your text here to reverse it> ")
rev = ""

for ch in TEX:
    rev = ch + rev

print("Here is your text reversed:", rev)

input("Press Enter to exit...")