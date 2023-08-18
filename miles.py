import tkinter

window = tkinter.Tk()
window.title("Miles to KM Convertor")
window.minsize(width=500, height=300)

label1 = tkinter.Label(text="is equal to")
label1.grid(row=1, column=0)

ans = tkinter.Entry()
ans.grid(row=0, column=1)

label2 = tkinter.Label()
label2.grid(row=1, column=1)

def unit_convertor():
    print("Calculate")
    label2["text"] = int(ans.get()) * 1.60934

    
doubletap = tkinter.Button(text="Calculate", command=unit_convertor)
doubletap.grid(row=2, column=1)

label3 = tkinter.Label(text="Miles")
label3.grid(row=0, column=2)

label4 = tkinter.Label(text="KM")
label4.grid(row=1, column=2)

window.mainloop()