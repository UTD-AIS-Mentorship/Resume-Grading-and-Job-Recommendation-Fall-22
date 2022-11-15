import nltk
import re
import language_tool_python
tool = language_tool_python.LanguageTool('en-US')


class resumeScore:

    # Convert text resume to list of sentences that will be scored for grammar, diction, ETC.
    def convertToSentenceArr(self, textpdf):
        sentenceArr = re.split(r'[\|\n\•]', textpdf)
        sentenceArr = [x.strip() for x in sentenceArr]

        newArray = []
        for x in sentenceArr:
            numCommas = x.count(",")
            if len(x.split()) > 10 and (numCommas/len(x.split())) < 0.3:
                newArray.append(x)

        return newArray
    # Verb Codes
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
            if individualScore[-1] < minScore:
                minScore = individualScore[-1]
                minScoreIndex = idx
        cumulativeScore = (sum(individualScore)/len(individualScore))
        return cumulativeScore, minScoreIndex

    def wordScore(self, resume):
        sentenceArray = self.convertToSentenceArr(resume)
        wordScore = len(sentenceArray)
        for x in sentenceArray:
            input_token = nltk.word_tokenize(input)
            result = nltk.pos_tag(input_token)
            print("Result: {}".format(result))
            first_word_result = result[0]
            first_word_code = first_word_result[1]
            if first_word_code not in self.VERB_CODES:
                wordScore -= 1
            finalWordScore = wordScore/len(sentenceArray)
            if finalWordScore <= 0.33:
                print("Your word choice is very poor, try using more professiona words")
            elif finalWordScore <= 0.66:
                print("Your word choice is good, but some improvements can be made")
            else:
                print("Your word choice is amazing")
            return finalWordScore
