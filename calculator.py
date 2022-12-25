import tkinter as tk

class Calculator(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        # Create the widgets for the calculator
        self.display = tk.Label(self, text='0', font=('Helvetica', 24))
        self.display.pack(side='top', fill='both', expand=True)

        self.button_0 = tk.Button(self, text='0', command=lambda: self.button_pressed('0'))
        self.button_0.pack(side='left', fill='both', expand=True)

        self.button_1 = tk.Button(self, text='1', command=lambda: self.button_pressed('1'))
        self.button_1.pack(side='left', fill='both', expand=True)

        self.button_2 = tk.Button(self, text='2', command=lambda: self.button_pressed('2'))
        self.button_2.pack(side='left', fill='both', expand=True)

        self.button_3 = tk.Button(self, text='3', command=lambda: self.button_pressed('3'))
        self.button_3.pack(side='left', fill='both', expand=True)

        self.button_4 = tk.Button(self, text='4', command=lambda: self.button_pressed('4'))
        self.button_4.pack(side='left', fill='both', expand=True)

        self.button_5 = tk.Button(self, text='5', command=lambda: self.button_pressed('5'))
        self.button_5.pack(side='left', fill='both', expand=True)

        self.button_6 = tk.Button(self, text='6', command=lambda: self.button_pressed('6'))
        self.button_6.pack(side='left', fill='both', expand=True)

        self.button_7 = tk.Button(self, text='7', command=lambda: self.button_pressed('7'))
        self.button_7.pack(side='left', fill='both', expand=True)

        self.button_8 = tk.Button(self, text='8', command=lambda: self.button_pressed('8'))
        self.button_8.pack(side='left', fill='both', expand=True)

        self.button_9 = tk.Button(self, text='9', command=lambda: self.button_pressed('9'))
        self.button_9.pack(side='left', fill='both', expand=True)

        self.button_add = tk.Button(self, text='+', command=lambda: self.button_pressed('+'))
        self.button_add.pack(side='left', fill='both', expand=True)

        self.button_sub = tk.Button(self, text='-', command=lambda: self.button_pressed
