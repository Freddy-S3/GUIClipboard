import tkinter as tk
import datetime

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
portfolio = "https://www.freddyshaikh.com/"
github = "https://github.com/Freddy-S3"


#Resume and coverletter
resumeText = open("resume.txt", "r").read()
resume = ["Resume", resumeText]

coverletterText = open("coverletter.txt", "r").read()
coverletter = ["Cover Letter", coverletterText]


#additional answers
salary = "115000"
notApplicable = "N/A"
whereDidYouHear = "ZipRecruiter"

today = datetime.datetime.now()
dateMDY = today.strftime("%x")
date = ["Date", dateMDY]

twoWeekslater = today + datetime.timedelta(days=14)
twoWeeksMDY = twoWeekslater.strftime("%x")
twoWeeksNotice = ["2 Weeks Notice", twoWeeksMDY]


fullPortfolioText = """Here's my Portfolio:
https://www.freddyshaikh.com/

All the code used is publicly available on my Github:
https://github.com/Freddy-S3

Thank you for your time and consideration in reviewing me as a candidate. Have a nice day!"""
fullPortfolio = ["Full Portfolio", fullPortfolioText]

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
           portfolio,
           github,
           notApplicable,
           salary,
           whereDidYouHear
           ]

bigButtons = [fullPortfolio,
              resume,
              coverletter,
              date,
              twoWeeksNotice]


#global counter
rowNumber = 0

#functions
def buttonFunction(buttonText):
    clipboard.clipboard_clear()
    clipboard.clipboard_append(buttonText)
    print("copied " + buttonText)


def buttonMaker(number):
    tk.Button(text=buttons[number], command=lambda: buttonFunction(buttons[number])).grid(column=1, row=rowNumber)

def altbuttonMaker(name, buttonText):
    tk.Button(text=name, bg='#000000', fg='#b7f731', command=lambda: buttonFunction(buttonText)).grid(column=1, row=rowNumber)

#mainloop
clipboard = tk.Tk()
clipboard.title('Copy Clipboard')
#clipboard.geometry("500x500")
#clipboard.resizable(0,0)

for i in range(len(buttons)):
    buttonMaker(i)    
    rowNumber += 1

#Special cases
for i in range(len(bigButtons)):
    altbuttonMaker(bigButtons[i][0], bigButtons[i][1])
    rowNumber += 1
    


clipboard.mainloop()