
input_data = input()
List_of_vale = []
List_of_zeros = []
answer_line = ""

for i in range(len(input_data)):

    a = input_data.__getitem__(i)

    if a == "0":
        List_of_zeros.append(a)
    elif a == " ":
        continue

    else:
        List_of_vale.append(a)
for j in range(len(List_of_vale)):
    print(List_of_vale.__getitem__(j)+" ",end="")
for k in List_of_zeros:
    print(List_of_zeros.__getitem__(int(k)) + " ", end="")

print(answer_line)
