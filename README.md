
# ResuBot 

ResuBot is a tool designed to help people improve their resumes and receive job suggestions that match their qualifications and experiences. Our platform was developed by students who were eager for internships, but frustrated by the challenge of effectively showcasing their qualifications and experiences to potential employers.




## Functionalities

1. Resume Grader
2. Resume Classifier
3. Job Recommender


## How

Resume Grading:

Used NLTK and LanguageTool in conjunction to grade the resume content based on strong action actions words, spelling, quantifiable data, grammar, and the average sentence length. 


Resume Classification:

Trained 3 distinct machine learning models with a Kaggle dataset of 2400+ resumes with the goal of acheiving the highest accuracy. 

Logistic Regression - 67%

<img src='https://imgur.com/a/ahVzaHC' title='Logistic Regression Heatmap' width='' alt='Logistic Regression Heatmap' />

Random Forest - 60%
![rfheatmap](https://imgur.com/a/2lpl4Lg)

XGBoost - 73%
![xgboostheatmap](https://imgur.com/a/zOwJLP9)


Job Recommendation:

Used NLTK to create a bag-of-words from a Kaggle dataset of 30000+ jobs and ScikitLearn's cosine similarity to compare the resume with web-scrapped job postings (using BeautifulSoup) from Indeed. Returned the top 10 best matched Indeed job postings. 

![vectorizerimg](https://imgur.com/a/h0XG8E8)







## Deployment

Once our functionalities were combined, we deployed our react.js front-end and flask back-end onto AWS EC2. 
![deploymentimg](https://imgur.com/a/jCPiVcC)
## Demo

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vSnY9GgOxlTkMaSDGUMpw4ki9xTylrgC3MnC3y2XFjNrwXfrnUKu-Y7gGzh2S3DUsCy-VBleB2CJWwW/embed?start=true&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

