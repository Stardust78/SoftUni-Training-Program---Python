number_of_strings = int(input())
brackets_balanced = False
left_bracket = 0
right_bracket = 0
for i in range(number_of_strings):
    input_string = input()
    input_string_length = len(input_string)
    if input_string_length == 1:
        string_ascii_number = ord(input_string)
        if string_ascii_number == 40:
            left_bracket += 1
        elif string_ascii_number == 41:
            right_bracket += 1
    if left_bracket - right_bracket > 1:
        break
    brackets_balanced = left_bracket == right_bracket
if brackets_balanced:
    print('BALANCED')
else:
    print('UNBALANCED')





