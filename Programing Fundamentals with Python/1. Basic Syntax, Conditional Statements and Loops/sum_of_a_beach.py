input_string = input().lower()
counter = 0

for i in range(len(input_string)):
    if input_string[i] == 'w' and (len(input_string) - i) >= 5:
        check = ""
        for j in range(i, i+5):
            check += input_string[j]
        if check == "water":
            counter += 1
    if input_string[i] == 'f' and (len(input_string) - i) >= 4:
        check = ""
        for j in range(i, i+4):
            check += input_string[j]
        if check == "fish":
            counter += 1
    if input_string[i] == 's':
        check = ""
        if input_string[i+1] == 'a' and (len(input_string) - i) >= 4:
            for j in range(i, i+4):
                check += input_string[j]
            if check == "sand":
                counter += 1
        elif input_string[i+1] == 'u' and (len(input_string) - i) >= 3:
            for j in range(i, i+3):
                check += input_string[j]
            if check == "sun":
                counter += 1
print(counter)

