from algorithms.utils.alphabet import *


class Caesar:
    def encrypt(self, plain_text, key):
        txt = clean_text(plain_text)
        k = clean_key(key)
        integers = [(k + alphabet[letter]) % alphabet_len for letter in txt]
        cipher_text = to_string(to_letters(integers))
        return cipher_text

    def decrypt(self, cipher_text, key):
        txt = clean_text(cipher_text)
        k = clean_key(key)
        integers = [(alphabet[letter] + alphabet_len - k) % alphabet_len for letter in txt]
        plain_text = to_string(to_letters(integers))
        return plain_text
