from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Heart Diagnose Report")
root.geometry("540x540")
root.configure(background = "salmon")

question1_radioBtn = StringVar(value = "0")
question1 = Label(root, text = "Do you experience shortness of breath during routine activities ?", fg = "white", bg = "salmon")
question1.pack()
question1_radio1 = Radiobutton(root, text = "Yes", variable = question1_radioBtn, value = "Yes", bg = "salmon")
question1_radio1.pack()
question1_radio2 = Radiobutton(root, text = "No", variable = question1_radioBtn, value = "No", bg = "salmon")
question1_radio2.pack()

question2_radioBtn = StringVar(value = "0")
question2 = Label(root, text = "Do you have swelling in the feet / ankles / legs (shoes feel tighter) or abdomen ?", fg = "white", bg = "salmon")
question2.pack()
question2_radio1 = Radiobutton(root, text = "Yes", variable = question2_radioBtn, value = "Yes", bg = "salmon")
question2_radio1.pack()
question2_radio2 = Radiobutton(root, text = "No", variable = question2_radioBtn, value = "No", bg = "salmon")
question2_radio2.pack()

question3_radioBtn = StringVar(value = "0")
question3 = Label(root, text = "Do you feel any symptoms - confusion, disorientation or loss of memory ?", fg = "white", bg = "salmon")
question3.pack()
question3_radio1 = Radiobutton(root, text = "Yes", variable = question3_radioBtn, value = "Yes", bg = "salmon")
question3_radio1.pack()
question3_radio2 = Radiobutton(root, text = "No", variable = question3_radioBtn, value = "No", bg = "salmon")
question3_radio2.pack()

question4_radioBtn = StringVar(value = "0")
question4 = Label(root, text = "Do you experience shortness of breath while at rest / lying down ?", fg = "white", bg = "salmon")
question4.pack()
question4_radio1 = Radiobutton(root, text = "Yes", variable = question4_radioBtn, value = "Yes", bg = "salmon")
question4_radio1.pack()
question4_radio2 = Radiobutton(root, text = "No", variable = question4_radioBtn, value = "No", bg = "salmon")
question4_radio2.pack()

question5_radioBtn = StringVar(value = "0")
question5 = Label(root, text = "Do you experience persistent wheezing / coughing that produces white or pink blood tinged mucus ?", fg = "white", bg = "salmon")
question5.pack()
question5_radio1 = Radiobutton(root, text = "Yes", variable = question5_radioBtn, value = "Yes", bg = "salmon")
question5_radio1.pack()
question5_radio2 = Radiobutton(root, text = "No", variable = question5_radioBtn, value = "No", bg = "salmon")
question5_radio2.pack()

def hd_score():
    score = 0
    if question1_radioBtn.get() == "Yes":
        score = score + 10
        print(score)
        
    if question2_radioBtn.get() == "Yes":
        score = score + 10
        print(score)
        
    if question3_radioBtn.get() == "Yes":
        score = score + 10
        print(score)
        
    if question4_radioBtn.get() == "Yes":
        score = score + 10
        print(score)
        
    if question5_radioBtn.get() == "Yes":
        score = score + 10
        print(score)
        
    if score <= 10:
        messagebox.showinfo("Report", "You don't need to visit a doctor.")
        
    elif score > 10 and score <= 30:
        messagebox.showinfo("Report", "You might perhaps have to visit a doctor.")
    
    else:
        messagebox.showinfo("Report", "I strongly advise you to visit a doctor.")

btn = Button(root, text = "Show Report", command = hd_score)
btn.pack()

root.mainloop()

