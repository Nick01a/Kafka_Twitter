from datetime import datetime



class Tweet:
    def __init__(self,name,message,date = datetime.now()):
        self.name = name
        self.message = message
        self.date = date

