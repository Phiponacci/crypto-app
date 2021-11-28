from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo


info = "Cryptography algorithms \n\n" \
       "[Author: Leo Phiponacci]\n\n" \
       "Computer Engineer"


class ToolbarSite:
    def __init__(self, root):
        self.toolbar = Frame(root, bg="#dddddd")
        self.toolbar.pack(side=TOP, fill=X)
        self.root = root

    def init_actions(self):
        #self.set_new_file_btn()
        #self.set_open_btn()
        #self.set_save_as_btn()
        self.set_clear_btn()
        self.set_encrypt_btn()
        self.set_decrypt_btn()
        self.set_exit_btn()
        self.set_info_btn()

    def set_new_file_btn(self):
        self.new_img = PhotoImage(file="ui/res/new_file.png")
        self.new_btn = ttk.Button(self.toolbar, image=self.new_img)
        self.new_btn.pack(side=LEFT, padx=2, pady=2)

    def set_open_btn(self):
        self.open_img = PhotoImage(file="ui/res/file.png")
        self.open_btn = ttk.Button(self.toolbar, image=self.open_img)
        self.open_btn.pack(side=LEFT, padx=2, pady=2)

    def set_clear_btn(self):
        self.clear_img = PhotoImage(file="ui/res/clearall.png")
        self.clear = ttk.Button(self.toolbar, image=self.clear_img)
        self.clear.pack(side=LEFT, padx=2, pady=2)

    def set_exit_btn(self):
        self.exit_img = PhotoImage(file="ui/res/exit.png")
        self.exit_btn = ttk.Button(self.toolbar, image=self.exit_img, command=exit)
        self.exit_btn.pack(side=RIGHT, padx=2, pady=2)

    def set_encrypt_btn(self):
        self.encrypt_img = PhotoImage(file="ui/res/lock.png")
        self.encrypt = ttk.Button(self.toolbar, image=self.encrypt_img)
        self.encrypt.pack(side=LEFT, padx=2, pady=2)

    def set_decrypt_btn(self):
        self.decrypt_img = PhotoImage(file="ui/res/unlock.png")
        self.decrypt = ttk.Button(self.toolbar, image=self.decrypt_img)
        self.decrypt.pack(side=LEFT, padx=2, pady=2)

    def set_save_as_btn(self):
        self.save_img = PhotoImage(file="ui/res/save_as.png")
        self.saveas = ttk.Button(self.toolbar, image=self.save_img)
        self.saveas.pack(side=LEFT, padx=2, pady=2)

    def display_info(self):
        showinfo("Info", info)

    def set_info_btn(self):
        self.info_img = PhotoImage(file="ui/res/info.png")
        self.info_btn = ttk.Button(self.toolbar, image=self.info_img, command=self.display_info)
        self.info_btn.pack(side=RIGHT, padx=2, pady=2)

    def define_action(self, action_label, action):
        pass

    def set_encrypt_action(self, action):
        self.encrypt.configure(command=action)

    def set_decrypt_action(self, action):
        self.decrypt.configure(command=action)

    def set_clear_action(self, action):
        self.clear.configure(command=action)
