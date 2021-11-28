from algorithms.playfair import Playfair
from algorithms.utils.alphabet import *
from tkinter import *
from tkinter import ttk

tag = "Playfair Cipher"


class PlayfairUI:
    def __init__(self, root, menu_site, toolbar_site):
        self.root = root
        self.menu_site = menu_site
        self.toolbar_site = toolbar_site
        self.algorithm = Playfair()
        self.create_menu()

    def from_letter_selected(self, event):
        from_ = self.from_combo.get()
        self.to_combo['values'] = tuple(list(alphabet_str.replace(from_, "") + " "))

    def encrypt(self):
        from_ = self.from_combo.get()
        to_ = self.to_combo.get()
        plain_txt = self.txt_entry.get("1.0", END)
        key = self.key_entry.get()
        self.algorithm.construct_key(key, from_, to_)
        result = self.algorithm.encrypt(plain_txt)
        self.txt_out.config(state=NORMAL)
        self.txt_out.delete(1.0, END)
        self.txt_out.insert(1.0, result)
        self.txt_out.config(state=DISABLED)

    def decrypt(self):
        cipher_txt = self.txt_entry.get("1.0", END)
        key = self.key_entry.get()
        self.algorithm.construct_key(key, "w", "")
        result = self.algorithm.decrypt(cipher_txt)
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
        self.from_combo.set("")
        self.to_combo.set("")
        self.to_combo['values'] = ("")

    def init_key_ui(self):
        self.key_frame = Frame(self.root)
        self.key_label = Label(self.root, text="Key:")
        self.key_label.grid(row=1, column=0, padx=10, pady=10)

        self.key_entry = Entry(self.key_frame)
        self.key_entry.grid(row=0, column=1, sticky=W, padx=10, pady=10)

    def init_letter_replacement_ui(self):
        self.from_label = Label(self.key_frame, text="from:")
        self.from_combo = ttk.Combobox(self.key_frame, width=15, state="readonly")
        self.from_combo['values'] = tuple(list(alphabet_str))
        self.from_label.grid(row=0, column=2)
        self.from_combo.grid(row=0, column=3)
        self.from_combo.bind("<<ComboboxSelected>>", self.from_letter_selected)
        self.to_label = Label(self.key_frame, text="to:")
        self.to_combo = ttk.Combobox(self.key_frame, state="readonly")
        self.to_label.grid(row=0, column=4)

        self.to_combo.grid(row=0, column=5)

        self.key_frame.grid(row=1, column=1, sticky=W)

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
        self.init_letter_replacement_ui()
        self.init_input_ui()
        self.init_output_ui()
        self.init_actions()

    def create_menu(self):
        self.menu_site.add_item("Algorithm", tag, self.init_ui)
