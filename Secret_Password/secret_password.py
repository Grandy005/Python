import random
import string

print('Random Password Generator')
while True:
    length = int(input('Enter the length of your password: '))
    ask = str(input('Do you want to save your password (yes/no)? '))
    if ask == 'Yes' or ask == 'yes' or ask == 'y' or ask == 'Y':
        website = str(input('Enter the website for your password: '))
        route = str(input('Enter the desired saving route: '))

        char = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.sample(char, length))
        print(password)

        file = open(f'{route}', 'a')
        file.write(website)
        file.write(': ')
        file.write(password)
        file.write('\n')
        break

    elif ask == 'No' or ask == 'no' or ask == 'N' or ask == 'n':
        char = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.sample(char, length))
        print(password)
        break
    
    else:
        print('Wrong answer!')