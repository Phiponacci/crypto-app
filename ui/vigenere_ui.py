from algorithms.vigenere import Vigenere
from tkinter import *

tag = "Vigenere Cipher"


class VigenereUI:
    def __init__(self, root, menu_site, toolbar_site):
        self.root = root
        self.menu_site = menu_site
        self.toolbar_site = toolbar_site
        self.algorithm = Vigenere()
        self.create_menu()

    def encrypt(self):
        plain_txt = self.txt_entry.get("1.0", END)
        key = self.key_entry.get()
        try:
            key = int(key)
        except:
            pass
        result = self.algorithm.encrypt(plain_txt, key)
        self.txt_out.config(state=NORMAL)
        self.txt_out.delete(1.0, END)
        self.txt_out.insert(1.0, result)
        self.txt_out.config(state=DISABLED)

    def decrypt(self):
        cipher_txt = self.txt_entry.get("1.0", END)
        key = self.key_entry.get()
        try:
            key = int(key)
        except:
            pass
        result = self.algorithm.decrypt(cipher_txt, key)
        self.txt_out.config(state=NORMAL)
        self.txt_out.delete(1.0, END)
        self.txt_out.insert(1.0, result)
        self.txt_out.config(state=DISABLED)

    def clear_fields(self):
        self.txt_out.config(state=NORMAL)
        self.txt_out.delete(1.0, END)
        self.txt_out.config(state=DISABLED)
        self.txt_entry.delete(1.0, END)
        self.key_entry.delete(0, END)

    def init_key_ui(self):
        self.key_label = Label(self.root, text="Key:")
        self.key_label.grid(row=1, column=0, padx=10, pady=10)

        self.key_entry = Entry(self.root)
        self.key_entry.grid(row=1, column=1, sticky=W, padx=10, pady=10)

    def init_input_ui(self):
        self.text_label = Label(self.root, text="Input:")
        self.text_label.grid(row=2, column=0, sticky=N, padx=10, pady=10)

        self.scroll_bar = Scrollbar(self.root)
        self.scroll_bar.grid(row=3, column=2, sticky=N + S)

        self.txt_entry = Text(self.root)
        self.txt_entry.grid(row=3, column=1)
        self.scroll_bar.config(command=self.txt_entry.yview)
        self.txt_entry.config(yscrollcommand=self.scroll_bar.set)

    def init_output_ui(self):
        self.output_label = Label(self.root, text="Output:")
        self.output_label.grid(row=2, column=3, sticky=N, padx=10, pady=10)

        self.scroll_bar_out = Scrollbar(self.root)
        self.scroll_bar_out.grid(row=3, column=5, sticky=N + S)

        self.txt_out = Text(self.root, state=DISABLED)
        self.txt_out.grid(row=3, column=4)
        self.scroll_bar_out.config(command=self.txt_out.yview)
        self.txt_out.config(yscrollcommand=self.scroll_bar_out.set)

    def init_actions(self):
        self.toolbar_site.set_encrypt_action(self.encrypt)
        self.toolbar_site.set_decrypt_action(self.decrypt)
        self.toolbar_site.set_clear_action(self.clear_fields)

    def init_ui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.label = Label(self.root, text=tag, font=("Consolas", 20, "italic", "bold"), fg="red")
        self.label.grid(row=0, column=0, columnspan=6)
        self.init_key_ui()
        self.init_input_ui()
        self.init_output_ui()
        self.init_actions()

    def create_menu(self):
        self.menu_site.add_item("Algorithm", tag, self.init_ui)
