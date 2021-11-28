from tkinter import ttk
from algorithms.utils.alphabet import *
from algorithms.hill import Hill
from tkinter import *

tag = "Hill Cipher"


class HillUI:
    def __init__(self, root, menu_site, toolbar_site):
        self.root = root
        self.menu_site = menu_site
        self.toolbar_site = toolbar_site
        self.algorithm = Hill()
        self.create_menu()

    def encrypt(self):
        plain_txt = self.txt_entry.get("1.0", END)
        key = self.key_entry.get()
        letter_to_add = self.added_letter.get()
        result = self.algorithm.encrypt(plain_txt, key, letter_to_add)
        self.txt_out.config(state=NORMAL)
        self.txt_out.delete(1.0, END)
        self.txt_out.insert(1.0, result)
        self.txt_out.config(state=DISABLED)

    def decrypt(self):
        cipher_txt = self.txt_entry.get("1.0", END)
        key = self.key_entry.get()
        letter_to_add = self.added_letter.get()
        result = self.algorithm.decrypt(cipher_txt, key, letter_to_add)
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
        self.utils_ui = Frame(self.root)

        self.key_label = Label(self.root, text="Key:")
        self.key_label.grid(row=1, column=0, padx=10, pady=10)

        self.key_entry = Entry(self.utils_ui)
        self.key_entry.grid(row=0, column=1, sticky=W, padx=10, pady=10)

    def init_added_letter_ui(self):
        self.added_letter_label = Label(self.utils_ui, text="Completion letter: ")
        self.added_letter_label.grid(row=0, column=2, padx=10, pady=10)

        self.added_letter = ttk.Combobox(self.utils_ui, width=15, state="readonly")
        self.added_letter['values'] = tuple(list(alphabet_str))
        self.added_letter.grid(row=0, column=3, padx=10, pady=10)

        self.utils_ui.grid(row=1, column=1, sticky=W)

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
        self.init_added_letter_ui()
        self.init_input_ui()
        self.init_output_ui()
        self.init_actions()

    def create_menu(self):
        self.menu_site.add_item("Algorithm", tag, self.init_ui)
