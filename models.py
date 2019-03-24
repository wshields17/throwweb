from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy() 
import random

class Throwers(db.Model):
    name = db.Column(db.String,primary_key=True)
    Gradyear = db.Column(db.Integer)
    

class meetdata(db.Model):
   
    id = db.Column(db.Integer,primary_key=True,default = lambda:random.randint(3000,1000000))
    name = db.Column(db.String)
    meetdate = db.Column(db.String)
    spresult = db.Column(db.Float)

class outdoormeetdata(db.Model):
    id = db.Column(db.Integer,primary_key=True,default = lambda:random.randint(10,1000000))
    name = db.Column(db.String)
    datemeet = db.Column(db.String)
    spresult = db.Column(db.Float)
    discresult = db.Column(db.Float)    
    

