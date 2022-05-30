ranges = int(input())
abc = ['a', 'b', 'c']
for i in range (ranges):
    char_one = abc[i]
    for j in range(ranges):
        char_two = abc[j]
        for k in range(ranges):
            char_three = abc[k]
            print(f'{char_one}{char_two}{char_three}')
