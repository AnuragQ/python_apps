from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


app= Flask(__name__)
basedir =os.path.abspath(os.path.dirname(__file__))



app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///' +os.path.join(basedir,'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
# @app.route('/', methods=['get'])
# def get():
#     return jsonify({'msg':'hello world'}) 
db.SQLAlchemy(app)

ma=Marshmallow(app)

#product

class Product(db,Model()):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),unique=True)
    description = db.Column(db.String(200))
    price = db.Column(dbFloat)
    qty = db.Column(db.Integer)
    def __init__(self, )



if __name__=='__main__':
    app.run(debug=True)