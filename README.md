
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

![lrheatmap](https://i.imgur.com/3FbstE4.png)

Random Forest - 60%

![rfheatmap](https://i.imgur.com/BQ5dzcb.png)

XGBoost - 73%

![xgboostheatmap](https://i.imgur.com/7SQheNl.png)


Job Recommendation:

Used NLTK to create a bag-of-words from a Kaggle dataset of 30000+ jobs and ScikitLearn's cosine similarity to compare the resume with web-scrapped job postings (using BeautifulSoup) from Indeed. Returned the top 10 best matched Indeed job postings. 

![vectorizerimg](https://i.imgur.com/bZhyKl1.png)







## Deployment

Once our functionalities were combined, we deployed our react.js front-end and flask back-end onto AWS EC2. 
![deploymentimg](https://i.imgur.com/4qdhfvk.png)
## Demo

Demo to come :)

Link to our presentation!

https://tinyurl.com/vbu4a47n
