from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()

def print_sentiment_scores(sentence):
    snt = analyser.polarity_scores(sentence)
    return snt['compound']

pos = 0
neg = 0
neut = 0
    
with open('path to your file containing tweets') as tdata:
    for row in tdata:
        sent = print_sentiment_scores(row)
        if sent > 0:
            pos += 1            
        if sent == 0:
            neut += 1            
        if sent < 0:
            neg += 1            

print('Positive: {0}'.format(str(pos)))
print('Negative: {0}'.format(str(neg)))
print('Neutral: {0}'. format(str(neut)))




