from tkinter import *
from ui.menu_system import MenuSite
from ui.ceasar_ui import CaesarUI
from ui.vigenere_ui import VigenereUI
from ui.file_manager import FileManager
from ui.toolbar_site import ToolbarSite
from ui.editor_site import EditorSite
from ui.affine_ui import AffineUI
from ui.playfair_ui import PlayfairUI
from ui.hill_ui import HillUI


def init_ui(editor, menu, toolbar):
    caesar_ui = CaesarUI(editor.frame, menu, toolbar)
    vigenere_ui = VigenereUI(editor.frame, menu, toolbar)
    affine_ui = AffineUI(editor.frame, menu, toolbar)
    playfair_ui = PlayfairUI(editor.frame, menu, toolbar)
    hill_ui = HillUI(editor.frame, menu, toolbar)


def main():
    root = Tk()
    root.title("CrYpToGrApHy")
    root.iconbitmap("ui/res/icon.ico")
    root.minsize(1640, 680)
    root.maxsize(1640, 680)

    toolbar = ToolbarSite(root)
    menu = MenuSite(root, toolbar)
    file_menu = FileManager(menu)
    toolbar.init_actions()

    editor = EditorSite(root)

    init_ui(editor, menu, toolbar)

    root.mainloop()


if __name__ == '__main__':
    main()

