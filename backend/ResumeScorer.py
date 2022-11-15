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

    # Score the resume based on the average of each grammar score from each sentence.
    def grammarScore(self, resumeText):
        sentenceArray = self.convertToSentenceArr(resumeText)
        individualScore = []
        for x in sentenceArray:
            errors = tool.check(x)
            numErrors = len(errors)
            countOfWords = len(x.split())
            individualScore.append(
                pow(((countOfWords - numErrors)/countOfWords), 3))
        cumulativeScore = (sum(individualScore)/len(individualScore))
        return cumulativeScore

        minScore = 0
        minScoreIndex = 0
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
        return cumulativeScore, sentenceArray[minScoreIndex]

    def wordChoiceScore(self, resumeText):
        sentenceArray = self.convertToSentenceArr(resumeText)
        score = len(sentenceArray)
        for x in sentenceArray:
            input_token = nltk.word_tokenize(x)
            result = nltk.pos_tag(input_token)
            print("Result: {}".format(result))
            first_word_result = result[0]
            first_word_code = first_word_result[1]
            if first_word_code not in self.VERB_CODES:
                score -= 1
        score = score / len(sentenceArray)
        if score < 0.33:
            print(
                "Your word choice is very poor, try using more professional words and better tense")
        elif score < 0.66:
            print("Your word choice is OK, try to improve certain words")
        else:
            print("Your word choice is amazing!")
