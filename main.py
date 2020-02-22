from resources.application import Application
from tkinter import Tk

name = 'CryptoClassics'
version = '0.1.0'
description = 'Tools for classical cryptography'

if __name__ == '__main__':
    # Create main UI program.
    root = Tk()
    root.title(f'{name} v{version} - {description}')
    root.resizable(1, 1)
    default_bg = root.cget('bg')

    app = Application(root, name, version, description)
    app.mainloop()
