import ast
import datetime as dt
from textblob import TextBlob

f = open("C:/Users/burha/Desktop/Weight Loss/Merged_loseitcomments_plus_topics.txt", "r")
g = open("authors_flairs_dates.txt", "r")

cnt = 0
s = ""

authors = {}
author_posts = {}
has_flair = {}
date_flair = {}

sentiment_beforeFlair = {}
sentiment_afterFlair = {}


for x in g:
    components = x.split(",")
    this_author = components[0]
    try:
        if len(components) > 2 and components[-1][4] == '-':
            date_flair[this_author] = components[-1].strip()
            # print(date_flair[this_author])
    except:
        continue


for x in f:
    cnt = cnt + 1
    # if cnt > 100000:
    #     break
    s_json = ast.literal_eval(x)

    this_author = s_json['author']
    # this_author_flair = str(s_json['author_flair_text'])
    this_post = s_json['id']
    this_date = s_json['created']
    this_body_sentiment = s_json['body_sentiment']
    this_date_readable = dt.datetime.fromtimestamp(
        int(this_date)
    ).strftime('%Y-%m-%d')

    if this_author in date_flair:
        if(this_date_readable <= date_flair[this_author]):
            try:
                sentiment_beforeFlair[this_author].append(this_body_sentiment)
            except:
                sentiment_beforeFlair[this_author] = [this_body_sentiment]
        else:
            try:
                sentiment_afterFlair[this_author].append(this_body_sentiment)
            except:
                sentiment_afterFlair[this_author] = [this_body_sentiment]
        # print(this_date_readable, date_flair[this_author])

    # # check if author exists in our dictionary. Increment for how many times that author has posted
    # if this_author in author_posts:
    #     authors[this_author] += 1
    #     author_posts[this_author].append(this_post)
    # else:
    #     authors[this_author] = 1
    #     author_posts[this_author] = [this_post]

counter1 = 0
counter2 = 0
for person in sentiment_afterFlair:
    try:
        beforeSentiment = sum(
            sentiment_beforeFlair[person])/len(sentiment_beforeFlair[person])
        afterSentiment = sum(
            sentiment_afterFlair[person])/len(sentiment_afterFlair[person])

        if(beforeSentiment > afterSentiment):
            counter1 += 1
        else:
            counter2 += 1
        # print(person,
        #       beforeSentiment, afterSentiment)
    except:
        continue

print(counter1, counter2)
# # prints out the top 100 posters
# cntt = 0
# for w in sorted(authors, key=authors.get, reverse=True):
#     try:
#         g.write(w + "," + has_flair[w] + "," + date_flair[w] + "\n")
#         # print(w, authors[w], has_flair[w])
#     except:
#         g.write(w + ",None" + "\n")
#         # print(w, authors[w], "No flair")
#     # if cntt > 100:
#     #     break
#     # cntt += 1

f.close()
g.close()
