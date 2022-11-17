import nltk
import pandas as pd
import numpy as np
import spacy
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download(['stopwords','wordnet'])
nltk.download('omw-1.4')

#python -m spacy download en_core_web_lg

class jobRecommender:
    #Process one resume at a time: the string resume
    def __init__(self, resumeStr):
        self.nlp = spacy.load('en_core_web_lg')
        self.clean_resume = self.processing(resumeStr)
        self.countVecArr = self.resume_vectorize()
        self.jobs = pd.read_csv("./JobsData.csv")
        self.simArr = self.calculateSimilarityScore()

    def processing(self, resumeStr):
        review = re.sub(
            '(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?"',
            " ",
            resumeStr,
        )
        review = review.lower()
        review = review.split()
        print(review)
        lm = WordNetLemmatizer()
        review = [
            lm.lemmatize(word)
            for word in review
            if not word in set(stopwords.words("english"))
        ]
        return " ".join(review)



    def findHighestSimJobs(self):
        indices = np.argpartition(self.simArr[0], -10)[-10:]
        for idx in indices:
            print(f"{self.jobs['job_post'][idx]}")
            print(f"{self.simArr[0][idx]}")
            print("")

    def resume_vectorize(self):
        with open('vectorizer_updated.pkl', 'rb') as f:
            _, resVec = pickle.load(f)
        vector = resVec.transform(pd.Series(self.clean_resume))
        vector_arr = vector.toarray()
        return vector_arr

    def calculateSimilarityScore(self):
        jobsArr = np.load('countVecJobsArr.npy')
        return cosine_similarity(self.countVecArr, jobsArr)

if __name__ == "__main__":
    test = jobRecommender("crazy my boi")


    # FindsimilarityScores
    # print(a)
    # a.findHighestSimJobs()