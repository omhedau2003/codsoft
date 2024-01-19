from tkinter import *

calculation = ""

# Functions for evaluation
def add_calculation(symbol):
    # Calculation as global variable
    global calculation
    # Any integer to string
    calculation += str(symbol)
    # Delete from result
    text_result.delete(1.0, "end")
    # Insert data
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    # Try catch statements for errors
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

root = Tk()

# A text display
text_result = Text(root, height=2, width=14, font=("Arial", 24))
# Grid structure with 5 columns
text_result.grid(columnspan=5)
# Designing button 1
btn_1 = Button(root, text="1", command=lambda : add_calculation(1), width=5, font=("Arial", 14))
btn_1.grid(row=2, column=1)
# Designing button 2
btn_2 = Button(root, text="2", command=lambda : add_calculation(2), width=5, font=("Arial", 14))
btn_2.grid(row=2, column=2)
# Designing button 3
btn_3 = Button(root, text="3", command=lambda : add_calculation(3), width=5, font=("Arial", 14))
btn_3.grid(row=2, column=3)
# Designing button 4
btn_4 = Button(root, text="4", command=lambda : add_calculation(4), width=5, font=("Arial", 14))
btn_4.grid(row=3, column=1)
# Designing button 5
btn_5 = Button(root, text="5", command=lambda : add_calculation(5), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=2)
# Designing button 6
btn_6 = Button(root, text="6", command=lambda : add_calculation(6), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=3)
# Designing button 7
btn_7 = Button(root, text="7", command=lambda : add_calculation(7), width=5, font=("Arial", 14))
btn_7.grid(row=4, column=1)
# Designing button 8
btn_8 = Button(root, text="8", command=lambda : add_calculation(8), width=5, font=("Arial", 14))
btn_8.grid(row=4, column=2)
# Designing button 9
btn_9 = Button(root, text="9", command=lambda : add_calculation(9), width=5, font=("Arial", 14))
btn_9.grid(row=4, column=3)
# Designing button 0
btn_0 = Button(root, text="0", command=lambda : add_calculation(0), width=5, font=("Arial", 14))
btn_0.grid(row=5, column=2)
# Designing button +
btn_plus = Button(root, text="+", command=lambda : add_calculation("+"), width=5, font=("Arial", 14))
btn_plus.grid(row=2, column=4)
# Designing button -
btn_minus = Button(root, text="-", command=lambda : add_calculation("-"), width=5, font=("Arial", 14))
btn_minus.grid(row=3, column=4)
# Designing button *
btn_mul = Button(root, text="*", command=lambda : add_calculation("*"), width=5, font=("Arial", 14))
btn_mul.grid(row=4, column=4)
# Designing button /
btn_div = Button(root, text="/", command=lambda : add_calculation("/"), width=5, font=("Arial", 14))
btn_div.grid(row=5, column=4)
# Designing button (
btn_open = Button(root, text="(", command=lambda : add_calculation("("), width=5, font=("Arial", 14))
btn_open.grid(row=5, column=1)
# Designing button )
btn_close = Button(root, text=")", command=lambda : add_calculation(")"), width=5, font=("Arial", 14))
btn_close.grid(row=5, column=3)
# Designing button clear
btn_clear = Button(root, text="C", command= clear_field, width=11, font=("Arial", 14))
btn_clear.grid(row=6, column=1, columnspan=2)
# Designing button =
btn_equals = Button(root, text="=", command= evaluate_calculation, width=11, font=("Arial", 14))
btn_equals.grid(row=6, column=3, columnspan=2)
root.mainloop()