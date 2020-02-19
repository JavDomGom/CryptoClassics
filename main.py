import logging as log
from pathlib import Path
from tkinter import Tk, Menu, Scrollbar, END, IntVar, StringVar, \
                    PhotoImage, Frame, Grid, Label, Entry, Text, \
                    Checkbutton, Button, Toplevel
from tkinter import messagebox as MessageBox
from tkinter.ttk import Combobox, Style

log_path = 'log'
log_file = f'{log_path}/mascrypt.log'
log_format = '%(asctime)-15s [%(levelname)s] %(message)s'

# Create log dir if not exist.
Path(log_path).mkdir(parents=True, exist_ok=True)

# Configure logging function to save logs.
log.basicConfig(
    handlers=[log.FileHandler(log_file, 'a', 'utf-8')],
    level=log.DEBUG,
    format=log_format
)

program_name = 'CryptoClassics'
program_version = '0.1.0'
updated = 'Updated: 2020/02/19'
copyleft = 'Copyleft 2020, written by Javier Domínguez Gómez'
program_description = ''
about_text = '''This program is free software:  you can  redistribute it
and/or modify it under the terms of the GNU General
Public License as published by the Free Software
Foundation, either version 3 of the License.'''
gplv3_image = 'img/gplv3-127x51.png'


if __name__ == '__main__':
    log.info(f'Start {program_name} {program_version}.')
    # Create main UI program.
    root = Tk()
    root.title(f'{program_name} - {program_description}')
    root.resizable(1, 0)
    default_bg = root.cget('bg')

    # Create custom style for combobox.
    style = Style()
    style.theme_create('custom_style',
                       parent='default',
                       settings={'TCombobox':
                                 {'configure':
                                  {'selectforeground': 'black',
                                   'selectbackground': 'white'}
                                  }
                                 }
                       )
    style.theme_use('custom_style')
