from tkinter import *
from tkinter.messagebox import *
# some useful variables
font = ("verdana", 22, )
# important functions
def clear():
    ex = textfield.get()
    ex = ex[0:len(ex) - 1]
    textfield.delete(0, END)
    textfield.insert(0, ex)

def all_clear():
    textfield.delete(0, END)
def click_btn_function(event):
    print("btn clicked")
    b = event.widget
    text = b["text"]
    print(text)

    if text == "x":
        textfield.insert(END, "*")
        return

    if text == "=":
        try:
            ex = textfield.get()
            answer = eval(ex)
            textfield.delete(0, END)
            textfield.insert(0, answer)
        except Exception as e:
            print("Error..", e)
            showerror("Error", e)
        return


    textfield.insert(END,text)
# creating a window

window = Tk()
window.title("Calculator")
window.resizable(width=False, height=False)
window.configure(bg='gainsboro')
# headingLabel
heading = Label(window, text="Calculator", bg='gainsboro', font=font,)
heading.pack(side=TOP)
# textfield
textfield = Entry(window, font=font, justify=RIGHT, textvariable= "screen" ,bd=14 ,insertwidth=4, width=14)
textfield.pack(side=TOP, pady=4, fill=X, padx=4)
# buttons
buttonFrame = Frame(window, bg='gainsboro')
buttonFrame.pack(side=TOP)
# adding buttons
temp = 1
for i in range(0,  3):
    for j in range(0, 3):
        btn = Button(buttonFrame, text=str(temp), font=font, bg='gainsboro',bd=3, width=5, relief="ridge",activebackground="orange", activeforeground="black")
        btn.grid(row=i, column=j, padx=3, pady=3)
        temp = temp+1
        btn.bind("<Button-1>", click_btn_function)
zeroBtn = Button(buttonFrame, text="0", font=font, width=5, relief="ridge",bd=3, activebackground="orange", activeforeground="black", bg='gainsboro')
zeroBtn.grid(row=3, column=0, padx=3, pady=3)
dotBtn = Button(buttonFrame, text=".", font=font, width=5, relief="ridge",bd=3, activebackground="orange", activeforeground="black", bg='gainsboro')
dotBtn.grid(row=3, column=1, padx=3, pady=3)
equalBtn = Button(buttonFrame, text="=", font=font, width=5, relief="ridge",bd=3,activebackground="orange", activeforeground="black", bg='gainsboro')
equalBtn.grid(row=3, column=2, padx=3, pady=3)
plusBtn = Button(buttonFrame, text="+", font=font, width=5, relief="ridge",bd=3, activebackground="orange", activeforeground="black", bg='gray70')
plusBtn.grid(row=0, column=3, padx=3, pady=3)
minusBtn = Button(buttonFrame, text="-", font=font, width=5, relief="ridge",bd=3, activebackground="orange", activeforeground="black", bg='gray70')
minusBtn.grid(row=1, column=3, padx=3, pady=3)
multBtn = Button(buttonFrame, text="x", font=font, width=5, relief="ridge",bd=3, activebackground="orange", activeforeground="black", bg='gray70')
multBtn.grid(row=2, column=3, padx=3, pady=3)
devideBtn = Button(buttonFrame, text="/", font=font, width=5, relief="ridge",bd=3, activebackground="orange", activeforeground="black", bg='gray70')
devideBtn.grid(row=3, column=3, padx=3, pady=3)
clearBtn = Button(buttonFrame, text="C", font=font, width=11, relief="ridge",bd=3, activebackground="orange", activeforeground="black", bg='gray70', command=clear)
clearBtn.grid(row=4, column=0, columnspan=2, padx=3, pady=3)
AllclearBtn = Button(buttonFrame, text="AC", font=font, width=11, relief="ridge",bd=3, activebackground="orange", activeforeground="black",bg='gray70', command=all_clear)
AllclearBtn.grid(row=4, column=2, columnspan=2, padx=3, pady=3)


#binding all buttons
plusBtn.bind("<Button-1>", click_btn_function)
minusBtn.bind("<Button-1>", click_btn_function)
multBtn.bind("<Button-1>", click_btn_function)
devideBtn.bind("<Button-1>", click_btn_function)
zeroBtn.bind("<Button-1>", click_btn_function)
dotBtn.bind("<Button-1>", click_btn_function)
equalBtn.bind("<Button-1>", click_btn_function)
window.mainloop()






