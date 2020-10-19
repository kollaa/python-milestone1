from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import csv
import pandas as pd 
import json
import sqlite3

app = Flask(__name__)
api = Api(app)

conn = sqlite3.connect('patientsdetail.db', check_same_thread=False)
cur = conn.cursor()
class Retriving(Resource):

    def get(self,name):
        with open(name, 'r') as csv_file:
            
            for row in csv_file:
                cur.execute("INSERT  INTO patient VALUES (?, ?, ?, ?, ?, ?, ?, ?)", row.split(","))

                conn.commit()
                
            return 'data transfer successful', 200
       
        cur.close()
        conn.close()
        


api.add_resource(Retriving, '/retrivings/<string:name>')

if __name__ == '__main__':
    app.run(port = 5000 , debug = True )