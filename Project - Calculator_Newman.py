import tkinter as tk
from  tkinter import Text
from tkinter.constants import INSERT



#button = tk.Button(window, text = 'OK', width=8, height=2, bg='light gray', fg='black') 
def display_digits(text):
    global results
    #Insert values onto the text box 
    text_box.insert(INSERT, text)
    #Store values onto results
    results=results+text
    
def clear():
    global results
    #"1.0" and "end" refer to the first character and the last character of the contents in the Text widget
    text_box.delete("1.0", "end") 
    results=''
def equal_button():
    try:
 
        global results

        #Python’s eval() allows you to evaluate arbitrary Python expressions from a string-based
        total = str(eval(results))
        text_box.delete("1.0", "end") 
        text_box.insert(INSERT, total)
 
        
    #Display an error if invalid data is entered through the eval() 
    except:

        text_box.delete("1.0", "end") 
        text_box.insert(INSERT," error ")
        
if __name__ == "__main__":

    window = tk.Tk()
    window.title("Calculator")
    window.geometry("277x240")
    #Indicating all the buttons 
    results=''
    button_1 = tk.Button(window, text = '1', bg='light gray', fg='black', width=8, height=2, command=lambda:display_digits('1')) 
    button_2 = tk.Button(window, text = '2', bg='light gray', fg='black', width=8, height=2, command=lambda:display_digits('2'))
    button_3 = tk.Button(window, text = '3', bg='light gray', fg='black', width=8, height=2, command=lambda:display_digits('3'))
    button_4 = tk.Button(window, text = '4', bg='light gray', fg='black', width=8, height=2, command=lambda:display_digits('4'))
    button_5 = tk.Button(window, text = '5', bg='light gray', fg='black', width=8, height=2, command=lambda:display_digits('5'))
    button_6 = tk.Button(window, text = '6', bg='light gray', fg='black', width=8, height=2, command=lambda:display_digits('6'))
    button_7 = tk.Button(window, text = '7', bg='light gray', fg='black', width=8, height=2, command=lambda:display_digits('7'))
    button_8 = tk.Button(window, text = '8', bg='light gray', fg='black', width=8, height=2, command=lambda:display_digits('8'))
    button_9 = tk.Button(window, text = '9', bg='light gray', fg='black', width=8, height=2, command=lambda:display_digits('9'))
    button_0 = tk.Button(window, text = '0', bg='light gray', fg='black', width=18, height=2, command=lambda:display_digits('0'))
    button_plus = tk.Button(window, text = '+', bg='light gray', fg='black', width=8, height=2, command=lambda:display_digits('+'))
    button_minus = tk.Button(window, text = '-', bg='light gray', fg='black', width=8, height=2, command=lambda:display_digits('-'))
    button_mult = tk.Button(window, text = '*', bg='light gray', fg='black', width=8, height=2, command=lambda:display_digits('*'))
    button_period = tk.Button(window, text = '.', bg='light gray', fg='black', width=8, height=2, command=lambda:display_digits('.'))
    button_slash = tk.Button(window, text = '/', bg='light gray', fg='black', width=8, height=2, command=lambda:display_digits('/'))
    button_equal = tk.Button(window, text = '=', bg='light gray', fg='black', width=28, height=2, command=lambda:equal_button()) ##Use this to equal the equation
    button_clear = tk.Button(window, text = 'Clear', bg='light gray', fg='black', width=8, height=2, command=lambda:clear()) ##Use this to clear equation

    #Creating the Entry Box (Text Box)
    #text_box=tk.Entry(window,  width=40)
    text_box = Text(window, height = 2, width = 32, bg = 'light yellow')

    #Placing all the buttons to the calculator 
    button_1.place(x=0,y=40)
    button_2.place(x=70,y=40)
    button_3.place(x=140,y=40)
    button_plus.place(x=210,y=40)
    button_4.place(x=0,y=80)
    button_5.place(x=70,y=80)
    button_6.place(x=140,y=80)
    button_minus.place(x=210,y=80)
    button_7.place(x=0,y=120)
    button_8.place(x=70,y=120)
    button_9.place(x=140,y=120)
    button_mult.place(x=210,y=120)
    button_0.place(x=0,y=160)
    button_period.place(x=140,y=160)
    button_slash.place(x=210,y=160)
    button_equal.place(x=0,y=200)
    button_clear.place(x=210,y=200)
    text_box.place(x=10, y=4)
    #text_box.pack()


    window.mainloop()

