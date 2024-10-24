#Jacob Melendez
def encode(pre_password):
    encoded_password = ""
    for item in pre_password:
        item = int(item)
        item += 3
        if len(str(item)) > 1:
            item %= 10
        encoded_password += str(item)
    return encoded_password

def decode(pre_password):
    decoded_password = ""
    for digit in pre_password:
        decoded_digit = (int(digit) - 3) % 10  # Reverse the shift by 3
        decoded_password += str(decoded_digit)
    return decoded_password


if __name__ == '__main__':
    encoded_pw = ''
    quit = False
    while quit == False:
        print('Menu \n -------------')
        print('1. Encode \n 2. Decode \n 3. Quit')
        option = int(input('Please enter an option: '))
        if option == 1:
            pre_encoded_pw = input('Please enter your password to encode (8 digits): ')
            if len(pre_encoded_pw) == 8 and pre_encoded_pw.isdigit():
                encoded_pw = encode(pre_encoded_pw)
                print(f'Your password has been encoded and stored as: {encoded_pw}')
                print()
            else:
                print("Invalid input. Please enter an 8-digit password.")

        elif option == 2:
            if encoded_pw:
                decoded_pw = decode(encoded_pw)
                print(f'The encoded password is {encoded_pw}, and the original password is {decoded_pw}.')
            else:
                print("No encoded password found. Please encode a password first.")

        elif option == 3:
            quit_program = True
            print("Goodbye!")

        else:
            print("Invalid option. Please choose 1, 2, or 3.")


