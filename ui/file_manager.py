from tkinter import *
from tkinter import ttk

tag = "File"

class FileManager:
    def __init__(self, menu_site):
        self.menu_site = menu_site
        self.create_menu()

    def open_file(self):
        pass

    def save_as(self):
        pass


    def quit(self):
        exit(0)

    def init_ui(self):
        print("init file menu")

    def create_menu(self):
        self.menu_site.add_item(tag, "New...", self.init_ui)
        self.menu_site.add_item(tag, "Open...", self.open_file)
        self.menu_site.add_item(tag, "Save As...", self.save_as)
        self.menu_site.add_item(tag, "Exit", self.quit)

