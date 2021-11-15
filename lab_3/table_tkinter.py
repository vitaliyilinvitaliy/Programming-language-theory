import tkinter as tk
from tkinter.constants import INSERT
from typing import Sized
from tkinter import scrolledtext
from algorithm_dmpa import DMPA


class Example(tk.Frame):
    
    txt_input_state= 0
    input_state = 0
    
    txt_output_result = 0
    output_result = 0

    button_start = 0

    txt_input_chain = 0
    input_chain = 0

    txt_size_state = 0
    input_size_state = 0

    txt_alphabet = 0
    input_alphabet = 0

    txt_start_state = 0
    input_start_state = 0

    txt_end_state = 0
    input_end_state = 0

    size_font = 13

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        #Init

        self.txt_input_state = tk.Label(self, text="Input:", font=("Arial Bold", self.size_font))

        self.input_state = scrolledtext.ScrolledText(self, width=60, height=15)

        self.output_result = scrolledtext.ScrolledText(self, width=60, height=8)
        self.txt_output_result = tk.Label(self, text="Output:", font=("Arial Bold", self.size_font))

        self.button_start = tk.Button(self, text="Start algorithm", command=self.on_start, font=("Arial Bold", self.size_font))

        self.input_size_state = tk.Entry(self,width=40)
        self.txt_size_state = tk.Label(self, text="Size state:", font=("Arial Bold", self.size_font))

        self.input_alphabet = tk.Entry(self,width=40)
        self.txt_alphabet = tk.Label(self, text="Alphabet:", font=("Arial Bold", self.size_font))

        self.input_start_state = tk.Entry(self,width=40)
        self.txt_start_state = tk.Label(self, text="Start state:", font=("Arial Bold", self.size_font))

        self.input_end_state = tk.Entry(self,width=40)
        self.txt_end_state = tk.Label(self, text="End state:", font=("Arial Bold", self.size_font))

        self.input_end_state = tk.Entry(self,width=40)
        self.txt_end_state = tk.Label(self, text="End state:", font=("Arial Bold", self.size_font))

        self.input_chain = tk.Entry(self,width=40)
        self.txt_input_chain = tk.Label(self, text="Chain:", font=("Arial Bold", self.size_font))

        #Move elements

        self.submit = self.txt_input_state
        self.submit.pack(side="top")

        self.submit = self.input_state
        self.submit.pack(side="top")

        self.submit = self.txt_size_state      
        self.submit.pack(side="top")

        self.submit = self.input_size_state      
        self.submit.pack(side="top")

        self.submit = self.txt_alphabet
        self.submit.pack(side="top")

        self.submit = self.input_alphabet
        self.submit.pack(side="top")
        
        self.submit = self.txt_start_state
        self.submit.pack(side="top")

        self.submit = self.input_start_state
        self.submit.pack(side="top")

        self.submit = self.txt_end_state
        self.submit.pack(side="top")

        self.submit = self.input_end_state
        self.submit.pack(side="top")

        self.submit = self.txt_input_chain
        self.submit.pack(side="top")

        self.submit = self.input_chain
        self.submit.pack(side="top")

        self.submit = self.button_start
        self.submit.pack(side="top")

        self.submit = self.txt_output_result
        self.submit.pack(side="top")      
        self.submit = self.output_result
        self.submit.pack(side="top")  

        
    def on_start(self):
        self.output_result.delete('1.0', tk.END)

        #Извлекаем данные из элементов окна
        input_state_str = self.input_state.get('1.0','end-1c')
        size_state_str = self.input_size_state.get()
        alphabet_str = self.input_alphabet.get()
        start_state_str = self.input_start_state.get()
        end_state_str = self.input_end_state.get()
        chain_str = self.input_chain.get()

        dmpa_res = DMPA([
                          input_state_str, 
                          size_state_str, 
                          alphabet_str, 
                          start_state_str, 
                          end_state_str,
                          chain_str
                        ])

        self.output_result.insert(INSERT, dmpa_res.output_str)