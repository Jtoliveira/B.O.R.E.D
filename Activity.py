class Activity:
    def __init__(self, activity, accessibility, typeOf, participants, price, link, key):
        self.activity = activity # Description of the queried Activity
        self.accessibility = accessibility #how possible it is ([0,1] is the most accessible)
        self.type = typeOf #"education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"
        self.participants = participants #number of people it could involve (0,n)
        self.price = price #Cost of the activity [0,1] -> 0 is free
        self.link = link #link to the activity, if there is a link to provide
        self.key = key #unique numeric id [1000000, 9999999]

    def getActivityName(self):
        return self.activity

    def getAccessibility(self):
        return str(self.accessibility)
    
    def getType(self):
        return self.type
    
    def getParticipants(self):
        return str(self.participants)
    
    def getPrice(self):
        return str(self.price)
    
    def getLink(self):
        return self.link
    
    def getKey(self):
        return self.key

    def setActivityName(self, name):
        self.activity = name
    
    def setAccessibility(self, ac):
        self.accessibility = ac

    def setType(self, typeOf):
        self.type = typeOf

    def setParticipants(self, participants):
        self.participants = participants

    def setPrice(self, price):
        self.price = price

    def setLink(self, link):
        self.link = link

    def setKey(self, key):
        self.key = key

    def toString(self):
       return "Name: " + self.getActivityName() + "\nAccessibility: " \
        + self.getAccessibility() + "\nType: " + self.getType() + "\nNr of Participants: " \
            + self.getParticipants() + "\nPrice: " + self.getPrice() + "\nKey: " + self.getKey() \
                + "\nLink: " + self.getLink()
    