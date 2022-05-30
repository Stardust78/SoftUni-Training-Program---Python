number_of_strings = int(input())
for words in range(number_of_strings):
    input_word = input()
    if ',' in input_word or '.' in input_word or '_' in input_word:
        print(f"{input_word} is not pure!")
    else:
        print(f"{input_word} is pure.")