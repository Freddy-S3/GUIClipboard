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
dateMDY = today.strftime("%m/%d/%Y")
date = ["Date", dateMDY]

twoWeekslater = today + datetime.timedelta(days=14)
twoWeeksMDY = twoWeekslater.strftime("%m/%d/%Y")
twoWeeksNotice = ["2 Weeks Notice", twoWeeksMDY]


fullPortfolioText = """Here's my Portfolio:
https://www.freddyshaikh.com/

All the code used is publicly available on my Github:
https://github.com/Freddy-S3

Thank you for your time and consideration in reviewing me as a candidate. Have a nice day!"""
fullPortfolio = ["Full Portfolio", fullPortfolioText]


whyUsText = """Based on the description, 
I get to make full use of my diverse set of talents, 
while the position is still challenging enough for me to learn something new."""
whyUs = ["Why Us?", whyUsText]


referredText = "Unfortunately I was not referred, but I would love to get to know the team!"
referred = ["Referred?", referredText]


whyMeText = """I am very proficient in teaching myself new technologies and methods, 
as evidenced by me teaching myself Japanese to fluency, 
and teaching myself Software Engineering and DevOps, 
despite my academic background being Healthcare"""
whyMe = ["Why Me?", whyMeText]

whyMe150CharText = """After escaping medical school, teaching myself Japanese, programming, and cloud architecture, I believe that I can teach myself just about anything!"""
whyme150Char = ["Why Me? 150Char", whyMe150CharText]

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
              twoWeeksNotice,
              whyUs,
              referred,
              whyMe,
              whyme150Char]


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