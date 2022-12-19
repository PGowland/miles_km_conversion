import tkinter

window = tkinter.Tk()
window.title("Miles-Kilometres Converter")
window.minsize(500, 300)
sub_title = tkinter.Label(text="Please enter the amount you wish to convert and select the type of conversions")
sub_title.pack()
amount = tkinter.Entry(width=10)
amount.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Miles to Kilometres", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Kilometres to Miles", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

answer = 0.0
answer_text = tkinter.Label(text="")
answer_text.pack(side="bottom")


def action():
    if radio_state.get() == 1:
        answer = float(amount.get()) * 1.6
        answer_text.config(text=f"{amount.get()} miles is equal to {answer}km", font=("Arial", 24, "bold"))
    if radio_state.get() == 2:
        answer = float(amount.get()) / 1.6
        answer_text.config(text=f"{amount.get()}km is equal to {answer} miles", font=("Arial", 24, "bold"))


button = tkinter.Button(text="Submit", command=action)
button.pack()
window.mainloop()
