from flask import Flask, request
import json
import model
app = Flask(__name__)
 
@app.route('/data' , methods = [ 'POST' , 'GET'])
def senddata() :
    data = str(request.files['document'].read(), 'utf-8')
    prediction = model.predict(data)
    return prediction

 
if __name__ == '__main__':
   app.run()