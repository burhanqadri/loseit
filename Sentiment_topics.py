# over months
import ast
import datetime as dt
from textblob import TextBlob

f = open("C:/Users/burha/Desktop/Weight Loss/Merged_loseitcomments_plus_topicsAMENDED.txt", "r")
g = open("authors_flairs_dates.txt", "r")

writefile = open("time_topics_frequency.txt", "a")

cnt = 0
s = ""

authors = {}
author_posts = {}
has_flair = {}
date_flair = {}

time_topics_sentiment = {}
author_topics_sentiment = {}

for x in g:
    components = x.split(",")
    this_author = components[0]
    try:
        if len(components) > 2 and components[-1][4] == '-':
            date_flair[this_author] = components[-1].strip()
    except:
        continue

for x in f:
    cnt = cnt + 1
    # if cnt > 100000:
    #     break
    s_json = ast.literal_eval(x)
    # print(s_json)

    this_author = s_json['author']
    # this_author_flair = str(s_json['author_flair_text'])
    this_date = s_json['created']
    this_body_sentiment = s_json['body_sentiment']
    this_topics_sentiment = s_json['body_topics']
    this_date_readable = dt.datetime.fromtimestamp(
        int(this_date)
    ).strftime('%m')
    # ).strftime('%Y-%m')
    # ).strftime('%Y-%m-%d')

    if this_author not in author_topics_sentiment:
        author_topics_sentiment[this_author] = {}

    counter = 0
    for item in this_topics_sentiment:
        counter += 1
        if counter not in author_topics_sentiment[this_author]:
            author_topics_sentiment[this_author][counter] = {}
        if counter not in time_topics_sentiment:
            time_topics_sentiment[counter] = {}
        if(not(item == -10)):
            if this_date_readable in time_topics_sentiment[counter]:
                time_topics_sentiment[counter][this_date_readable].append(item)
            else:
                time_topics_sentiment[counter][this_date_readable] = [item]

            # if this_date_readable in author_topics_sentiment[this_author][counter]:
            #     author_topics_sentiment[this_author][counter][this_date_readable].append(
            #         item)
            # else:
            #     author_topics_sentiment[this_author][counter][this_date_readable] = [
            #         item]

            # sentiment_forAuthor[this_author].append(this_body_sentiment)

            #     if this_author in date_flair:
            #         if(this_date_readable <= date_flair[this_author]):
            #             try:
            #                 sentiment_beforeFlair[this_author].append(this_body_sentiment)
            #             except:
            #                 sentiment_beforeFlair[this_author] = [this_body_sentiment]
            #         else:
            #             try:
            #                 sentiment_afterFlair[this_author].append(this_body_sentiment)
            #             except:
            #                 sentiment_afterFlair[this_author] = [this_body_sentiment]
            #         # print(this_date_readable, date_flair[this_author])

            #     # # check if author exists in our dictionary. Increment for how many times that author has posted
            #     # if this_author in author_posts:
            #     #     authors[this_author] += 1
            #     #     author_posts[this_author].append(this_post)
            #     # else:
            #     #     authors[this_author] = 1
            #     #     author_posts[this_author] = [this_post]

            # counter1 = 0
            # counter2 = 0
for counter in time_topics_sentiment:
    for month in time_topics_sentiment[counter]:
        try:
            avg_sent = sum(
                time_topics_sentiment[counter][month])/len(time_topics_sentiment[counter][month])
            print(counter, month, len(
                time_topics_sentiment[counter][month]), avg_sent)
        except:
            continue

            # print(counter1, counter2)
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
