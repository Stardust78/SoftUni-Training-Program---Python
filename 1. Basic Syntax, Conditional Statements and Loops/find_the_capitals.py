input_string = input()
output_value = []
for index in range(len(input_string)):
    if input_string[index].isupper():
        output_value.append(index)
    else:
        continue
print(output_value)