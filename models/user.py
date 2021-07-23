from app import db

class Users(db.Model):   
    __tablename__ = 'user' 
    _id = db.Column('id', db.Integer, primary_key=True)   
 
    name = db.Column('name', db.String(100))    
    email = db.Column(db.String(100)) 
   
    def __init__(self, name, email):  
      
        self.name =name    
    
        self.email = email
