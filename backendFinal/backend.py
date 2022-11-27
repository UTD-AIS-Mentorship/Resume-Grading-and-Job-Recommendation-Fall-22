from flask import Flask, request
import ResumeScorer
import json
import xgb_model
import ResumeToText
from ResumeRequirements import requirements
import nltk
from nltk.stem.snowball import SnowballStemmer
app = Flask(__name__)
import threading
Resume_scorer = ResumeScorer.resumeScore() # Object for the functionality Grammar Score 
stemmer = SnowballStemmer("english")

############## functions for prediction and scoring
def func1(data , hashmap) :
    hashmap['prediction'] = xgb_model.predict([data])

def func2(data , hashmap) :
    Resume_Req = requirements(data)
    hashmap['Resume_Requirements'] = Resume_Req.calcScore()

def func3(data , hashmap) :
    hashmap['grammar_score'] = Resume_scorer.grammarScore(data)
    
def func4(data , hashmap) :
    hashmap['word_score'] = Resume_scorer.wordScore(data)
    
    
def func5(data , hashmap) :
    hashmap['numeric_score'] = Resume_scorer.numericScore(data)
    
################# End of them
 
@app.route('/data' , methods = [ 'POST' , 'GET'])
def senddata() :
    
    
    data = (request.files['document'].read()).decode()



    data = ResumeToText.extract_text_from_pdf(data)
 
    result = {}
    
    
    # stemming the text data
    data = data.split()
    data = ' '.join([stemmer.stem(y) for y in data])
    
    scores = {}
    # Now calculating scores using threading 
    t1 = threading.Thread(target=func1, args=(data,result))
    t2 = threading.Thread(target=func2, args=(data,scores))
    t3 = threading.Thread(target=func3, args=(data,scores))
    t4 = threading.Thread(target=func4, args=(data,scores))
    t5 = threading.Thread(target=func5, args=(data,scores))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()


    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    
    result['scores'] = scores
    
    return result

 
if __name__ == '__main__':
   app.run(debug = True)