import nltk

pos_tweets = []
neg_tweets = []

positiveReviewsFileName = "path to pos data"
negativeReviewsFileName = "path to neg data"

# Read pos and neg sentences
with open(positiveReviewsFileName,'r') as f:
    positiveReviews = f.readlines()

with open(negativeReviewsFileName,'r') as f:
    negativeReviews = f.readlines()

# Split data into training and test data
testTrainingSplitIndex = 250
neg_tweets_tr = negativeReviews[:testTrainingSplitIndex]
pos_tweets_tr = positiveReviews[:testTrainingSplitIndex]

for l in pos_tweets_tr:
    pos_tweets.append((l, 'positive'))

for l in neg_tweets_tr:
    neg_tweets.append((l,'negative'))

#Take pos and neg and create a single list
tweets = []
for (words, sentiment) in pos_tweets + neg_tweets:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
    tweets.append((words_filtered, sentiment))


#The list of word features need to be extracted from the tweets. It is a list
# with every distinct words ordered by frequency of appearance. We use the following
# function to get the list plus the two helper functions.

def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
	# -------------------------------------------------------
	# Left this comment intentionally to show freq distribution
	# -------------------------------------------------------
    #for key, value in wordlist.most_common(20):
    #    print(key, value)
	
    word_features = wordlist.keys()
    return word_features

word_features = get_word_features(get_words_in_tweets(tweets))


#return dictionary indicating what words are contained in the input that was passed
def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

training_set = nltk.classify.apply_features(extract_features, tweets)
classifier = nltk.NaiveBayesClassifier.train(training_set)

#TEST
pos = 0
neg = 0

testdata = []
with open('path to your test data') as tdata:
    for row in tdata:
        row = row.split('|')
        testdata.append((row[0].strip(), row[1].strip()))

for row in testdata:
    sent = classifier.classify(extract_features(row[0].split()))
    if sent == 'positive':
        pos +=1
    if sent == 'negative':
        neg +=1

print("Positive: {0}".format(pos))
print("Negative: {0}".format(neg))

