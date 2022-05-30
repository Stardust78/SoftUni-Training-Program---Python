input_number = input()
input_list = []
max_number = ''
for index_i in range(len(input_number)):
    input_list += input_number[index_i]
input_list.sort(reverse=True)
for index_i in range(len(input_list)):
    max_number += input_list[index_i]
print(max_number)


