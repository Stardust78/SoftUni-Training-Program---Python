input_string = input()

while not input_string == 'End':
    output_string = ''
    if input_string == 'SoftUni':
        input_string = input()
        continue
    for index in range(len(input_string)):
        output_string += (input_string[index]*2)
    print(output_string)
    input_string = input()
