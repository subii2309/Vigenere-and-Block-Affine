import operator
from os import system

# characters to numbers tables
cnall = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8,
         'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16,
         'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
         'Z': 25, 'a': 26, 'b': 27, 'c': 28, 'd': 29, 'e': 30, 'f': 31, 'g': 32,
         'h': 33, 'i': 34, 'j': 35, 'k': 36, 'l': 37, 'm': 38, 'n': 39, 'o': 40,
         'p': 41, 'q': 42, 'r': 43, 's': 44, 't': 45, 'u': 46, 'v': 47, 'w': 48,
         'x': 49, 'y': 50, 'z': 51}

cnupper = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8,
           'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16,
           'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
           'Z': 25}

# numbers to characters tables
ncall = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I',
         9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q',
         17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y',
         25: 'Z', 26: 'a', 27: 'b', 28: ',c', 29: 'd', 30: 'e', 31: 'f', 32: 'g',
         33: 'h', 34: 'i', 35: 'j', 36: 'k', 37: 'l', 38: 'm', 39: 'n', 40: 'o',
         41: 'p', 42: 'q', 43: 'r', 44: 's', 45: 't', 46: 'u', 47: 'v', 48: 'w',
         49: 'x', 50: 'y', 51: 'z'}

ncupper = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I',
           9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q',
           17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y',
           25: 'Z'}


def crypted26(vigenere_text, shift_, multiplier_):
    crypt_Text = []

    for clearChar in map(operator.add, vigenere_text[::2], vigenere_text[1::2]):

        # loop characters in key
        a = clearChar

        i = 0
        j = 1
        while i < len(a):

            left = a[i]

            while j < len(a):
                right = a[j]
                h = 0
                char_num = str(cnall[left])
                if len(char_num) == 1:
                    char_num = str(h) + char_num
                # print(charNum)
                char_num1 = str(cnall[right])
                if len(char_num1) == 1:
                    char_num1 = str(h) + char_num1
                # print(charNum1)
                d = int(str(char_num) + str(char_num1))
                z = (int(multiplier_) * d)
                y = (z + int(shift_))
                crypt = (y % 2526)
                crypt_char = str(crypt)
                print(crypt_char)
                if len(crypt_char) == 3:
                    crypt_char = str(h) + crypt_char
                elif len(crypt_char) == 2:
                    crypt_char = str(h) + str(h) + crypt_char
                print(crypt_char)
                crypt_Text.append(crypt_char)

                break

            break
    return ''.join(crypt_Text)


def convert26(crypt_text):
    affine = []

    for char in map(operator.add, crypt_text[::2], crypt_text[1::2]):
        crypted1 = str(char)
        s = 0
        t = 1

        while s < len(crypted1):
            h = 0
            left = crypted1[s]
            if left == str(h):
                left = ''

            while t < len(crypted1):
                right = crypted1[t]

                combine = (str(left) + str(right))
                print(combine)
                lookup = ncall[int(combine)]
                affine.append(lookup)
                break
            break
    return ''.join(affine)


def crypted52(vigenere_, shift_, multiplier_):
    crypt_Text = []

    for clearChar in map(operator.add, vigenere_[::2], vigenere_[1::2]):
        # loop characters in key
        a = clearChar

        i = 0
        j = 1
        while i < len(a):

            left = a[i]

            while j < len(a):
                right = a[j]
                h = 0
                char_num = str(cnall[left])
                if len(char_num) == 1:
                    char_num = str(h) + char_num
                # print(charNum)
                char_num1 = str(cnall[right])
                if len(char_num1) == 1:
                    char_num1 = str(h) + char_num1
                # print(charNum1)
                d = int(str(char_num) + str(char_num1))
                z = (int(multiplier_) * d)
                y = (z + int(shift_))
                crypt = (y % 5152)
                crypt_char = str(crypt)
                print(crypt_char)
                if len(crypt_char) == 3:
                    crypt_char = str(h) + crypt_char
                elif len(crypt_char) == 2:
                    crypt_char = str(h) + str(h) + crypt_char
                print(crypt_char)
                crypt_Text.append(crypt_char)

                break

            break
    return ''.join(crypt_Text)


def convert52(crypt_text):
    affine = []

    for char in map(operator.add, crypt_text[::2], crypt_text[1::2]):
        crypted1 = str(char)
        s = 0
        t = 1

        while s < len(crypted1):
            h = 0
            left = crypted1[s]
            if left == str(h):
                left = ''

            while t < len(crypted1):
                right = crypted1[t]

                combine = (str(left) + str(right))
                print(combine)
                lookup = ncall[int(combine)]
                affine.append(lookup)
                break
            break
    return ''.join(affine)


while True:

    with open('vigenerecipheroutput.txt', 'r') as myfile:
        vigenere = myfile.read().replace('\n', '')
    print(vigenere)

    shift = input("Enter value of b\n\n")
    system('cls')

    multiplier = input("Enter value of m\n\n")
    system('cls')

    choice = input("Enter S or L\n\n")
    system('cls')

    if choice.lower() == 's':
        vigeneretext = vigenere.upper()
        cryptText = crypted26(vigeneretext, shift, multiplier)
        print(cryptText)
        AffineText = convert26(cryptText)
        print(AffineText)
        print('done')
        cryptDir = open('C:/Users/subin/Documents/python progs/stringformatting/blockaffinecipheroutputtext.txt', 'w')
        cryptDir.write(cryptText)
        cryptDir.close()
        break

    elif choice.lower() == 'l':

        cryptText = crypted52(vigenere, shift, multiplier)
        print(cryptText)
        AffineText = convert52(cryptText)
        print(AffineText)
        print('done')
        cryptDir = open('C:/Users/subin/Documents/python progs/stringformatting/blockaffinecipheroutputtext.txt', 'w')
        cryptDir.write(cryptText)
        cryptDir.close()
        break
    break
