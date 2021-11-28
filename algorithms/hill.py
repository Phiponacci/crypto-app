from algorithms.utils.alphabet import *


class Hill:
    def encrypt(self, text, key, letter_to_add):
        cipher_text = ""
        n = valid_square_matrix(clean_text(key))
        if n == 0:
            return ""
        plain_text = split_text_by(clean_text(text), n, letter_to_add)
        matrix = to_matrix(key, n, n)
        for el in plain_text:
            _, cipher_part = np.divmod(np.matmul(matrix, np.array(to_integers(el))), alphabet_len)
            cipher_text += to_string(to_letters(cipher_part.tolist()))
        return cipher_text

    def decrypt(self, text, key, letter_to_add):
        plain_text = ""
        n = valid_square_matrix(clean_text(key))
        if n == 0:
            return ""
        cipher_text = split_text_by(clean_text(text), n, letter_to_add)
        matrix = to_matrix(key, n, n)
        det = np.linalg.det(matrix)
        inv = np.linalg.inv(matrix)
        inv_matrix = inv * det * modinv(int(det), alphabet_len)
        _, inv_mod_matrix = np.divmod(inv_matrix, alphabet_len)
        inv_mod_matrix = np.around(inv_mod_matrix).astype(int)

        for el in cipher_text:
            _, plain_part = np.divmod(np.matmul(inv_mod_matrix, np.array(to_integers(el))), alphabet_len)
            plain_text += to_string(to_letters(plain_part.tolist()))

        return plain_text
