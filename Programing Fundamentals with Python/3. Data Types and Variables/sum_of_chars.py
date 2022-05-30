num = int(input())
char_value_sum = 0
for i in range(num):
    input_char = ord(input())
    char_value_sum += input_char
print(f'The sum equals: {char_value_sum}')