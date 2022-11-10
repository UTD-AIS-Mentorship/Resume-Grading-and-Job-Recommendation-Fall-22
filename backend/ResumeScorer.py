import language_tool_python
tool = language_tool_python.LanguageTool('en-US')
import re

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



