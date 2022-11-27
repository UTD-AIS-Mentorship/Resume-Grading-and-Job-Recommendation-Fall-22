
import pickle
import pandas as pd
import xgboost as xgb


labels = ['ARTSFITNESS' , 'BUSINESSHR' , 'CONSULTANTADVOCATE', 'ENGINEERING' ,'FINANCEBANKINGACCOUNTING' , 'HEALTHCARE' , 'INFORMATIONTECHNOLOGY', 'PUBLICRELATIONSDIGITALMEDIASALES' , 'TEACHER']

xgb_classifier = xgb.Booster()
xgb_classifier.load_model("model.txt")
countvectorizer_pickled = pickle.load(open('vectorizer', 'rb'))

def predict(resume):
    vect_resume_arr = countvectorizer_pickled.transform(resume).toarray()
    feature_names = countvectorizer_pickled.get_feature_names_out()
    vecDF = pd.DataFrame(vect_resume_arr, columns = feature_names)
    xgtest = xgb.DMatrix(vecDF.values)
    prediction = xgb_classifier.predict(xgtest)
    prediction = prediction.tolist()[0]
    output = []
    for i in range(0 , 9) : output.append([labels[i], (round(prediction[i]**(1./3) * 100 , 2))])
    output.sort(key = lambda x : x[1] , reverse= True)
    return output[0 : 3]




 # print(len(feature_names))
    # print(vecDF)
    # vecDF = xgb.DMatrix(vecDF)