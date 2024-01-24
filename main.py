import random

lower_alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
    'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
    'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
    'z'
]
upper_alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
    'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
    'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
    'Z'
]
numbers = [
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 0
]
symbols = [
    '!', '@', '#', '$', "%"
    '^', '&', '*', '(', ")"
]
mixed = lower_alphabet + upper_alphabet + numbers + symbols
password = ''

if __name__ == '__main__':
    try:
        length = int(input('Length: '))
    except ValueError:
        print('Only int allowed')

    while (length):
        a = random.choice(mixed)
        password += str(a)
        length -= 1
    print(password)

