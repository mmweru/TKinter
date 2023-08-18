import tkinter

window = tkinter.Tk()
window.title("My First Gui Program")
window.minsize(width=500, height=300)

# #Label
# my_label = tkinter.Label(text="Hello it's a label here", font=("Arial", 24, "italic"))
# my_label.pack() #places the label on the screen
#
# #to change the properties of a new text we use
# my_label["text"] = "Maryann is Awesome"
#
# #Button
# def button_clicked():
#     print("It's Me")
#     my_label["text"] = input.get()
#
#
# button = tkinter.Button(font=("Times New Roman", 12, "bold"), text = "Click Me", command=button_clicked)
# button.pack()

label = tkinter.Label(text="Label")
label.grid(row=0, column=0)

bbutton = tkinter.Button(text = "Button")
bbutton.grid(row=1, column=1)

nnewb = tkinter.Button(text="New Button")
nnewb.grid(row=0, column=2)

entry = tkinter.Entry()
entry.grid(row=3, column=3)
#Entry

# input = tkinter.Entry(width=10)
# input.pack()
# print(input.get())

window.mainloop()
