import sqlite3
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import xlsxwriter
import os

app =Flask(__name__)
api = Api(app)




class Spliting(Resource):
    def get(self,file_name):
        conn = sqlite3.connect('patientsdetail.db', check_same_thread=False)
        cu = conn.cursor()
        cu.execute("SELECT * FROM PATIENT")
        
        WB_PATH = file_name
        PATH_TO_XLSX = os.path.basename(file_name)
        
        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook(PATH_TO_XLSX)

        worksheet = workbook.add_worksheet()
        
        expenses = cu.fetchall()
        # Start from the first cell. Rows and columns are zero indexed.
        row = 0
        col = 0
        # Iterate over the data and write it out row by row.
        for sno,firstname,lastname,email,state,country,pincode,phonenumber in (expenses):
            worksheet.write(row, col,     sno)
            worksheet.write(row, col + 1, firstname)
            worksheet.write(row, col + 2, lastname)
            worksheet.write(row, col + 3, email)
            worksheet.write(row, col + 4, state)
            worksheet.write(row, col + 5, country)
            worksheet.write(row, col + 6, pincode)
            worksheet.write(row, col + 7, phonenumber)
            row += 1
        workbook.close()
        return 'spliting is done',200

        cu.close()
        conn.close()

api.add_resource(Spliting, '/spliting/<string:file_name>')

if __name__ == '__main__':
    app.run(port = 5001 , debug = True )




