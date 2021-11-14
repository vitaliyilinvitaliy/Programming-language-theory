from tkinter import *
from table_tkinter import *

window = Tk()

def main():
    
    window.title("Lab4")
    window.geometry('550x800')

    Example(window).pack(side="top", fill="both", expand=True)
    window.mainloop()
    
if __name__ == '__main__':
    main()
