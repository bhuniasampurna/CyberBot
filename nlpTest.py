import nltk
import string
import pandas as pd
import nlp_utils as nu
import matplotlib.pyplot as plt

'''
f = open("/home/sampurnab/Sampurna_Bhunia_1/College/College_Documents/Project/Personal_project/SBH_All/dialogs.txt")
print(f.read())
'''

df=pd.read_csv("/home/sampurnab/Sampurna_Bhunia_1/College/College_Documents/Project/Personal_project/SBH_All/dialogs.txt",names=('Query','Response'),sep=('\t'))

'''
df
df.shape
df.columns
df.info()
df.describe()
df.nunique()
df.isnull().sum()
df['Query'].value_counts()
df['Response'].value_counts()
'''

from nltk.sentiment.vader import SentimentIntensityAnalyzer
#nltk.downloader.download('vader_lexicon')
Text=df['Query']

'''
sid = SentimentIntensityAnalyzer()
for sentence in Text:
     print(sentence)
        
     ss = sid.polarity_scores(sentence)
     for k in ss:
         print('{0}: {1}, ' .format(k, ss[k]), end='')
     print()
'''

analyzer = SentimentIntensityAnalyzer()
df['rating'] = Text.apply(analyzer.polarity_scores)
df=pd.concat([df.drop(['rating'], axis=1), df['rating'].apply(pd.Series)], axis=1)
df

import re
punc_lower = lambda x: re.sub('[%s]' % re.escape(string.punctuation), ' ', x.lower())
remove_n = lambda x: re.sub("\n", " ", x)
remove_non_ascii = lambda x: re.sub(r'[^\x00-\x7f]',r' ', x)
alphanumeric = lambda x: re.sub('\w*\d\w*', ' ', x)
df['Query'] = df['Query'].map(alphanumeric).map(punc_lower).map(remove_n).map(remove_non_ascii)
df['Response'] = df['Response'].map(alphanumeric).map(punc_lower).map(remove_n).map(remove_non_ascii)
df
punc_lower = lambda x: re.sub('[%s]' % re.escape(string.punctuation), ' ', x.lower())
remove_n = lambda x: re.sub("\n", " ", x)
remove_non_ascii = lambda x: re.sub(r'[^\x00-\x7f]',r' ', x)
alphanumeric = lambda x: re.sub('\w*\d\w*', ' ', x)
df['Query'] = df['Query'].map(alphanumeric).map(punc_lower).map(remove_n).map(remove_non_ascii)
df['Response'] = df['Response'].map(alphanumeric).map(punc_lower).map(remove_n).map(remove_non_ascii)

'''
df
pd.set_option('display.max_rows',3800)
df
imp_sent=df.sort_values(by='compound', ascending=False)
imp_sent.head(5)
pos_sent=df.sort_values(by='pos', ascending=False)
pos_sent.head(5)
neg_sent=df.sort_values(by='neg', ascending=False)
neg_sent.head(5)
'''

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer()
factors = tfidf.fit_transform(df['Query']).toarray()
tfidf.get_feature_names_out ()

from sklearn.metrics.pairwise import cosine_distances
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

query = 'who are you ?'
def chatbot(query):
    # step:-1 clean
    query = lemmatizer.lemmatize(query)
    # step:-2 word embedding - transform
    query_vector = tfidf.transform([query]).toarray()
    # step-3: cosine similarity
    similar_score = 1 -cosine_distances(factors,query_vector)
    index = similar_score.argmax() # take max index position
    # searching or matching question
    matching_question = df.loc[index]['Query']
    response = df.loc[index]['Response']
    pos_score = df.loc[index]['pos']
    neg_score = df.loc[index]['neg']
    neu_score = df.loc[index]['neu']
    confidence = similar_score[index][0]
    chat_dict = {'match':matching_question,
                'response':response,
                'score':confidence,
                'pos':pos_score,
                'neg':neg_score,
                'neu':neu_score}
    return chat_dict

import nltk
#nltk.download('wordnet')
query = 'hi'
response = chatbot(query)
print(response)
query = 'I want to register a cyber crime'
print(query)
if query == 'exit':
    pass
    
response = chatbot(query)
if response['score'] <= 0.2: 
    print('BOT: Please rephrase your Question.')

else:
    print('='*80)
    print('logs:\n Matched Question: %r\n Confidence Score: %0.2f \n PositiveScore: %r \n NegativeScore: %r\n NeutralScore: %r'%(response['match'],response['score']*100,response['pos'],response['neg'],response['neu']))
    print('='*80)
    print('BOT: ',response['response'])

