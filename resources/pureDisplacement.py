import json
import re
from unicodedata import normalize
from tkinter import Toplevel, Frame, Text, Scrollbar, Button, Label, IntVar, \
                    filedialog
from tkinter.ttk import Progressbar, Separator, Combobox


class PureDisplacement(Frame):

    def __init__(self, master, name, alpha_tuple):
        super().__init__(master)
        self.master = master
        self.name = name
        self.alpha_title = alpha_tuple[0].get()
        self.alpha_file = alpha_tuple[1].get()
        self.alpha_regex = alpha_tuple[2].get()
        self.padx = 3
        self.pady = 3
        self.txt_width = 50
        self.txt_height = 3
        self.font = ('Courier New', 10)
        self.key = IntVar()
        self.pack()
        self._show()

    def _read_alpha_file(self, file):
        try:
            with open(file, 'r') as f:
                alpha = f.read().rstrip()
                alpha = json.loads(alpha)
                return alpha
        except FileNotFoundError:
            return False

    def _get_regex(self, input):
        return re.sub(
            r'([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+',
            r'\1',
            normalize('NFD', input), 0, re.I
        )

    def _crypt(self, input, txt_output, progressBar):
        alpha = self._read_alpha_file(self.alpha_file)
        max_size = len(alpha)
        progressBar['maximum'] = len(input)
        output = ''
        k = self.key.get()
        for i, c in enumerate(re.sub(
            self.alpha_regex,
            '',
            self._get_regex(input)
        ).lower()):
            # time.sleep(0.005)
            progressBar['value'] = i + 1
            progressBar.update()
            new_position = alpha[c] + k
            if new_position > max_size:
                new_position -= max_size
            for kz, vz in alpha.items():
                if new_position == vz:
                    output += kz

        txt_output.delete(1.0, 'end')
        txt_output.insert('end', output.upper())

    def _decrypt(self, input, txt_output):
        alpha = self._read_alpha_file(self.alpha_file)
        max_size = len(alpha)
        output = ''
        k = self.key.get()
        for c in re.sub(
            self.alpha_regex,
            '',
            self._get_regex(input)
        ).lower():
            new_position = alpha[c] - k
            if new_position > max_size:
                new_position -= max_size
            for kz, vz in alpha.items():
                if new_position == vz:
                    output += kz

        txt_output.delete(1.0, 'end')
        txt_output.insert('end', output.upper())

    def _load_file(self, txt_input, txt_output):
        file_types = [('All files', '*')]
        dialog = filedialog.Open(self, filetypes=file_types)
        filename = dialog.show()

        if filename != '':
            with open(filename, 'r') as f:
                txt_input.delete(1.0, 'end')
                txt_output.delete(1.0, 'end')
                txt_input.insert('end', f.read())

    def _show(self):
        tpl_pd = Toplevel(self.master)
        tpl_pd.resizable(0, 0)
        tpl_pd.title(f'{self.name} - {self.alpha_title}')

        # Top frame.
        frm_0 = Frame(
            tpl_pd
        )
        frm_0.pack(side='top', fill='both')

        # Top frame left.
        frm_0L = Frame(
            frm_0,
            bd=5
        )
        frm_0L.pack(side='left', fill='both')
        frm_0L.grid_columnconfigure(0, weight=1)
        frm_0L.grid_columnconfigure(0, minsize=30)

        btn_crypt = Button(
            frm_0L,
            text='Crypt',
            command=lambda: self._crypt(
                txt_input.get(1.0, 'end').rstrip().replace(' ', ''),
                txt_output,
                progressBar
            )
        )
        btn_crypt.grid(
            row=0, column=0, padx=self.padx, pady=self.pady, sticky='w'
        )

        btn_decrypt = Button(
            frm_0L,
            text='Decrypt',
            command=lambda: self._decrypt(
                txt_input.get(1.0, 'end').rstrip().replace(' ', ''),
                txt_output
            )
        )
        btn_decrypt.grid(
            row=0, column=1, padx=self.padx, pady=self.pady, sticky='w'
        )

        lbl_key = Label(
            frm_0L,
            text='Key:',
            anchor='e'
        )
        lbl_key.grid(
            row=0, column=2, padx=self.padx, pady=self.pady, sticky='e'
        )

        def set_key(event):
            self.key.set(cb_key.get())

        cb_key = Combobox(frm_0L, state='readonly')
        cb_key['values'] = [i for i in range(10)]

        cb_key.current(0)
        cb_key.bind(
            '<<ComboboxSelected>>', set_key
        )
        cb_key.grid(
            row=0, column=3, padx=self.padx, pady=self.pady, sticky='ns'
        )

        btn_help = Button(
            frm_0L,
            text='Help',
            command=self.master.destroy
        )
        btn_help.grid(
            row=0, column=4, padx=self.padx, pady=self.pady, sticky='w'
        )

        # Top frame right.
        frm_0L = Frame(
            frm_0,
            bd=5
        )
        frm_0L.pack(side='right', fill='both')
        frm_0L.grid_columnconfigure(0, weight=1)
        frm_0L.grid_columnconfigure(0, minsize=30)

        lbl_load = Label(
            frm_0L,
            text='Load:',
            anchor='e'
        )
        lbl_load.grid(
            row=0, column=0, padx=self.padx, pady=self.pady, sticky='e'
        )

        btn_load_example = Button(
            frm_0L,
            text='Test example',
            command=self.master.destroy
        )
        btn_load_example.grid(
            row=0, column=1, padx=self.padx, pady=self.pady, sticky='e'
        )

        sep = Separator(tpl_pd, orient='horizontal')
        sep.pack(anchor='nw', fill='x')

        # Middle frame.
        frm_1 = Frame(
            tpl_pd,
            bd=5
        )
        frm_1.pack(expand=True, fill='both')
        frm_1.grid_propagate(True)
        frm_1.grid_columnconfigure(0, weight=1)
        frm_1.grid_rowconfigure(0, weight=1)
        frm_1.grid_rowconfigure(1, weight=1)

        lbl_input = Label(
            frm_1,
            text='Input:',
            anchor='w'
        )
        lbl_input.grid(
            row=0, column=0, padx=self.padx, pady=self.pady, sticky='ew'
        )

        txt_input = Text(
            frm_1,
            width=self.txt_width,
            height=self.txt_height,
            font=self.font,
            state='normal'
        )
        scrollb_input = Scrollbar(frm_1)
        scrollb_input.config(command=txt_input.yview)
        txt_input.config(yscrollcommand=scrollb_input.set)
        scrollb_input.grid(row=0, column=2, pady=self.pady+5, sticky='nsew')
        txt_input.grid(row=0, column=1, pady=self.pady+5, sticky='nsew')

        lbl_open_input_file = Label(
            frm_1,
            text='Input file:'
        )
        lbl_open_input_file.grid(
            row=0, column=3, padx=self.padx, pady=self.pady+5, sticky='n'
        )

        btn_open_input_file = Button(
            frm_1,
            text='Open',
            command=lambda: self._load_file(txt_input, txt_output)
        )
        btn_open_input_file.grid(
            row=0, column=3, padx=self.padx, pady=self.pady+5, sticky='s'
        )

        lbl_output = Label(
            frm_1,
            text='Output:',
            anchor='w'
        )
        lbl_output.grid(
            row=1, column=0, padx=self.padx, pady=self.pady, sticky='ew'
        )

        txt_output = Text(
            frm_1,
            width=self.txt_width,
            height=self.txt_height,
            font=self.font,
            state='normal'
        )
        scrollb_output = Scrollbar(frm_1)
        scrollb_output.config(command=txt_output.yview)
        txt_output.config(yscrollcommand=scrollb_output.set)
        scrollb_output.grid(row=1, column=2, pady=self.pady+5, sticky='nsew')
        txt_output.grid(row=1, column=1, pady=self.pady+5, sticky='nsew')

        lbl_save_output_file = Label(
            frm_1,
            text='Output file:'
        )
        lbl_save_output_file.grid(
            row=1, column=3, padx=self.padx, pady=self.pady+5, sticky='n'
        )

        btn_save_output_file = Button(
            frm_1,
            text='Save',
            command=self.master.destroy
        )
        btn_save_output_file.grid(
            row=1, column=3, padx=self.padx, pady=self.pady+5, sticky='s'
        )

        # Bottom frame.
        frm_2 = Frame(
            tpl_pd,
            bd=5
        )
        frm_2.pack(expand=True, fill='both')
        frm_2.grid_propagate(True)
        frm_2.grid_columnconfigure(0, weight=1)
        frm_2.grid_rowconfigure(0, weight=1)

        lbl_input = Label(
            frm_2,
            text='Ready:',
            anchor='w'
        )
        lbl_input.grid(
            row=0, column=0, padx=self.padx, pady=self.pady, sticky='w'
        )

        progressBar = Progressbar(
            frm_2,
            orient='horizontal',
            mode='determinate',
            length=500
        )
        progressBar.place(anchor='sw', x=1, bordermode="outside")
        progressBar.grid(row=0, column=1, pady=self.pady, sticky='w')
