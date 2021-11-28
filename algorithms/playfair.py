from algorithms.utils.alphabet import *


class Playfair:
    def construct_key(self, key, from_, to_):
        self.from_, self.to_ = from_, to_
        k = remove_redundant(clean_text(key)).replace(from_, to_)
        rest = remove_letters_from_text(alphabet_str, k).replace(from_, to_)
        if k.__contains__(to_):
            rest = rest.replace(to_, "")
        k += rest
        index = 0
        self.key = self.matrix(5, 5, 0)
        for i in range(0, 5):
            for j in range(0, 5):
                self.key[i][j] = k[index]
                index += 1

    def get_index(self, c):
        loc = list()
        for i, j in enumerate(self.key):
            for k,l in enumerate(j):
                if c == l:
                    loc.append(i)
                    loc.append(k)
                    return loc

    def encrypt(self, text):
        plain_txt = clean_text(text).replace(self.from_, self.to_)
        if len(plain_txt) % 2 == 1:
            plain_txt += "x"
        i = 0
        for s in range(0, len(plain_txt) + 1, 2):
            if s < len(plain_txt) - 1:
                if plain_txt[s] == plain_txt[s + 1]:
                    plain_txt = plain_txt[:s + 1] + 'x' + plain_txt[s + 1:]
        cipher_text = ""
        while i < len(plain_txt):
            loc = self.get_index(plain_txt[i])
            loc1 = self.get_index(plain_txt[i + 1])
            if loc[1] == loc1[1]:
                cipher_text += "{}{}".format(self.key[(loc[0] + 1) % 5][loc[1]], self.key[(loc1[0] + 1) % 5][loc1[1]]) + " "
            elif loc[0] == loc1[0]:
                cipher_text += "{}{}".format(self.key[loc[0]][(loc[1] + 1) % 5], self.key[loc1[0]][(loc1[1] + 1) % 5]) + " "
            else:
                cipher_text += "{}{}".format(self.key[loc[0]][loc1[1]], self.key[loc1[0]][loc[1]]) + " "
            i = i + 2
        return cipher_text


    def decrypt(self, text):
        cipher_txt = clean_text(text).replace(self.from_, self.to_)
        if len(cipher_txt) % 2 == 1:
            cipher_txt += "x"
        plain_text = ""

        i = 0
        while i < len(cipher_txt):
            loc = self.get_index(cipher_txt[i])
            loc1 = self.get_index(cipher_txt[i + 1])
            if loc[1] == loc1[1]:
                plain_text += "{}{}".format(self.key[(loc[0] - 1) % 5][loc[1]], self.key[(loc1[0] - 1) % 5][loc1[1]])
            elif loc[0] == loc1[0]:
                plain_text += "{}{}".format(self.key[loc[0]][(loc[1] - 1) % 5], self.key[loc1[0]][(loc1[1] - 1) % 5])
            else:
                plain_text += "{}{}".format(self.key[loc[0]][loc1[1]], self.key[loc1[0]][loc[1]])
            i = i + 2
        return plain_text

    def matrix(self, x, y, initial):
        return [[initial for i in range(x)] for j in range(y)]
