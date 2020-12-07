from tkinter import *

from requests.api import get
from Request import Request
from Activity import Activity

def createPage(newPage, User):
    global randomActPage 

    randomActPage = newPage

    global parameters

    randomActPage.geometry("400x400")
    randomActPage.title(User + " Activity Page")

    setupButtons()

    parameters = "minprice=" + minPrice.get() + "&maxprice=" + maxPrice.get() + "&minaccessibility=" + minAcc.get() + "&maxaccessibility=" + maxAcc.get()

    note = Label(randomActPage, text="Remember to re-choose the type of activity\nafter altering the Price or Accessibility")
    note.place(x = 10, y = 340, width= 250)


def addParameter(newParam):
    global parameters
    global minPrice
    global maxPrice
    global minAcc
    global maxAcc

    parameters = "minprice=" + minPrice.get() + "&maxprice=" + maxPrice.get() + "&minaccessibility=" + minAcc.get() + "&maxaccessibility=" + maxAcc.get()

    if newParam != "":
        parameters = "type=" + newParam + "&" + parameters
    
def setupButtons():
    education = Button(randomActPage, text="Education", command = lambda: addParameter("education"))
    education.place(x = 0, y = 120, width = 100)

    recreational = Button(randomActPage, text="Recreational", command = lambda: addParameter("recreational"))
    recreational.place(x = 0, y = 140, width = 100)

    social = Button(randomActPage, text="Social", command = lambda: addParameter("social"))
    social.place(x = 0, y = 160, width = 100)

    diy = Button(randomActPage, text="DIY", command = lambda: addParameter("diy"))
    diy.place(x = 0, y = 180, width = 100)

    charity = Button(randomActPage, text="Charity", command = lambda: addParameter("charity"))
    charity.place(x = 0, y = 200, width = 100)

    cooking = Button(randomActPage, text="Cooking", command = lambda: addParameter("cooking"))
    cooking.place(x = 0, y = 220, width = 100)

    relaxation = Button(randomActPage, text="Relaxation", command = lambda: addParameter("relaxation"))
    relaxation.place(x = 0, y = 240, width = 100)

    music = Button(randomActPage, text="Music", command = lambda: addParameter("music"))
    music.place(x = 0, y = 260, width = 100)

    busywork = Button(randomActPage, text="Busywork", command = lambda: addParameter("busywork"))
    busywork.place(x = 0, y = 280, width = 100)

    busywork = Button(randomActPage, text="Random", command = lambda: addParameter(""))
    busywork.place(x = 0, y = 300, width = 100)

    priceLabel = Label(randomActPage, text ="Price [0,1]:") 
    priceLabel.place(x = 150, y = 120) 

    minPriceLabel = Label(randomActPage, text ="Min:")
    minPriceLabel.place(x = 150, y = 140) 

    global minPrice 
    minPrice = Entry(randomActPage, width = 15) 
    minPrice.place(x = 150, y = 160, width = 100) 

    maxPriceLabel = Label(randomActPage, text ="Max:")
    maxPriceLabel.place(x = 150, y = 180) 

    global maxPrice
    maxPrice = Entry(randomActPage, width = 15) 
    maxPrice.place(x = 150, y = 200, width = 100) 

    AccessibilityLabel = Label(randomActPage, text ="Accessibility [0,1]:") 
    AccessibilityLabel.place(x = 150, y = 230) 

    minAccLabel = Label(randomActPage, text ="Min:")
    minAccLabel.place(x = 150, y = 250) 

    global minAcc
    minAcc = Entry(randomActPage, width = 15) 
    minAcc.place(x = 150, y = 270, width = 100) 

    maxAccLabel = Label(randomActPage, text ="Max:")
    maxAccLabel.place(x = 150, y = 290) 

    global maxAcc
    maxAcc = Entry(randomActPage, width = 15) 
    maxAcc.place(x = 150, y = 310, width = 100) 

    newRandomActivity = Button(randomActPage, text = "New Activity", command = lambda: getNewActivity())
    newRandomActivity.place(x = 300, y = 340, width = 100)

    logout = Button(randomActPage, text="Logout", command = randomActPage.quit)
    logout.place(x = 300, y = 370, width = 100)

def getNewActivity():

    global parameters

    request = Request("http://www.boredapi.com/api/activity").makeRequest(parameters)

    displayActivity(request)

def displayActivity(request): #'REQUEST' is an activity in JSON format

    activity = Activity(
        request['activity'], 
        str(request["accessibility"]), 
        request["type"], 
        str(request["participants"]), 
        str(request["price"]),
        request["link"], 
        request["key"]
        )

    text = Text(randomActPage, height = 7, width = 50)
    text.insert(INSERT,activity.toString())
    text.place(x = 0)

