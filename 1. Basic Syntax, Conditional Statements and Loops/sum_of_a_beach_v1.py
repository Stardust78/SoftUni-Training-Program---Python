input_string = input().lower()
string_length = len(input_string)
# print(string_length)
counter = 0
keywords = ['sand', 'water', 'fish', 'sun']
for i in range(len(keywords)):
    try:
        start_index = input_string.index(keywords[i])
        counter += 1
        while (string_length - start_index) >= (len(keywords[i]) - 1):
            try:
                start = start_index + len(keywords[i]) + 1
                start_index = input_string.index(keywords[i], start, string_length)
                counter += 1
                continue
            except ValueError:
                break
    except ValueError:
        continue

print(counter)


