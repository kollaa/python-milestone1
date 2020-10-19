from PyPDF2 import PdfFileMerger
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import os
app = Flask(__name__)
api = Api(app)

class Merging(Resource):
    def get(self,file_name):
        WB_PATH = file_name
        BASE_NAME = os.path.basename(WB_PATH)
        PATH_TO_PDF = WB_PATH[0:WB_PATH.find(BASE_NAME)] + BASE_NAME[0:-4] + ".pdf"
        pdfs = os.getcwd()
        merger = PdfFileMerger()
        for pdf in os.listdir(pdfs):
            if pdf.endswith(".pdf"):
                print(pdf)
                merger.append(pdf)
        merger.write(PATH_TO_PDF)
        merger.close()
        return 'merging was done', 200

api.add_resource(Merging, '/merging/<string:file_name>')


if __name__ == '__main__':
    app.run(port = 5003, debug = True )