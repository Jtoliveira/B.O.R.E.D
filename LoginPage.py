from tkinter import *
from LoginUtils import Login
import RandomActivityPage

#layout adapted from https://www.geeksforgeeks.org/create-mysql-database-login-page-in-python-using-tkinter/

login = Login("users.txt")

root = Tk()

root.geometry("400x400")
root.title("B.O.R.E.D - Born Of Random Entertainment Deficits")

#creating/opening the database and creating the USERS table
login.databaseSetup()

def createNewUser(username, password):

    if login.checkIfUserAlreadyExists(username):
        warning = Label(root, text="User Already Exists")
        warning.place(x = 175, y = 200)
        warning.after(5000, lambda: warning.destroy()) #the warning goes away after 5 seconds
    else:
        login.createUser(username, password)

def loginFunction(username, password):
    
    if login.checkUserLogin(username,password):
        RandomActivityPage.createPage( Toplevel(),  username)#open the user main page
        root.withdraw() #destroy() will end the program, withdraw hides the window
    else:
        warning = Label(root, text="Invalid Login")
        warning.place(x = 175, y = 200)
        warning.after(5000, lambda: warning.destroy()) #the warning goes away after 5 seconds


# Definging the first row 
lblfrstrow = Label(root, text ="Username") 
lblfrstrow.place(x = 100, y = 20) 
  
Username = Entry(root, width = 35) 
Username.place(x = 200, y = 20, width = 100) 
   
lblsecrow = Label(root, text ="Password", ) 
lblsecrow.place(x = 100, y = 50) 
  
password = Entry(root, show='*', width = 35) 
password.place(x = 200, y = 50, width = 100) 
  
submitbtn = Button(root, text ="Login", command = lambda : loginFunction(Username.get(), password.get())) 
submitbtn.place(x = 175, y = 100, width = 55) 

createUserButton = Button(root, text ="Create User", command = lambda : createNewUser( Username.get(), password.get() ) ) 
createUserButton.place(x = 155, y = 300, width = 100) 

root.mainloop()