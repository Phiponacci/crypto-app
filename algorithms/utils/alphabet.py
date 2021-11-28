import string
import numpy as np

alphabet_str = string.ascii_lowercase

alphabet_len = len(alphabet_str)

alphabet = {}

for i, char in enumerate(alphabet_str):
    alphabet[char] = i
    alphabet[i] = char


def to_string(letters):
    return "".join(letters)


def to_letters(integers):
    letters = [alphabet[integer] for integer in integers]
    return letters


def to_integers(letters):
    integers = [alphabet[letter] for letter in letters]
    return integers


def clean_text(text):
    clean_txt = ""
    for letter in list(text.lower()):
        if alphabet_str.__contains__(letter):
            clean_txt += letter
    return clean_txt


def remove_letters_from_text(text, letters):
    clean_txt = text
    for letter in letters:
        if clean_txt.__contains__(letter):
            clean_txt = clean_txt.replace(letter, "")

    return clean_txt


def to_matrix(seq, row, col):
    text = clean_text(seq)
    matrix = np.array([[alphabet[el] for el in text[j * col:col * (j + 1)]] for j in range(row)])
    return matrix


def valid_square_matrix(seq):
    return int(np.sqrt(len(seq))) if int(np.sqrt(len(seq))) == np.sqrt(len(seq)) else 0


def split_text_by(seq, number, letter_added):
    to_add = (number - (len(seq) % number)) % number
    text = seq
    text += letter_added * to_add
    return [text[index:index + number] for index in range(0, len(text), number)]


def letter_add(letter1, letter2):
    integer1 = clean_key(letter1)
    integer2 = clean_key(letter2)
    addition = alphabet[(integer1 + integer2) % alphabet_len]
    return addition


def letter_sub(letter1, letter2):
    integer1 = clean_key(letter1)
    integer2 = clean_key(letter2)
    addition = alphabet[(integer1 + alphabet_len - integer2) % alphabet_len]
    return addition


def clean_key(key):
    k = key
    if isinstance(key, str):
        k = alphabet[key]
    k = k % alphabet_len
    return k


def remove_redundant(text):
    return "".join(dict.fromkeys(text))


def modinv(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return 1
