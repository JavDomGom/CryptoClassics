from tkinter import Toplevel, Frame, Text, Scrollbar, Button, Label


class PureDisplacement(Frame):

    def __init__(self, master, name):
        super().__init__(master)
        self.master = master
        self.name = name
        self.padx = 3
        self.pady = 3
        self.font = ('Courier New', 10)
        self.pack()
        self._show()

    def _show(self):
        tpl_pd = Toplevel(self.master)
        tpl_pd.resizable(1, 1)
        tpl_pd.title(f'{self.name}')

        # Top frame.
        frm_0 = Frame(
            tpl_pd,
            bg='#ff0000',
            bd=5
        )
        frm_0.pack(fill='both', side='top')
        frm_0.grid_columnconfigure(0, weight=1)
        frm_0.grid_columnconfigure(1, weight=1)
        frm_0.grid_columnconfigure(2, weight=1)
        frm_0.grid_columnconfigure(3, weight=1)
        frm_0.grid_columnconfigure(4, minsize=30)

        btn_crypt = Button(
            frm_0,
            text='Crypt',
            command=self.master.destroy
        )
        btn_crypt.grid(
            row=0, column=0, padx=self.padx, pady=self.pady, sticky='w'
        )

        btn_decrypt = Button(
            frm_0,
            text='Decrypt',
            command=self.master.destroy
        )
        btn_decrypt.grid(
            row=0, column=1, padx=self.padx, pady=self.pady, sticky='w'
        )

        btn_key = Button(
            frm_0,
            text='Key',
            command=self.master.destroy
        )
        btn_key.grid(
            row=0, column=2, padx=self.padx, pady=self.pady, sticky='w'
        )

        btn_help = Button(
            frm_0,
            text='Help',
            command=self.master.destroy
        )
        btn_help.grid(
            row=0, column=3, padx=self.padx, pady=self.pady, sticky='w'
        )

        lbl_load = Label(
            frm_0,
            text='Load:',
            anchor='e'
        )
        lbl_load.grid(
            row=0, column=4, padx=self.padx, pady=self.pady, sticky='e'
        )

        btn_load_example = Button(
            frm_0,
            text='Test example',
            command=self.master.destroy
        )
        btn_load_example.grid(
            row=0, column=5, padx=self.padx, pady=self.pady, sticky='e'
        )

        # Middle frame.
        frm_1 = Frame(
            tpl_pd,
            bg='#00ff00',
            bd=5
        )
        frm_1.pack(expand=True, fill='both')
        frm_1.grid_propagate(True)
        frm_1.grid_columnconfigure(0, weight=1)
        frm_1.grid_rowconfigure(0, weight=1)

        lbl_input = Label(
            frm_1,
            text='Input:',
            justify='right'
        )
        lbl_input.grid(
            row=0, column=0, padx=self.padx, pady=self.pady, sticky='we'
        )

        txt_input = Text(
            frm_1,
            width=75,
            height=3,
            font=self.font,
            state='normal'
        )
        scrollb_input = Scrollbar(frm_1)
        scrollb_input.config(command=txt_input.yview)
        txt_input.config(yscrollcommand=scrollb_input.set)
        scrollb_input.grid(row=0, column=2, pady=self.pady, sticky='nsew')
        txt_input.grid(row=0, column=1, pady=self.pady, sticky='nsew')
