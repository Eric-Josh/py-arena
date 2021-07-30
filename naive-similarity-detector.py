# Naïve similarity detector
# This can be used to identify collusion between students in their assessments.
# The program will read in two assessment submissions (two strings) in turn and output a similarity score for them.

commonWords=[]
uniqueWords=[]

firstSubmit = input('Enter the first submission: ')
secondSubmit = input('Enter the second submission: ')

# convert to lowercase to compare
firstSubmitSplit = firstSubmit.lower().split(' ')
secondSubmitSplit = secondSubmit.lower().split(' ')

# compare to get common words
for x in firstSubmitSplit:
    for y in secondSubmitSplit:
        if x in secondSubmitSplit and x not in commonWords:
            commonWords.append(x)
        elif y in firstSubmitSplit and y not in commonWords:
            commonWords.append(y)
            
# compare to get unique words
for x in firstSubmitSplit:
    for y in secondSubmitSplit:
        if x not in uniqueWords:
            uniqueWords.append(x)
        elif y not in uniqueWords:
            uniqueWords.append(y)


commonWordsCount=len(commonWords)
uniqueWordsCount=len(uniqueWords)            
similarityCal = (commonWordsCount*100)/uniqueWordsCount
    
print('The similarity score between the two is:',round(similarityCal,2),'%')