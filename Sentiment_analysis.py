# Creating a pandas dataframe from reviews.txt file
from textblob import TextBlob
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk import pos_tag
from nltk.tokenize import word_tokenize
import nltk
import pandas as pd
import numpy as np
import re

# Define a function to clean the text


def clean(text):
    # Removes all special characters and numericals leaving the alphabets
    text = re.sub('[^A-Za-z]+', ' ', text)
    return text


# # Cleaning the text in the review column

# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('averaged_perceptron_tagger')

# POS tagger dictionary
pos_dict = {'J': wordnet.ADJ, 'V': wordnet.VERB,
            'N': wordnet.NOUN, 'R': wordnet.ADV}


def token_stop_pos(text):
    tags = pos_tag(word_tokenize(text))
    newlist = []
    for word, tag in tags:
        if word.lower() not in set(stopwords.words('english')):
            newlist.append(tuple([word, pos_dict.get(tag[0])]))
    return newlist


wordnet_lemmatizer = WordNetLemmatizer()


def lemmatize(pos_data):
    lemma_rew = " "
    for word, pos in pos_data:
        if not pos:
            lemma = word
            lemma_rew = lemma_rew + " " + lemma
        else:
            lemma = wordnet_lemmatizer.lemmatize(word, pos=pos)
            lemma_rew = lemma_rew + " " + lemma
    return lemma_rew


# # function to calculate subjectivity


def getSubjectivity(review):
    return TextBlob(review).sentiment.subjectivity
    # function to calculate polarity


def getPolarity(review):
    return TextBlob(review).sentiment.polarity

# function to analyze the reviews


def analysis(score):
    if score < 0:
        return 'Negative'
    elif score == 0:
        return 'Neutral'
    else:
        return 'Positive'


# sample = "The amazing thing is, in the past if I'd been 9 and a half stone I'd be disgusted with myself, I'd be really heavy, and now I was jubilant because I felt I was really light. It's all relative."
sample = "I have still got a certain amount of caution about it all. But you've got to have a happy medium between encouraging yourself and whacking yourself over the head."
# sample = "When I got down to 10 stone, I felt really slim. But after a few weeks I started feeling fat again. I used to think it would be wonderful to get down to a size 14, but once I did, I wanted to get to a size 12, or even a 10."
# sample = "…I was so emotionally involved with trying to lose weight and trying to be something I couldn't be, I let go of everything else. The weight thing takes over your life… I see parallels with anorexia. They live around their bodies, as we do, but on the other side of the scale."

# cleaned_sample = clean(sample)
# tokenized = token_stop_pos(cleaned_sample)
# print(lemmatize(tokenized))
print(getPolarity(sample))
