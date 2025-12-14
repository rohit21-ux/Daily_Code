import tkinter as tk
import sys

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)  # do_clear the current input
    entry.insert(tk.END, current + str(value)) 

# Function to calculate the operation
def do_calculate():
    try:
        result = str(eval(entry.get()))  # calculate the expression
        entry.delete(0, tk.END)  # clear the entry
        entry.insert(tk.END, result)  # Show the result
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the input
def do_clear():
    entry.delete(0, tk.END)

def do_exit():
    sys.exit(0)

# Set up the main gui  window
root_window = tk.Tk()
root_window.title("Basic Calculator")

# Create the input field
entry = tk.Entry(root_window, width=20, font=("Georgia", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# buttons in row 1
B1 = tk.Button(root_window)
B1.configure(text='1', command=lambda: button_click('1'), font=("Georgia", 18), width=5, height=2) # lambda command is used for small operations 
B1.grid(row=1, column=0, padx=5, pady=5)

B2 = tk.Button(root_window)
B2.configure(text='2', command=lambda: button_click('2'), font=("Georgia", 18), width=5, height=2) # lambda command is used for small operations
B2.grid(row=1, column=1, padx=5, pady=5)

B3 = tk.Button(root_window)
B3.configure(text='3', command=lambda: button_click('3'), font=("Georgia", 18), width=5, height=2) # lambda command is used for small operations
B3.grid(row=1, column=2, padx=5, pady=5)

B4 = tk.Button(root_window)
B4.configure(text='.', command=lambda: button_click('.'), font=("Georgia", 18), width=5, height=2) # lambda command is used for small operations
B4.grid(row=1, column=3, padx=5, pady=5)

# buttons in Row 2
B5 = tk.Button(root_window)
B5.configure(text='4', command=lambda: button_click('4'), font=("Georgia", 18), width=5, height=2) # lambda command is used for small operations
B5.grid(row=2, column=0, padx=5, pady=5)

B6 = tk.Button(root_window)
B6.configure(text='5', command=lambda: button_click('5'), font=("Georgia", 18), width=5, height=2) # lambda command is used for small operations
B6.grid(row=2, column=1, padx=5, pady=5)

B7 = tk.Button(root_window)
B7.configure(text='6', command=lambda: button_click('6'), font=("Georgia", 18), width=5, height=2) # lambda command is used for small operations
B7.grid(row=2, column=2, padx=5, pady=5)

B8 = tk.Button(root_window)
B8.configure(text='*', command=lambda: button_click('*'), font=("Georgia", 18), width=5, height=2) # lambda command is used for small operations
B8.grid(row=2, column=3, padx=5, pady=5)

# buttons in Row 3
B9 = tk.Button(root_window)
B9.configure(text='7', command=lambda: button_click('7'), font=("Georgia", 18), width=5, height=2) # lambda command is used for small operations
B9.grid(row=3, column=0, padx=5, pady=5)

B10 = tk.Button(root_window)
B10.configure(text='8', command=lambda: button_click('8'), font=("Georgia", 18), width=5, height=2) # lambda command is used for small operations
B10.grid(row=3, column=1, padx=5, pady=5)

B11 = tk.Button(root_window)
B11.configure(text='9', command=lambda: button_click('9'), font=("Georgia", 18), width=5, height=2) # lambda command is used for small operations
B11.grid(row=3, column=2, padx=5, pady=5)

B12 = tk.Button(root_window)
B12.configure(text='+', command=lambda: button_click('+'), font=("Georgia", 18), width=5, height=2) # lambda command is used for small operations
B12.grid(row=3, column=3, padx=5, pady=5)

# buttons in Row 4
B13 = tk.Button(root_window)
B13.configure(text='0', command=lambda: button_click('0'), font=("Georgia", 18), width=5, height=2) # lambda command is used for small operations
B13.grid(row=4, column=0, padx=5, pady=5)

B14 = tk.Button(root_window)
B14.configure(text='/', command=lambda: button_click('/'), font=("Georgia", 18), width=5, height=2) # lambda command is used for small operations
B14.grid(row=4, column=1, padx=5, pady=5)

B15 = tk.Button(root_window)
B15.configure(text='=', command=do_calculate, font=("Georgia", 18), width=5, height=2)  # do_calculate command to evaluate expression
B15.grid(row=4, column=2, padx=5, pady=5)

B16 = tk.Button(root_window)
B16.configure(text='-', command=lambda: button_click('-'), font=("Georgia", 18), width=5, height=2) # lambda command is used for small operations
B16.grid(row=4, column=3, padx=5, pady=5)

# buttons in Row 5
B17 = tk.Button(root_window)
B17.configure(text='C', command=do_clear, font=("Georgia", 18), width=5, height=2,bg='skyblue') # do_clear command for clearing message box
B17.grid(row=5, column=1, padx=5, pady=5)

B18 = tk.Button(root_window)
B18.configure(text='Exit', command=do_exit, font=("Georgia", 18), width=5, height=2 ,bg='#ff7f7f') # do_exit command to terminate the application
B18.grid(row=5, column=2, padx=5, pady=5)


root_window.mainloop()
