from sklearn.feature_extraction.text import CountVectorizer
import pickle
import pandas as pd


logistic_reg_pickled_model = pickle.load(open('logistic_regression_model', 'rb'))
countvectorizer_pickled = pickle.load(open('vectorizer', 'rb'))


def predict(resume):
    vect_resume_arr = countvectorizer_pickled.transform(resume).toarray()
    feature_names =countvectorizer_pickled.get_feature_names_out()
    vecDF = pd.DataFrame(vect_resume_arr, columns = feature_names)
    
    prediction = logistic_reg_pickled_model.predict(vecDF)
    return prediction


resume = " I love to become software engineer"

print(predict([resume]))