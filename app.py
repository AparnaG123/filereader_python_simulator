from flask import Flask, render_template, request, jsonify
import json
import os
from bs4 import BeautifulSoup
import xml.dom.minidom



app = Flask(__name__)

#@Author: #
#@Date: #14-9-2021

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

@app.route('/', methods=['GET', 'POST']) # To render HSS Homepage
def home_page():
    return render_template('index.html')

@app.route('/addPdp', methods=['POST'])  # This is the PDPprofile api.
def add_pdp():
    if (request.method=='POST'):
        #Please replace the json file and thats all! Fire away.
        result=open(os.path.join(__location__, 'addPdpProfile.json'))
    else:
        result = "Response not registered in the Python Application"
    
    return jsonify(json.load(result))

@app.route('/locationInfo', methods=['POST']) # for calling the locationInfo API 
def locationInfo():
    if (request.method=='POST'):
    #Please replace the json file and thats all! Fire away.
        result = open(os.path.join(__location__, 'locationInfo.json'))
    else:
        result = "Response not registered in the Python Application"
    
    return jsonify(json.load(result))
    
    
@app.route('/tadigError', methods=['POST']) # for calling the locationInfo API 
def tadigError():
    if (request.method=='POST'):
    #Please replace the json file and thats all! Fire away.
        result = open(os.path.join(__location__, 'tadigError.json'))

    else:
        result = "Response not registered in the Python Application"
    
    return jsonify(json.load(result))


@app.route('/otaErrorInfo', methods=['POST']) # for calling the locationInfo API 
def otaErrorInfo():
    if (request.method=='POST'):
    #Please replace the json file and thats all! Fire away.
        result = open(os.path.join(__location__, 'otaErrorInfo.json'))

    else:
        result = "Response not registered in the Python Application"
    
    return jsonify(json.load(result))



@app.route('/otaProgressInfo', methods=['POST']) # for calling the locationInfo API 
def otaProgressInfo():
    if (request.method=='POST'):
    #Please replace the json file and thats all! Fire away.
        result = open(os.path.join(__location__, 'otaProgressInfo.json'))

    else:
        result = "Response not registered in the Python Application"
    
    return jsonify(json.load(result))


@app.route('/otaJobId', methods=['POST']) # for calling the locationInfo API 
def otaJobId():
    if (request.method=='POST'):
    #Please replace the json file and thats all! Fire away.
        result = open(os.path.join(__location__, 'otaJobId.json'))

    else:
        result = "Response not registered in the Python Application"
    
    return jsonify(json.load(result))

@app.route('/otaSomething', methods=['POST']) # for calling the locationInfo API 
def otaSomething():
    if (request.method=='POST'):
    #Please replace the json file and thats all! Fire away.
        result = open(os.path.join(__location__, 'otaSomething.json'))

    else:
        result = "Response not registered in the Python Application"
    
    return jsonify(json.load(result))

@app.route('/OTAAdaptor/CreateCampaign', methods=['POST']) # for calling the CreateCampaign API 
def CreateCampaign():
    if (request.method=='POST'):
        CURRENT_path=os.path.dirname(__file__)+'/'
        print('Cwd of the Response File:',CURRENT_path)
        dom = xml.dom.minidom.parse(CURRENT_path+'CreateCampaign.xml') # or        xml.dom.minidom.parseString(xml_string)
        pretty_xml_as_string = dom.toprettyxml()
    else:
        result = "Response not registered in the Python Application"
    
    return pretty_xml_as_string

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=16060,debug=True)
