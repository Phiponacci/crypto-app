from tkinter import Menu


class MenuSite:
    def __init__(self, root, toolbar_site):
        self.root = root
        self.sub_menus = {}
        self.toolbar = toolbar_site
        self.root_menu = Menu(self.root)
        self.root.config(menu=self.root_menu)

    def add_item(self, menu_label, item, action):
        if self.sub_menus.__contains__(menu_label):
            self.sub_menus[menu_label].add_command(label=item, command=action)
        else:
            sub_menu = Menu(self.root_menu)  # sub menu
            self.root_menu.add_cascade(label=menu_label, menu=sub_menu)
            sub_menu.add_command(label=item, command=action)
            self.sub_menus[menu_label] = sub_menu
