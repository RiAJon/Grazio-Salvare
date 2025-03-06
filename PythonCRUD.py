from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    def __init__(self,username,password):
        
        # connection variables
        USER = username
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32789
        DB = 'AAC'
        COL = 'animals'
        
        # initialize connection 
        self.client = MongoClient(
            'mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
    # CREATE method
    def create(self, data):
      
        if data is not None:
            try:
                result = self.collection.insert_one(data)
                return result.acknowledged # returns true if successful 
            except Exception as e:
                raise Exception(f"An error occured while inserting document: {e}")
        else: 
            raise Exception("Nothing to save, because data parameter is empty")
            
    # READ method
    def read(self, query):
        
        if query is not None:
            try: 
                resultCursor = self.collection.find(query)
                return list(resultCursor) # convert cursor to list 
            except Exception as e:
                raise Exception(f"An error occured while reading document(s): {e}")
                
        else:
            raise Exception("Cannot locate document(s), because query parameter is empty")
            
    #UPDATE method
    def update(self, query, updateValues):
        
        if all([query,updateValues]):
            try: 
                result = self.collection.update_many(query,{"$set": updateValues})
                return result.modified_count # returns number of successfully modified documents 
            except Exception as e:
                raise Exception(f"An error occured while updating document(s): {e}")
        else:
            raise Exception("Cannot locate document(s), because either the query or updated values parameter is empty")
            
    #DELETE method
    def delete(self,query):
        
        if query is not None:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count # returns number of successfully deleted documents 
            except Exception as e:
                raise Exception(f"An error occured while deleting document(s): {e}")
        else:
            raise Exception("Cannot locate document(s), because query parameter is empty")

                
        
    
    
    
    
    