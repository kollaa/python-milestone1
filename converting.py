from docx2pdf import convert
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import csv
import pandas as pd 
import json
import os
import win32com.client
import pythoncom
from pywintypes import com_error

app = Flask(__name__)
api = Api(app)

class ConvertingDocx(Resource):

    def get(self,file_name):
        pythoncom.CoInitialize()
        save_path = os.getcwd()
        WB_PATH = file_name
        BASE_NAME = os.path.basename(WB_PATH)
        print(BASE_NAME)
        PATH_TO_PDF = WB_PATH[0:WB_PATH.find(BASE_NAME)] + "new" + BASE_NAME[0:-5] + ".pdf"
        completeName = os.path.join(save_path,PATH_TO_PDF)
        
        print(PATH_TO_PDF)
        convert(file_name, completeName)
        return 'converting docx to pdf is done', 200

class ConvertingXlsx(Resource):
    
    def get(self,file_name):
        
        pythoncom.CoInitialize()
        save_path = os.getcwd()
        WB_PATH = file_name
        newpath = os.path.abspath(file_name)
        BASE_NAME = os.path.basename(WB_PATH)
        PATH_TO_PDF = WB_PATH[0:WB_PATH.find(BASE_NAME)] + "new" + BASE_NAME[0:-5] + ".pdf"
        completeName = os.path.join(save_path,PATH_TO_PDF)
        excel = win32com.client.Dispatch("Excel.Application")
        #app.logger.info(excel)
        excel.Visible = False
        try:
            print('Start conversion to PDF')
            wbs = excel.Workbooks.Open(newpath)
            ws_index_list = [1]
            wbs.WorkSheets(ws_index_list).Select()
            wbs.ActiveSheet.ExportAsFixedFormat(0, completeName)
        except com_error as e:
            print('failed.')
        else:
            print('Succeeded.')
        finally:
            wbs.Close()
            excel.Quit()
        return 'converting xlsx to pdf is done', 200

api.add_resource(ConvertingDocx, '/convertingdocx/<string:file_name>')

api.add_resource(ConvertingXlsx, '/convertingxlsx/<string:file_name>')

if __name__ == '__main__':
    app.run(port = 5002, debug = True )