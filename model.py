
import pickle
import pandas as pd
import xgboost as xgb

xgb_classifier = xgb.Booster()
xgb_classifier.load_model("model.txt")
countvectorizer_pickled = pickle.load(open('vectorizer', 'rb'))

def predict(resume):
    vect_resume_arr = countvectorizer_pickled.transform(resume).toarray()
    feature_names = countvectorizer_pickled.get_feature_names_out()
    vecDF = pd.DataFrame(vect_resume_arr, columns = feature_names)
    xgtest = xgb.DMatrix(vecDF.values)
    prediction = xgb_classifier.predict(xgtest)
    print(type(prediction))
    return prediction


resume = "My name is raghuvamsi, I love software developer role"

print("###################################################")

print(predict([resume]))


 # print(len(feature_names))
    # print(vecDF)
    # vecDF = xgb.DMatrix(vecDF)