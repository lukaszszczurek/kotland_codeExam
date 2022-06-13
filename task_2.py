Lists_of_Lines = []
VOWELS_AVAILABLE = "aAeEiIoOuUyY"
CONSONANTS_AVAILABLE = "bBcCdDfFgGhHjJkKlLmMnNpPqQrRsStTvVwWxXzZ"
vowels = 0
consonants = 0

how_man_lines = int(input())

for i in range(how_man_lines):
    line = input()
    Lists_of_Lines.append(line)
    #Let's join every elements of List into one string
Lists_of_Lines = "".join(Lists_of_Lines)

for j in Lists_of_Lines:
    if j in VOWELS_AVAILABLE:

        vowels += 1
    elif j in CONSONANTS_AVAILABLE:

        consonants += 1
print("Number of vowels " + str(vowels))
print("Number of consonants " + str(consonants))