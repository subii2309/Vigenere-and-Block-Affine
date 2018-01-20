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

# numbers to characters table UP
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


def decrypt52(key_, crypt_text):
    clear_text = []
    num_key = []
    key_count = 0

    for keyClearChar in key_:
        key_num = cnall[keyClearChar]
        num_key.append(key_num)

    for cryptChar in crypt_text:
        if key_count == len(key_):
            key_count = 0
        crypt_num = cnall[cryptChar]
        key_index = num_key[key_count]
        clear_char = ncall[((crypt_num - key_index) % 52)]
        clear_text.append(clear_char)
        key_count += 1

    return ''.join(clear_text)


def decrypt26(key_, crypt_text):
    clear_text = []
    num_key = []
    key_count = 0

    for keyClearChar in key_:
        key_num = cnupper[keyClearChar]
        num_key.append(key_num)

    for cryptChar in crypt_text:
        if key_count == len(key_):
            key_count = 0
        crypt_num = cnupper[cryptChar]
        key_index = num_key[key_count]
        clear_char = ncupper[((crypt_num - key_index) % 26)]
        clear_text.append(clear_char)
        key_count += 1

    return ''.join(clear_text)


with open('key.txt', 'r') as myfile:
    key = myfile.read().replace('\n', '')
    print(key)

while True:
    choice = input("Enter S or L\n\n")
    system('cls')

    if choice.lower() == 's':
        key1 = key.upper()
        cryptDir = open("C:/Users/subin/Documents/python progs/stringformatting/blockaffinecipherplainoutput.txt", 'r')
        cryptText = list(cryptDir.read())
        clearText1 = decrypt26(key1, cryptText)
        decryptDir = open('C:/Users/subin/Documents/python progs/stringformatting/secondplaintext.txt', 'w')
        decryptDir.write(clearText1)
        decryptDir.close()
        break

    elif choice.lower() == 'l':

        cryptDir = open("C:/Users/subin/Documents/python progs/stringformatting/blockaffinecipherplainoutput.txt", 'r')
        cryptText = list(cryptDir.read())
        clearText2 = decrypt52(key, cryptText)
        decryptDir = open('C:/Users/subin/Documents/python progs/stringformatting/secondplaintext.txt', 'w')
        decryptDir.write(clearText2)
        decryptDir.close()
        break

print("Done!")
