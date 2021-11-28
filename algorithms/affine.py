from algorithms.utils.alphabet import *

tag = "Affine"


class Affine:
    def encrypt(self, plain_text, key):
        txt = clean_text(plain_text)
        t1, t2 = key
        a = clean_key(t1)
        b = clean_key(t2)
        integers = [(a * alphabet[letter] + b) % alphabet_len for letter in txt]
        cipher_text = to_string(to_letters(integers))
        return cipher_text

    def decrypt(self, cipher_text, key):
        txt = clean_text(cipher_text)
        t1, t2 = key
        a = clean_key(t1)
        b = clean_key(t2)
        integers = [(((alphabet[y] + alphabet_len - b) % alphabet_len) * modinv(a, alphabet_len))%alphabet_len for y in txt]
        plain_text = to_string(to_letters(integers))
        return plain_text
