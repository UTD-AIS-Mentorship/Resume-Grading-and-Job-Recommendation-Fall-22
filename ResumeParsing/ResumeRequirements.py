import re
import pandas as pd

#education
#address
#experience: employer, dates, company name, bullet points
#skills
#phone number
#websites: github, linkedin, personal website
#relavant courses
#gpa
#name
class requirements():
    resume = ""
    score = 0
    gpa = ""
    phone = ""
    address = ""
    websites = []

    def __init__(self, resume):
        self.resume = resume
        self.gpa = self.findGPA()
        self.address = self.findStreetAddress()
        self.phone = self.findPhone()
        self.findWebsites()

    def __str__(self):
        return f"requirement score: {self.score}/100.0"

    def findEducation(self):
        return bool(re.search(r"(education)", self.resume.lower()))

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
        pattern = re.compile(r"\b\d{1,6} +.{2,25}\b(avenue|ave|court|ct|street|st|drive|dr|lane|ln|road|rd|blvd|plaza|parkway|pkwy|suite|park|pk)[.,]?(.{0,25} +\b\d{5}\b)?")
        matches = pattern.finditer(self.resume.lower())
        for match in matches:
            return match.group(0)

    def findWebsites(self):
        pattern = re.compile(r"[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z()]{1,6}\b([-a-zA-Z0-9()@:%_\+~#?&=\/]*)\b")
        matches = pattern.finditer(self.resume.lower())
        for match in matches:
            self.websites.append(match.group(0))

    def findGPA(self):
        pattern = re.compile(r"\b\d{1,10}\.\d{1,10}(\/\d{1,10}\.\d{1,10})?\b")
        matches = pattern.finditer(self.resume.lower())
        for match in matches:
            return match.group(0)

    def printWebsites(self):
        for site in self.websites:
            print(site)

    def calcScore(self):
        if self.findEducation():
            self.score += 20
        else:
            print("no education found")
        if self.findExperience():
            self.score += 100
        else:
            print("no experience found")
        if self.findSkills():
            self.score += 30
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
        if self.address is not None:
            self.score += 5
        else:
            print("no address number found")
        self.score = self.score/165*100
def main():
    df = pd.read_csv("../Count_Vectorize_Resume_Linkedin_Keywords/resume.csv")
    # req = requirements(df["Resume_str"][0])
    req = requirements("(832) 943-6612")
    print(req.findExperience())
    print(req.findEducation())
    print(req.findSkills())
    print(req.phone)
    print(req.address)
    print(req.gpa)
    req.printWebsites()
    print("~~~~~~~~~~~~~~~~~~~~")
    req.calcScore()
    print(req)
if __name__ == "__main__":
    main()