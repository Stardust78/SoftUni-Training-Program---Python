number_of_strings = int(input())
brackets_balanced = False
left_bracket_counter = 0
right_bracket_counter = 0
for i in range(number_of_strings):
    input_string = input()
    if len(input_string) == 1:
        left_bracket_counter += input_string.count('(')
        right_bracket_counter += input_string.count(')')
    if abs(left_bracket_counter - right_bracket_counter) > 1:
        break
    brackets_balanced = left_bracket_counter == right_bracket_counter
if brackets_balanced:
    print('BALANCED')
else:
    print('UNBALANCED')





