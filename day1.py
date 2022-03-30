import random as rd
import json

def generate_password(words):
    password = ''
    alph=['@','!','#','$','%','^','&','*','(',')','1','2','3','4','5','6','7','8','9','0']
    for i in words:
        password+=i
    for i in range(5):
        l = rd.randrange(len(alph))
        password +=alph[l]

    return password

def check_password(password):
    if len(password) < 8:
        return 'Weak'
    else:
        return 'Strong'

def main():
    username = input('Enter the username : ').split()
    words = input('Enter the words : ').split()
    password = generate_password(words)
    print('Password : ', password)
    print('Password Strength : ', check_password(password))
    details={
        'Username':username,
        'password':password
    }
    with open('password.txt', 'w') as f:
        f.write(json.dumps(details))


if __name__ == '__main__':
    main()