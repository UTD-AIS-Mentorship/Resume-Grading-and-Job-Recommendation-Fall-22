import re
import pandas as pd
# import spacy
#education
#spacy
class requirements():
    resume = ""
    score = 0
    gpa = ""
    phone = ""
    name = ""
    address = []
    websites = set()
    schools = []
    majors = []
    emails = set()
    names = []

    def __init__(self, resume):
        self.resume = resume
        self.gpa = self.findGPA()
        self.address = self.findStreetAddress()
        self.phone = self.findPhone()
        self.websites = self.findWebsites()
        self.schools = self.findSchools()
        self.majors = self.findMajor()
        self.emails = self.findEmail()
        self.websites -= self.emails
        # self.names = self.find_persons()
        self.calcScore()

    def __str__(self):
        return f"requirement score: {self.score}/100.0"

    # def find_persons(self):
    #     # Create Doc object
    #
    #     doc2 = self.nlp(self.resume[:30])
    #
    #     # Identify the persons
    #     persons = [ent.text for ent in doc2.ents if ent.label_ == 'PERSON']
    #
    #     # Return persons
    #     return persons

    def findEducation(self):
        return bool(re.search(r"(education)", self.resume.lower()))

    def findSchools(self):
        schools = []
        pattern = re.compile(r"(\b\w*\b\s){0,3}(\b(polytechnic|university|institute|school|faculty|technology|engineering|high school)\b)(\s\b\w*\b){0,4}")
        matches = pattern.finditer(self.resume.lower())
        for match in matches:
            schools.append(match.group(0))
        return schools

    def findMajor(self):
        majors = []
        pattern = re.compile(r"\b(major|minor)[:,-]?(\s\b\w*\b){0,5}")
        matches = pattern.finditer(self.resume.lower())
        for match in matches:
            majors.append(match.group(0))
        return majors

    def findExperience(self):
        return bool(re.search(r"(experience)", self.resume.lower()))

    def findSkills(self):
        return bool(re.search(r"(skills?)", self.resume.lower()))

    def findPhone(self):
        pattern = re.compile(r"[([{]?\d{3}[]})]?\D?\d{3}\D?\d{4}\b")
        matches = pattern.finditer(self.resume.lower())
        for match in matches:
            return match.group(0)

    def findStreetAddress(self):
        addresses = []
        pattern = re.compile(r"\b\d{1,6} +.{2,25}\b(avenue|ave|court|ct|street|st|drive|dr|lane|ln|road|rd|blvd|plaza|parkway|pkwy|suite|park|pk)[.,]?(.{0,25} +\b\d{5}\b)?")
        matches = pattern.finditer(self.resume.lower())
        for match in matches:
            addresses.append(match.group(0))

        # city, State
        pattern = re.compile(r"\b\w+, (AL|KY|OH|AK|LA|OK|AZ|ME|OR|AR|MD|PA|AS|MA|PR|CA|MI|RI|CO|MN|SC|CT|MS|SD|DE|MO|TN|DC|MT|TX|FL|NE|TT|GA|NV|UT|GU|NH|VT|HI|NJ|VA|ID|NM|VI|IL|NY|WA|IN|NC|WV|IA|ND|WI|KS|MP|WY)\b")
        matches = pattern.finditer(self.resume.upper())
        for match in matches:
            addresses.append(match.group(0))
        return addresses

    def findWebsites(self):
        websites = set()
        pattern = re.compile(r"[-a-zA-Z0-9:%._+~#@=]{1,256}\.(com|net|co|org|edu|us)\b([-a-zA-Z0-9()@:%_\+~#?&=\/]*)\b")
        matches = pattern.finditer(self.resume.lower())
        for match in matches:
            websites.add(match.group(0))
        return websites

    def findEmail(self):
        emails = set()
        pattern = re.compile(r"[-a-zA-Z0-9:%._\+~#=]{1,256}@[-a-zA-Z0-9:%._\+~#=]{1,256}\.(com|net|co|org|edu|us)\b([-a-zA-Z0-9()@:%_\+~#?&=\/]*)\b")
        matches = pattern.finditer(self.resume.lower())
        for match in matches:
            emails.add(match.group(0))
        return emails

    def findGPA(self):
        pattern = re.compile(r"\b\d{1,10}\.\d{1,10}(\/\d{1,10}\.\d{1,10})?\b")
        matches = pattern.finditer(self.resume.lower())
        for match in matches:
            return match.group(0)

    def calcScore(self):
        if self.findEducation():
            self.score += 10
        else:
            print("no education found")
        if self.findExperience():
            self.score += 25
        else:
            print("no experience found")
        if self.findSkills():
            self.score += 25
        else:
            print("no skills found")
        if self.gpa is not None:
            self.score += 5
        else:
            print("no GPA found")
        if self.phone is not None:
            self.score += 5
        else:
            print("no phone number found")
        if self.schools is not None:
            self.score += 7.5
        else:
            print("no schools found")
        if self.address is not None:
            self.score += 5
        else:
            print("no address found")
        if self.emails is not None:
            self.score += 5
        else:
            print("no email found")
        if self.majors is not None:
            self.score += 7.5
        else:
            print("no major found")
        if self.websites is not None:
            self.score += 5
        else:
            print("no website found")

