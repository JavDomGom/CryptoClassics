import logging as log
from tkinter import Toplevel, Frame, Text, Scrollbar, END


class ShowDoc(Frame):

    def __init__(self, master, doc):
        super().__init__(master)
        self.master = master
        self.doc = doc
        self.pady = 3
        self.font = ('Courier New', 10)
        self.pack()
        self._show()

    def _show(self):
        """ This function opens a pop-up window and shows a document
        with information.

        Attributes:
            :doc: Document to open and show in a new window.
        """
        tpl_table = Toplevel(self.master)
        tpl_table.resizable(1, 1)
        tpl_table.title(f'{self.doc[1]}')

        frm_tpl = Frame(
            tpl_table,
            bd=5
        )
        frm_tpl.pack(expand=True, fill='both')
        frm_tpl.grid_propagate(True)
        frm_tpl.grid_columnconfigure(0, weight=1)
        frm_tpl.grid_rowconfigure(0, weight=1)

        txt_doc = Text(
            frm_tpl,
            font=self.font,
            state='normal'
        )
        scrollb = Scrollbar(frm_tpl)
        scrollb.config(command=txt_doc.yview)
        txt_doc.config(yscrollcommand=scrollb.set)
        scrollb.grid(row=0, column=1, pady=self.pady, sticky='nsew')
        txt_doc.grid(row=0, column=0, pady=self.pady, sticky='nsew')

        with open(self.doc[0], 'r') as f:
            log.debug(f'Showing information from "{self.doc[0]}".')
            txt_doc.insert(
                END,
                f.read().rstrip()
            )
