import Tkinter
import tkMessageBox

window = Tkinter.Tk()

greeting = Tkinter.Label(window, text="How many numbers would you like to have?")
greeting.pack()

guess = Tkinter.Entry(window)
guess.pack()

def show_answer():
    for i in range(int(guess.get())):
        if i % 3 == 0:
            result = "Fizz"
        elif i % 5 == 0:
            result = "Buzz"
        elif i % 3 == 0 and i % 5 == 0:
            result ="FizzBuzz"
        else:
            result = i

        tkMessageBox.showinfo(message = result)

# submit button
submit = Tkinter.Button(window, text="Submit", command=show_answer)  # check_guess, not check_guess()
submit.pack()

window.mainloop()