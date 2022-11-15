import language_tool_python
tool = language_tool_python.LanguageTool('en-US')
import re

from pdfminer.high_level import extract_text

class resumeScore:

    #Convert text resume to list of sentences that will be scored for grammar, diction, ETC.
    def convertToSentenceArr(self, textpdf):
        sentenceArr = re.split(r'[\|\n\•]', textpdf)
        sentenceArr = [x.strip() for x in sentenceArr]

        newArray = []
        for x in sentenceArr:
            numCommas = x.count(",")
            if len(x.split()) > 10 and (numCommas/len(x.split())) < 0.3:
                newArray.append(x)

        return newArray

    #Score the resume based on the average of each grammar score from each sentence.
    def grammarScore(self, resumeText):
        sentenceArray = self.convertToSentenceArr(resumeText)
        individualScore = []
        for x in sentenceArray:
            errors = tool.check(x)
            numErrors = len(errors)
            countOfWords = len(x.split())
            individualScore.append(pow(((countOfWords - numErrors)/countOfWords), 3))
        cumulativeScore = (sum(individualScore)/len(individualScore))
        return cumulativeScore

    def numericScore(self, resumeText):
        sentences = self.convertToSentenceArr(resumeText)
        numbers = re.findall(r'(\d+(?:[.,]\d+)|\d+)', " ".join(sentences))
        
        numOfNumbers = len(numbers)
        numOfSentences = len(sentences)  
        score = pow(min(1,(numOfNumbers/numOfSentences)), 2)

        message = ""
        if score < 0.7:
            message = "Use more quantifiable Metrics"
        elif score < 0.8:
            message = "Good usage Quantifiable Metrics, use more if possible"
        else:
            message = "Amazing use of Quantifable Metrics"


        return {'Score': score, "Description": message}

   



