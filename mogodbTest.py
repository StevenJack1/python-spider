from pymongo import MongoClient


class mongoDbBase:

    def __init__(self, databaseIp = '127.0.0.1',databasePort = 27017, mongodbName='wind'):

        client = MongoClient(databaseIp,databasePort)
        self.db = client[mongodbName]

    def saveInfo(self,infoList):
        self.db.banking_and_wealth.insert_many(infoList)