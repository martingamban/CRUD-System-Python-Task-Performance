from tkinter import *
from tkinter import ttk
from tkinter import messagebox

StudentList = []
class Employee:
    def __init__(self, name, section, StudentNumber):
        self.name = name
        self.section = section
        self.StudentNumber = StudentNumber

    def getName (self):
        return self.name

    def getSection(self):
        return self.section

    def getStundentNumber(self):
        return self.StudentNumber
    


window = Tk()
window.title("Student Information List")
#window.resizable(0,0)
window.configure(background = 'light gray')

#Add to list   
def add_to_list():
    tree.insert('', 'end', text = input1.get(), values =(input1.get(), input2.get(), input3.get()))
    messagebox.showinfo("Information", "Succesfully Added")

    input1.delete(0, 'end')
    input2.delete(0, 'end')
    input3.delete(0, 'end')

    
#Exit The system
def exit_prog():
       window.destroy()

#Delete data
def delete_to_list():
    MsgBox = messagebox.askquestion("Delete Entry","Are you sure you want to Delete an Entry")
    if MsgBox == 'yes':
       selected_items = tree.selection()[0]
       tree.delete(selected_items)
    else:
       messagebox.showinfo("Return","you will now return to the appplication screen")

    input1.delete(0, 'end')
    input2.delete(0, 'end')
    input3.delete(0, 'end')

#Update the list
#Click the tow after that change the info in the textbox afterwards click the button update 
def update_prog():
    selected_items = tree.selection()[0]
    tree.item(selected_items, text = input1.get(), values=(input1.get(), input2.get(), input3.get()))

#Label
Label (window, text="STUDENT INFORMATION LIST", font = "Calibri 14 bold", background = 'light gray').grid(row=1, column = 1 ,padx=20, pady=10)    
Label (window, text="Student Name:", background = 'light gray').grid(row=2, padx=20, pady=10)
Label (window, text="Course/Section:", background = 'light gray').grid(row=3, padx=20, pady=10)
Label (window, text="Student Number:", background = 'light gray').grid(row=4, padx=20, pady=10)

#Textbox
input1 = Entry(window, width = 20)
input1.grid(row=2, column=1 , padx=20, pady=10)
input2 = Entry(window,width = 20)
input2.grid(row=3, column=1, padx=20, pady=10)
input3 = Entry(window,width = 20)
input3.grid(row=4, column=1, padx=20, pady=10)

#Button
button1 = Button(window, text="ADD", command=add_to_list)
button1.grid(row=5, column=0, padx=20, pady=10)
button3 = Button(window, text="DELETE", command=delete_to_list)
button3.grid(row=5, column=1, padx=20, pady=10)
button4 = Button(window, text="UPDATE", command = update_prog)
button4.grid(row=5,column=2, padx=20, pady=10)
button5 = Button(window, text="EXIT", command=exit_prog)
button5.grid(row=5, column=4, padx=20, pady=10)


#Treeview

tree = ttk.Treeview(window, height=15 , columns=("student name","course/section","Student Number"), show = "headings")
tree.grid(row=6,column=0, columnspan=6)
tree.heading('#1', text="Student Name",anchor=W)
tree.heading('#2', text="Course/Section")
tree.heading('#3', text="Student Number")
                                                  
window.mainloop()
