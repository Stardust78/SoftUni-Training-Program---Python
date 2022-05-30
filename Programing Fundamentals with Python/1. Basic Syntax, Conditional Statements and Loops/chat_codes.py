number_of_messages = int(input())
decoded_message = ''
for messages in range(number_of_messages):
    number = int(input())
    if number == 88:
        decoded_message = 'Hello'
    elif number == 86:
        decoded_message = 'How are you?'
    elif number < 88:
        decoded_message = 'GREAT!'
    elif number > 88:
        decoded_message = 'Bye.'
    print(decoded_message)
