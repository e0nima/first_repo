import random


def text_to_bin(word):
    if word.lower() == "yes":
        return 1
    return 0


digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
doubletrouble_symbols = "il1Lo0O"


def questions():
    return (
        text_to_bin(input("Should we add digits?\n")),
        text_to_bin(input("Should we add lowercase letters?\n")),
        text_to_bin(input("Should we add uppercase letters?\n")),
        text_to_bin(input("Should we add non-alphabet symbols?\n")),
        text_to_bin(input('Are "il1Lo0O" symbols allowed?\n')),
    )


def definition_alphabet():
    chars = []
    min_len = 0
    is_digits, is_lower, is_upper, is_symbols, is_doubletrouble_symbols = questions()

    if is_digits:
        min_len += 1
        chars.append(digits)
    if is_lower:
        min_len += 1
        chars.append(lowercase_letters)
    if is_upper:
        min_len += 1
        chars.append(uppercase_letters)
    if is_symbols:
        min_len += 1
        chars.append(punctuation)
    if not is_doubletrouble_symbols:
        chars = [
            "".join(c for c in charset if c not in doubletrouble_symbols)
            for charset in chars
        ]
    return chars, min_len


def gen_password(lengh, chars):
    password = ""
    alph_str = "".join(chars)
    for _ in range(lengh):
        password += random.choice(alph_str)
    return password


def is_valid(password, alphs):
    for i in range(len(alphs)):
        if not (set(alphs[i]) & set(password)):
            return False
    return True


# main


num = int(input("How many passwords do you need?\n"))
lengh = int(input("How long every password should be?\n"))
chars, min_len = definition_alphabet()

while min_len * 2 >= lengh:
    lengh = int(
        input("Lengh you're asking for is too short. Please, insert longer lengh.")
    )


for i in range(num):
    while 1:
        password = gen_password(lengh, chars)
        if is_valid(password, chars):
            print(password)
            break
