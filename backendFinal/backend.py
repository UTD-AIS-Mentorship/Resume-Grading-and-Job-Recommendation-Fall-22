from flask import Flask, request, jsonify
from flask_cors import CORS

import re
import os
import json

import ResumeScorer
import xgb_model
import ResumeToText
from ResumeRequirements import requirements
from JobRecommender import JobRecommender

import nltk
from nltk.stem.snowball import SnowballStemmer


app = Flask(__name__)
CORS(app)
import threading
Resume_scorer = ResumeScorer.resumeScore() # Object for the functionality Grammar Score 
stemmer = SnowballStemmer("english")

fileFolder = "./resumes"
fileIndex = 0

############## functions for prediction and scoring
def func1(data , hashmap) :
    hashmap['prediction'] = xgb_model.predict([data])

def func2(data , hashmap) :
    Resume_Req = requirements(data)
    hashmap['Resume Requirements'] = Resume_Req.calcScore()

def func3(data , hashmap) :
    hashmap['Grammar score'] = Resume_scorer.grammarScore(data)
    
def func4(data , hashmap) :
    hashmap['Word Score'] = Resume_scorer.wordScore(data)
     
    
def func5(data , hashmap) :
    hashmap['Numeric Score'] = Resume_scorer.numericScore(data)

def func6(data , hashmap) :
    f = JobRecommender(data)
    hashmap['similarjobs'] = f.find_highest_sim_jobs()

################# End of them
 
@app.route('/data' , methods = [ 'POST' , 'GET'])
def senddata() :
    global fileIndex
    global fileFolder

    fileIndex += 1

    fileName = 'curResume' +str(fileIndex) + '.pdf'

    filePath = fileFolder + "/" + fileName

    file  = request.files['file']
    file.save(filePath)

    data = ResumeToText.extract_text_from_pdf(filePath)
     
    result = {}
    
    # stemming the text data
    data_model = re.sub(
            '(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?"',
            " ",
            data,
        )
    data_model = data_model.lower()
    data_model = data_model.split()
    data_model = ' '.join([stemmer.stem(y) for y in data_model])
    
    
    scores = {}
    # Now calculating scores using threading 
    t1 = threading.Thread(target=func1, args=(data_model,result))
    t2 = threading.Thread(target=func2, args=(data,scores))
    t3 = threading.Thread(target=func3, args=(data,scores))
    t4 = threading.Thread(target=func4, args=(data,scores))
    t5 = threading.Thread(target=func5, args=(data,scores))
    t6 = threading.Thread(target=func6, args=(data,result))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()


    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    
    result['TotalScore'] = (50 * scores['grammar_score']['Score'] + 20 * scores['Resume_Requirements']['Score'] + 15 * (scores['word_score']['Score'] + scores['numeric_score']['Score'] ) )/ 100
                            
    
    result['scores'] = scores
    
    print("here")
    print(jsonify(result))

    return result

 
if __name__ == '__main__':
   app.run()