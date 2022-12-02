import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download(['stopwords', 'wordnet'])
nltk.download('omw-1.4')


class JobRecommender:
    # open the necessary files for processing and job recommendation
    job_df = pd.read_csv('job_df.csv', encoding='cp1252')
    with open('skill_bank.pkl', 'rb') as f:
        skill_bank = pickle.load(f)
    f.close()
    with open('job_tfidf.pkl', 'rb') as f:
        job_tfidf = pickle.load(f)
    f.close()
    with open('job_words.pkl', 'rb') as f:
        job_words = pickle.load(f)
    f.close()

    # Create the similarity matrix
    sim_arr = cosine_similarity(job_tfidf, job_tfidf)

    # Process one resume at a time: the string resume
    def __init__(self, resume_str):

        # Load LinkedIn Skills to help clean resume
        self.clean_resume = self.processing(resume_str)

    def processing(self, resume_str):
        # Clean up text using NLP

        review = re.sub(
            '(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?"',
            " ",
            resume_str,
        )
        review = review.lower()
        review = review.split()
        lm = WordNetLemmatizer()
        review = [
            lm.lemmatize(word)
            for word in review
            if not word in set(stopwords.words("english"))
        ]

        # Remove words not part of the skills
        temp = []
        for word in review:
            if word in self.skill_bank:
                temp.append(word)
        ret_str = ' '.join(temp)

        return ret_str

    def find_highest_sim_jobs(self):
        # Creating a Tfidf Vectorizer
        query_tfidf = TfidfVectorizer().fit(JobRecommender.job_words)
        query_tfidf = query_tfidf.transform([self.clean_resume])
        # Create a Cosine similarity matrix to recommend jobs
        cosine_similarities = cosine_similarity(query_tfidf, JobRecommender.job_tfidf).flatten()
        top_10_jobs = cosine_similarities.argsort()[:-11:-1]
        top_10_jobs_df = pd.DataFrame({"company": [], "positionName": [], "url": [], "similarity score": [], "location":[]})
        # Create and return a dataframe composed of the top 10 job recommendations
        counter = 0
        for job in top_10_jobs:
            print(JobRecommender.job_df.iloc[job]["url"])
            top_10_jobs_df.loc[len(top_10_jobs_df.index)] = JobRecommender.job_df.iloc[job]
            top_10_jobs_df.loc[counter]["similarity score"] = cosine_similarities[job]
            counter += 1
        
        return [
                {
                "company": x["company"],
                "positionName": x["positionName"],
                "url": x["url"],
                "location": x["location"],
                "similarity score": x["similarity score"],
                } 
                for i,x in top_10_jobs_df.iterrows()
            ]