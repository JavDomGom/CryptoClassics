import logging as log
from pathlib import Path
from tkinter import Toplevel, Frame, Menu, PhotoImage, Button, Label
from resources.showDoc import ShowDoc as sd
from resources.pureDisplacement import PureDisplacement as pd


class Application(Frame):

    def __init__(self, master, name, version, description):
        super().__init__(master)
        self.master = master
        self.fg_color = '#000000'
        self.name = name
        self.version = version
        self.updated = 'Updated: 2020/02/25'
        self.copyleft = 'Copyleft 2020, written by Javier Domínguez Gómez'
        self.description = description
        self.about = '''This program is free software: you can redistribute it
and/or modify it under the terms of the GNU General
Public License as published by the Free Software
Foundation, either version 3 of the License.'''
        self.gplv3_image = 'img/gplv3-127x51.png'
        self.padx = 3
        self.pady = 3
        self.font = ('Courier New', 10)
        self.license = (
            'LICENSE',
            f'{self.name} v{self.version} License'
        )
        self.log_path = 'log'
        self.log_file = f'{self.log_path}/cryptoclassics.log'
        self.log_format = '%(asctime)-15s [%(levelname)s] %(message)s'

        self.pack()
        self._configure_logs()
        self._create_menubar()
        self._create_parent_frame()

        log.info(f'Start {self.name} {self.version}.')

    def _configure_logs(self):
        # Create log dir if not exist.
        Path(self.log_path).mkdir(parents=True, exist_ok=True)

        # Configure logging function to save logs.
        log.basicConfig(
            handlers=[log.FileHandler(self.log_file, 'a', 'utf-8')],
            level=log.DEBUG,
            format=self.log_format
        )

    def _build_cryptosystem(self, cs):
        print(cs)
        if cs == 'Pure displacement':
            pd(self.master, cs)

    def _create_menubar(self):
        # Build menubar.
        menubar = Menu(self.master, fg=self.fg_color, borderwidth=1)
        self.master.config(menu=menubar)

        # Build Cryptosystems menu.
        cryptosystems_list = [
            'Pure displacement',
            'Pure decimation',
            'Affine cipher',
            'Gronsfeld',
            'Vigenère',
            'Continuous key',
            'Beaufort',
            'Hill',
            'Playfair',
            'Transposition',
            'Binary Vernam',
            'Enigma'
        ]

        cryptosystems_menu = Menu(menubar, tearoff=0)

        for i, cs in enumerate(cryptosystems_list):
            if i in (3, 7, 9, 11):
                cryptosystems_menu.add_separator()

            cryptosystems_menu.add_command(
                label=f'{cs}',
                command=lambda cs=cs: self._build_cryptosystem(cs)
            )

        # Build Tools menu.
        tools_list = [
            'Primality test',
            'Modular arithmetic',
            'GDC and LCM',
            'Reduced Residue System',
            'Euler\'s totient function',
            'Modular multiplicative inverse',
            'Matrices',
            'Language statistics',
            'Text grouping'
        ]

        tools_menu = Menu(menubar, tearoff=0)

        for i, t in enumerate(tools_list):
            if i in (7, 8):
                tools_menu.add_separator()

            tools_menu.add_command(
                label=f'{t}',
                command=self.master.destroy
            )

        # Build Options menu.
        options_list = [
            'Spanish Z27 (A-Z)',
            'Spanish Z37 (A-Z, 0-9)',
            'English Z26 (A-Z)',
            'English Z36 (A-Z, 0-9)',
            'ASCII 191'
        ]

        options_menu = Menu(menubar, tearoff=0)
        for op in options_list:
            options_menu.add_command(
                label=f'{op}',
                command=self.master.destroy
            )

        # Build Help menu.
        help_menu = Menu(menubar, tearoff=0)
        help_menu.add_command(
            label='View license',
            command=lambda: sd(self.master, self.license)
        )
        help_menu.add_separator()
        help_menu.add_command(
            label=f'About {self.name} {self.version}',
            command=self._about
        )

        # Build menubar with all previously menus.
        menubar.add_cascade(label='Cryptosystems', menu=cryptosystems_menu)
        menubar.add_cascade(label='Tools', menu=tools_menu)
        menubar.add_cascade(label='Options', menu=options_menu)
        menubar.add_cascade(label='Help', menu=help_menu)

    def _create_parent_frame(self):
        # Build parent frame.
        frm = Frame(
            self.master,
            bd=5,
            width=700,
            height=350
        )
        frm.pack(side='left', expand=True, fill='both')

    def _about(self):
        """ This function shows information about the program."""
        tpl_about = Toplevel(self.master)
        tpl_about.resizable(0, 0)
        tpl_about.title(f'About {self.name}')

        tpl_msg = Label(
            tpl_about,
            width=35,
            text=f'{self.name} v{self.version}\n{self.updated}\
\n\n{self.copyleft}',
            justify='center'
        )
        tpl_msg.grid(
            row=0, column=0, padx=self.padx, pady=self.pady, sticky='we'
        )

        lbl_gplv3 = Label(
            tpl_about,
            text=self.about,
            justify='center'
        )
        lbl_gplv3.grid(row=1, column=0, padx=self.padx+15, pady=self.pady)

        img_gplv3 = PhotoImage(file=self.gplv3_image)

        lbl_img_gplv3 = Label(tpl_about)
        lbl_img_gplv3.grid(row=2, column=0, padx=self.padx, pady=self.pady)
        lbl_img_gplv3.configure(image=img_gplv3)
        lbl_img_gplv3.image = img_gplv3

        tpl_button = Button(
            tpl_about,
            anchor='center',
            text='Close',
            command=tpl_about.destroy
        )
        tpl_button.grid(row=3, column=0, padx=self.padx, pady=self.pady)
