decoding_key = int(input())
number_of_symbols = int(input())
decoded_word = ''
for i in range(number_of_symbols):
    coded_symbol = input()
    decoded_symbol = chr(ord(coded_symbol) + decoding_key)
    decoded_word += decoded_symbol
print(decoded_word)

