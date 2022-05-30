input_command = input()
number_of_coffees_needed = 0

while not input_command == 'END':
    if input_command.isupper():
        if input_command == 'DOG' or input_command == 'CAT' or input_command == 'CODING' or input_command == 'MOVIE':
            number_of_coffees_needed += 2
        else:
            input_command = input()
            continue
    else:
        if input_command == 'dog' or input_command == 'cat' or input_command == 'coding' or input_command == 'movie':
            number_of_coffees_needed += 1
        else:
            input_command = input()
            continue
    input_command = input()

if number_of_coffees_needed > 5:
    print("You need extra sleep")
else:
    print(number_of_coffees_needed)
