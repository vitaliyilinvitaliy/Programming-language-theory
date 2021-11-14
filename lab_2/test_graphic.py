from tkinter import *
from table_tkinter import *

window = Tk()

def main():
    
    window.title("Lab3")
    window.geometry('800x800')

#    btn = Button(window, text="Создать таблицу для ввода данных", command=clicked)
#    btn.grid(column=0, row=0)
    Example(window).pack(side="top", fill="both", expand=True)
    window.mainloop()
    




if __name__ == '__main__':
    main()
