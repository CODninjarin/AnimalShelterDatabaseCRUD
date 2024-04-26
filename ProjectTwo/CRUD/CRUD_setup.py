from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        DB = 'AAC'
        COL = 'animals'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30914
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if self.collection.find(data).count() == 0:
            self.database.animals.insert(data)  # data should be dictionary   
            return True
        else:
            print ("data already exists")
            return False

# Create method to implement the R in CRUD.
    def read(self,data):
        if self.collection.find(data).count() > 0:
            return list(self.collection.find(data))
        else:
            return ("data does not exist")
    
# Update method
    def update(self, query, data):
        if self.collection.find(query).count() > 0:
            return self.database.animals.update_many(query, {"$set": data}).raw_result
        else:
            return ("No entry to delete")

# delete method
    def delete(self,query):
        if self.collection.find(query).count() > 0:
            return self.database.animals.delete_many(query).raw_result
        else:
            return ("No entry to delete")
