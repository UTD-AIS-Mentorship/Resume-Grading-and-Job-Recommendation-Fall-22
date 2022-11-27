import re
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download(['stopwords', 'wordnet'])
nltk.download('omw-1.4')


class JobRecommender:
    # Process one resume at a time: the string resume
    def __init__(self, resume_str):
        skills_path = 'linkedinskills.txt'
        with open(skills_path, encoding='utf8') as f:
            lines = f.readlines()
        f.close()
        skill_bank = []
        for line in lines:
            skill_bank.append(line.strip().lower())
        self.skill_str = ' '.join(skill_bank)
        self.clean_resume = self.processing(resume_str)
        self.job_df = pd.read_csv('job_df.csv')
        self.countVecArr = self.resume_vectorize()
        self.simArr = self.calculateSimilarityScore()


    def printTest(self):
        print(self.clean_resume)

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
            if word in self.skill_str:
                temp.append(word)
        ret_str = ' '.join(temp)

        return ret_str

    def findHighestSimJobs(self):
        cosine_sim = cosine_similarity(self.countVecArr, self.countVecArr)
        use = pd.DataFrame(cosine_sim)
        use = use.drop([0, 0])
        return self.job_df["company"].iloc[use.idxmax()[0]]

    def resume_vectorize(self):
        count = CountVectorizer(min_df=0)
        count_matrix = count.fit_transform(self.job_df["clean!"], self.clean_resume)
        return count_matrix

    def calculateSimilarityScore(self):
        cosine_sim = cosine_similarity(self.countVecArr, self.countVecArr)
        use = pd.DataFrame(cosine_sim)
        use = use.drop([0, 0])
        # print(self.job_df["company"].iloc[use.idxmax()[0]])
        # print(use[0].iloc[use.idxmax()[0] + 1])

        return use[0].iloc[use.idxmax()[0] + 1]

    if __name__ == "__main__":
        findHighestSimJobs()
        calculateSimilarityScore()
