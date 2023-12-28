import tkinter as tk

#Address
address = "85 Bristol Road East"
city = "Mississauga"
province = "Ontario"
postalCode = "L4Z 3P3"
country = "Canada"

#Name
firstName = "Freddy"
lastName = "Shaikh"
fullName = firstName + " " + lastName

#contacts
phoneNumber = "437-267-3291"
email = "shaikhfh1@gmail.com"
linkedIn = "https://www.linkedin.com/in/freddy-shaikh/"
portfolio = """Here's my Portfolio:
https://www.freddyshaikh.com/

All the code used is publicly available on my Github:
https://github.com/Freddy-S3

Thank you for your time and consideration in reviewing me as a candidate. Have a nice day!"""


#buttons
buttons = [address,
           city,
           province,
           postalCode,
           country,
           firstName,
           lastName,
           fullName,
           phoneNumber,
           email,
           linkedIn,
           portfolio
           ]

#functions
def buttonFunction(buttonText):
    clipboard.clipboard_clear()
    clipboard.clipboard_append(buttonText)
    print("copied" + buttonText)


def buttonMaker(number):
    tk.Button(text=buttons[number], command=lambda: buttonFunction(buttons[number])).grid(column=1, row=number)

#mainloop
clipboard = tk.Tk()
clipboard.title('Copy Clipboard')
clipboard.geometry("500x500")
clipboard.resizable(0,0)

for i in range(len(buttons)):
    buttonMaker(i)    

clipboard.mainloop()