import language_tool_python
tool = language_tool_python.LanguageTool('en-US')
import re
import nltk

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

    VERB_CODES = {
        'VBD',  # Verb, past tense
        'VBG',  # Verb, gerund or present participle
        'VBN',  # Verb, past participle
    }

    # Score the resume based on the average of each grammar score from each sentence.
    def grammarScore(self, resumeText):
        sentenceArray = self.convertToSentenceArr(resumeText)
        individualScore = []
        minIndex = 0
        minScoreIndex = 0
        wordScore = len(sentenceArray)
        for idx, x in enumerate(sentenceArray):
            errors = tool.check(x)
            numErrors = len(errors)
            countOfWords = len(x.split())
            individualScore.append(
                pow(((countOfWords - numErrors)/countOfWords), 3))
            if individualScore[-1] < individualScore[minScoreIndex]:
                minScore = individualScore[-1]
                minScoreIndex = idx
        cumulativeScore = (sum(individualScore)/len(individualScore))
        return {
            "Score": cumulativeScore,
            "Description": "This sentence: \"" + sentenceArray[minScoreIndex] + "\" has a grammer score of " + str(round(individualScore[minScoreIndex] * 100, 1)) + "/100."
            }

    def wordScore(self, resume):
        sentenceArray = self.convertToSentenceArr(resume)
        wordScore = len(sentenceArray)
        for x in sentenceArray:
            input_token = nltk.word_tokenize(resume)
            result = nltk.pos_tag(input_token)
            #print("Result: {}".format(result))
            first_word_result = result[0]
            first_word_code = first_word_result[1]
            if first_word_code not in self.VERB_CODES:
                wordScore -= 1
        finalWordScore = wordScore/len(sentenceArray)

        message = ""

        if finalWordScore <= 0.33:
            message = "Your word choice is very poor, try using more professiona words"
        elif finalWordScore <= 0.66:
            message = "Your word choice is good, but some improvements can be made"
        else:
            message = "Your word choice is amazing"
        return {
            "Score": finalWordScore,
            "Description": message
        }

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