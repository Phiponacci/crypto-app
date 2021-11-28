from algorithms.utils.alphabet import *


class Vigenere:

    def encrypt(self, plain_text, key):
        txt = clean_text(plain_text)
        k = clean_text(key)
        key_len = len(k)
        cipher_txt = ""
        for i, letter in enumerate(list(txt)):
            cipher_letter = letter_add(letter, k[i % key_len])
            cipher_txt += cipher_letter
        return cipher_txt

    def decrypt(self, cipher_text, key):
        txt = clean_text(cipher_text)
        k = clean_text(key)
        key_len = len(k)
        plain_text = ""
        for i, letter in enumerate(list(txt)):
            cipher_letter = letter_sub(letter, k[i % key_len])
            plain_text += cipher_letter
        return plain_text
