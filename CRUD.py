""" CS340: Paul Kenaga """
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps

class AnimalShelter(object):
    
    """ 
    CRUD operations for collection in MongoDB 
    
    Methods:
    - create
    - read
    - update
    - delete
    
    """

    def __init__(self, user: str, password: str):
        """ 
        Initializing the MongoClient. This helps to access the MongoDB databases and collections 
        """
        self.client = MongoClient('mongodb://%s:%s@localhost:44114/?authSource=AAC&authMechanism=DEFAULT' % (user, password))
        self.database = self.client['AAC']
        
        

    def create(self, data: dict) -> bool:
        """ 
        Create/insert method to add a new document to a collection
        
        Parameter: set of key/value lookup pairs
        """
        try: 

            self.database.animals.insert_one(data)
                
             # Return true if insert successful
            return True
                
        except:
            
            # Return false if insert unsuccessful
            print('Error: unable to insert document')
            return False
        
        

    def read(self, target: dict):
        """ 
        Read/find method to retrieve a document from a collection
        
        Parameter: key/value lookup pair
        """
        try:
  
            # Store matching document(s) in cursor object
            cursor = self.database.animals.find(target, {'_id':False})
            
            
            # Check that cursor length is greater than 0
            if cursor.count() > 0:
                
                # Return result in cursor if successful
                return cursor

            else:

                # Else return error message string
                return 'Error: no matching results for target parameter' 
               
        except:
            
            return 'Error: unable to read document'
            
            
            
    def update(self, target: dict, data: dict):
        """ 
        Update method to change a field of a document from a collection 
        
        Parameters: (2) key/value lookup pairs
        """
        try:
           
            result = self.database.animals.update_many(target, {'$set': data })
            
            # Check that document(s) were updated
            if result.matched_count > 0:    
    
                # Return result in JSON format if successful
                return {'Result': True}

            else:

                # Else return error message string
                return 'Error: no matching results for target parameter' 
                
        except:
            
            return 'Error: unable to update document'
            
            
            
    def delete(self, target: dict):
        """ 
        Create/insert method to add a new document to a collection 
        
        Parameter: key/value lookup pair
        """
        try: 

            result = self.database.animals.delete_many(target)

            # Check that document(s) were deleted
            if result.deleted_count > 0:
                    
                # Return result in JSON format if successful
                return {'Result': True}

            else:

                # Else return error message string
                return 'Error: no matching results for target parameter'
            
        except:
            
            return 'Error: unable to remove document'  
            
       
             
            
            