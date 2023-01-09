# from flask_sqlalchemy import SQLAlchemy


# db = SQLAlchemy()



# class Employee(db.Model):
#     __tablename__ = 'results'

#     name = db.Column(db.String(30),primary_key = True)
#     age = db.Column(db.Integer())

#     def __init__(self, name,age):
#         self.name = name
#         self.age  = age
        
#     def __repr__(self):
#         return '<id {self.}>'.format(self.name)

from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)

db = SQLAlchemy()

class Employee(db.Model):

    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(40))
    age = db.Column(db.Integer)

    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age

    def __repr__(self):
        return f"User<{self.name}>"
