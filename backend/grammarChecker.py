import language_tool_python
tool = language_tool_python.LanguageTool('en-US')

def grammarScore(resume):
    errors = tool.check(resume)
    numErrors = len(errors)
    countOfWords = len(resume.split())
    score = ((countOfWords - numErrors)/countOfWords)
    return score
resume = input("Enter the resume: ")
print("The grammar score is ", grammarScore(resume))
