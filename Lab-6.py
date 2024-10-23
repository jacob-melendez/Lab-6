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

if __name__ == '__main__':
    encoded_pw = ''
    quit = False
    while quit == False:
        print('Menu \n -------------')
        print('1. Encode \n 2. Decode \n 3. Quit')
        option = int(input('Please enter an option: '))
        if option == 1:
            pre_encoded_pw = input('Please enter your password to encode: ')
            encoded_pw = encode(pre_encoded_pw)
            print('Your password has been encoded and stored!')
            print()
        elif option == 2:
            pass
        elif option == 3:
            quit = True



