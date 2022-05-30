first_string = input()
second_string = input()
mutate_string = first_string
for index in range(len(first_string)):
    left_side = second_string[:index+1]
    right_side = first_string[index+1:]
    output_string = left_side + right_side
    if not mutate_string == output_string:
        print(output_string)
    mutate_string = output_string
