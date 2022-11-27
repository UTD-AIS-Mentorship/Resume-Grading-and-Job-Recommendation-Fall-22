from flask import Flask, request
import ResumeScorer
import json
import xgb_model
import ResumeToText
import time
from ResumeRequirements import requirements
import nltk
from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")

Resume_scorer = ResumeScorer.resumeScore()

tic = time.perf_counter()

data = ResumeToText.extract_text_from_pdf('JesseMusaResumeFall2022.pdf')
data = data.split()
data = ' '.join([stemmer.stem(y) for y in data])

print(type(data))

  
    
# print("succesfully created the text data form the given pdf file")
    
    
prediction = xgb_model.predict([data])
# print(prediction)

# print(prediction)

Resume_Req = requirements(data)
Resume_Requirements = Resume_Req.calcScore()





grammar_score = Resume_scorer.grammarScore(data)
word_score = Resume_scorer.wordScore(data)
numeric_score = Resume_scorer.numericScore(data)

# print(grammar_score)

toc = time.perf_counter()


print(f"Time taken :  {toc - tic:0.4f} seconds")