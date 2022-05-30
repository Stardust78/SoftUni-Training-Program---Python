start_range = int(input())
end_range = int(input())
output_string = ''

for char in range(start_range, end_range + 1):
    output_string += chr(char) + chr(32)
print(output_string)