from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()

def print_sentiment_scores(sentence):
    snt = analyser.polarity_scores(sentence)
    return snt['compound']

text = []
text.append(('Awesome movie'))
text.append(('Awesome movie!'))
text.append(('Awesome movie!!!'))
text.append(('That was good'))
text.append(('That was good :)'))
text.append(('That was good :('))
text.append(('Pay the piper'))

for row in text:
    sent = print_sentiment_scores(row)
    print('Text: {1}   Compound Score: {0}'.format(sent, row))