def main():
    df = pd.read_csv("../Count_Vectorize_Resume_Linkedin_Keywords/resume.csv")
    req = requirements(df["Resume_str"][0])
    req = requirements("""
Jesse Musa

jessemusa2@gmail.com | (832)871-2702 | github.com/jesse51002 | Plano, TX

EDUCATION

The University of Texas at Dallas - Richardson, TX
Major: Computer Science Bachelor of Science | Minor: Statistics | Expected Graduation: December 2024
Computer Science GPA: 3.8 | Cumulative GPA: 3.65 | Jonsson Academic Success Scholarship Recipient

EXPERIENCE

Nova, Open-Source Self Driving Car

Core Developer

September 2022 – Current

•  Contributing to Nova's mission is to make an open-source self-driving car to increase accessibility of self-driving
•  Developing using the Robot Operating System (ROS) to combine the C++ and python programming languages
•  Applying Ground Segmentation using the Markov Random Field algorithm on a set of 3D points from 16-ring lidar
•  Creating the Dynamic Occupancy Grid Maps (DOGMa) using lidar points and dynamic state information
•

Implementing PredNet, a Recurrent Neural Network, to predict DOGMa across the car’s future time horizon

Artificial Intelligence Society

Project Lead

September 2022 – Current

•  Leading a team to make a Resume Grader and Job Recommender using NLP techniques and AWS services
•  Predicting Top Job Classes for inputted resumes using Supervised Classification Machine Learning Models
•  Recommending jobs based on the Cosine Similarity Score of the vectorization of the job description and resume content
•  Creating an Interactive React Front End to receive user's resumes, display resume scores and job recommendations

Association of Computing Machinery UTD

Research Assistant

September – November 2021

•  Researched to examine the effect of modern-day mob mentality on a companies’ financial performance in the stocks market
•  Web scraper 100,000+ #Neftlix Tweets from 09/2018 - 09/2021 then cleaned and applied sentiment analysis using Vader
•  Calculated the correlation between the sentiments of our tweets and the stock prices to give a correlation of 0.75.

PROJECTS

Emo7ion | Convolutional Neural Network, TensorFlow Keras, Flask, Matplotlib, AWS

Implemented AWS cloud services to create a deep learning Convolutional Neural Network (CNN) using TensorFlow Keres

•  Collaborated with the Artificial Intelligence Society to make a real time emotion detector website using AWS services
•
•  Trained model on 35,000+ images classified into 7 different emotions to achieve an emotion prediction accuracy of 65%
•  Deployed the model into a flask web application to predict multiple faces emotion in real-time from a webcam

Predicting Effective Arguments | Scikit-Learn, NLTK, Matplotlib, Logistic Regression

•  Competed in a Georgia Tech Kaggle’s competition to give 6th – 12th graders unbiased feedback on their argumentative texts
•  Oversampled argumentative text rating to increase the ‘ineffective’ class from 17% of data to 33%
•  Trained a Logistic regression model on 36,000+ argumentative texts categories to achieve an accuracy of 67%

RELEVANT SKILLS

•  Languages: Python, JavaScript, SQL, C++, Java, Lua, C#, C
•  Libraries: Pandas, TensorFlow, Spacy, NLTK, Matplotlib, Imblearn, NumPy, Scikit Learn
•  Framework & Tools: React.js, BigQuery, Github, Juypter Notebook, VS
•  Classes: Data Structures and Algorithms, Unix System, Probability and Statistics in Computer Science
""")
    print(req.findExperience())
    print(req.findEducation())
    print(req.findSkills())
    print(req.phone)
    print(req.address)
    print(req.gpa)
    print(req.websites)
    print(req.findSchools())
    print(req.majors)
    print(req.findEmail())
    print("~~~~~~~~~~~~~~~~~~~~")
    # req.calcScore()
    print(req)
if __name__ == "__main__":
    main()