import tkinter as tk
from tkinter.constants import INSERT
from typing import Sized
from tkinter import scrolledtext
from dka_class import DKA

class SimpleTableInput(tk.Frame):
    def __init__(self, parent, rows, columns):
        tk.Frame.__init__(self, parent)

        self._entry = {}
        self.rows = rows
        self.columns = columns

        # register a command to use for validation
        vcmd = (self.register(self._validate), "%P")

        # create the table of widgets
        for row in range(self.rows):
            for column in range(self.columns):
                index = (row, column)
                e = tk.Entry(self, validate="key", validatecommand=vcmd)
                e.grid(row=row, column=column, stick="nsew")
                self._entry[index] = e
        # adjust column weights so they all expand equally
        for column in range(self.columns):
            self.grid_columnconfigure(column, weight=1)
        # designate a final, empty row to fill up any extra space
        self.grid_rowconfigure(rows, weight=1)

    def get(self):
        '''Return a list of lists, containing the data in the table'''
        result = []
        for row in range(self.rows):
            current_row = []
            for column in range(self.columns):
                index = (row, column)
                current_row.append(self._entry[index].get())
            result.append(current_row)
        return result

    def _validate(self, P):
        '''Perform input validation. 

        Allow only an empty value, or a value that can be converted to a float
        '''
        #if P.strip() == "":
        #    return True

        #try:
        #    f = float(P)
        #except ValueError:
        #    self.bell()
        #    return False
        return True

class Example(tk.Frame):
    spin = 0
    resize = 0
    start = 0 
    txt_input_alphabet = 0
    txt_label_alphabet = 0
    txt_input_chain = 0
    txt_label_chain = 0
    txt_input_final_state = 0
    txt_label_final_state = 0
    label_spin = 0
    spin_init = 0
    output_result = 0

    last_spin_number = int(0)

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.last_spin_number = int(3)

        self.spin = tk.Spinbox(self, from_=3, to=15, width=5)
        self.start = tk.Button(self, text="Start", command=self.on_start)
        self.resize = tk.Button(self, text="Resize", command=self.on_resize)
        self.txt_input_alphabet = tk.Entry(self,width=40)
        self.txt_label_alphabet = tk.Label(self, text="Enter characters of the alphabet separated by a space:")
        
        self.txt_input_chain = tk.Entry(self,width=40)
        self.txt_label_chain = tk.Label(self, text="Enter the chain:")
        
        self.txt_input_final_state = tk.Entry(self,width=40)
        self.txt_label_final_state = tk.Label(self, text="Enter the numbers of the end states separated by a space:")
        self.output_result = scrolledtext.ScrolledText(self, width=40, height=10) 
        self.label_spin = tk.Label(self, text="Select init state") 
        self.spin_init = tk.Spinbox(self, from_=0, to=self.last_spin_number - 1, width=5)

        self.submit = self.spin
        self.submit.pack(side='top')
        
        self.submit = self.resize
        self.submit.pack(side="top")

        self.table = SimpleTableInput(self, 3, 3)
        self.table.pack(side="top", fill="both", expand=True)

        self.submit = self.output_result
        self.submit.pack(side="bottom")
        
        self.submit = self.start      
        self.submit.pack(side="bottom")
        
        self.submit = self.txt_input_chain
        self.submit.pack(side="bottom")

        self.submit = self.txt_label_chain
        self.submit.pack(side="bottom")  
        
        self.submit = self.txt_input_final_state
        self.submit = self.submit.pack(side="bottom")

        self.submit = self.txt_label_final_state
        self.submit.pack(side="bottom")

        self.submit = self.txt_input_alphabet
        self.submit.pack(side="bottom")

        self.submit = self.txt_label_alphabet
        self.submit.pack(side="bottom")
        
        self.submit = self.spin_init
        self.submit.pack(side="bottom")
     
        self.submit = self.label_spin
        self.submit.pack(side="bottom")




    def on_resize(self):
        print(self.spin.get())
        
        number_state = int(self.spin.get())
        
        if number_state <= 15:
            self.last_spin_number = number_state

            self.spin.destroy()
            self.resize.destroy()
            self.start.destroy()
            self.table.destroy()
            self.txt_input_alphabet.destroy()
            self.txt_label_alphabet.destroy()
            self.txt_label_chain.destroy()
            self.txt_input_chain.destroy()
            self.txt_input_final_state.destroy()
            self.txt_label_final_state.destroy()
            self.spin_init.destroy()
            self.label_spin.destroy()

            self.txt_input_chain = tk.Entry(self,width=40)
            self.txt_label_chain = tk.Label(self, text="Enter the chain:")
            self.txt_input_alphabet = tk.Entry(self,width=40)
            self.txt_label_alphabet = tk.Label(self, text="Enter symbols of the alphabet separated by a space:")
            self.spin = tk.Spinbox(self, from_=self.last_spin_number, to=15, width=5)
            self.start = tk.Button(self, text="Start", command=self.on_start)
            self.resize = tk.Button(self, text="Resize", command=self.on_resize)

            self.txt_input_final_state = tk.Entry(self,width=40)
            self.txt_label_final_state = tk.Label(self, text="Enter the numbers of the end states separated by a space:")
                
            self.spin_init = tk.Spinbox(self, from_=0, to=self.last_spin_number - 1, width=5)
            self.label_spin = tk.Label(self, text="Select init state") 

            self.submit = self.spin
            self.submit.pack(side='top')

            self.submit = self.resize
            self.submit.pack(side="top") 

            self.table = SimpleTableInput(self, number_state, number_state)
            
            self.table.pack(side="top", fill="both", expand=True)

            self.submit = self.start      
            self.submit.pack(side="bottom")
        
            self.submit = self.txt_input_chain
            self.submit.pack(side="bottom")

            self.submit = self.txt_label_chain
            self.submit.pack(side="bottom")  
       
            self.submit = self.txt_input_final_state
            self.submit = self.submit.pack(side="bottom")

            self.submit = self.txt_label_final_state
            self.submit.pack(side="bottom")

            self.submit = self.txt_input_alphabet
            self.submit.pack(side="bottom")

            self.submit = self.txt_label_alphabet
            self.submit.pack(side="bottom")
       
            self.submit = self.spin_init
            self.submit.pack(side="bottom")

            self.submit = self.label_spin
            self.submit.pack(side="bottom")

            self.update()
            self.mainloop()

    def on_start(self):
       
        self.output_result.delete('1.0', tk.END)

        number_states = int(self.spin.get())
        dka_matrix = self.table.get()
        alph = [self.txt_input_alphabet.get()]
        final_states = self.txt_input_final_state.get().split(' ')
        chain_str = self.txt_input_chain.get()
        
        chain_str = chain_str.replace(' ','')

        check_dka = DKA(dka_matrix, number_states)
        check_dka._set_alphabet(alph)
        check_dka._set_init_state(self.spin_init.get())
        check_dka._set_final_states(final_states)
   
        check_dka.check_chain(chain_str)

        check_dka.display_dka()
        self.output_result.insert(INSERT, check_dka.str_output)
        


