from tkinter import *

window = Tk()
window.title('Miles to KM Converter')
window.minsize(width=200,height=100)
window.config(padx=20, pady=10)

def outputCalc():
    converted_figure = int(miles_input.get()) * 1.609
    output_label.config(text=str(converted_figure))

equal_to_label = Label(text='is equal to')
equal_to_label.grid(column=0, row=2)

output_label = Label(text=0, anchor="center")
output_label.grid(column=1, row=2)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=2)

submit_btn = Button(text="Calculate", command=outputCalc)
submit_btn.grid(column=1, row=3)

window.mainloop()
