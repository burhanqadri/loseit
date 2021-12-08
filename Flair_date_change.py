import ast
import datetime as dt
from textblob import TextBlob

g = open("authors_flairs_dates_fixed.txt", "a")

f = open("C:/Users/burha/Desktop/Weight Loss/Merged_loseitcomments_plus_topics.txt", "r")
# f = open("sample_loseit_posts.txt", "r")
# f = open("progresspics_comments.txt", "r")
# f = open("progresspics_posts.txt", "r")

cnt = 0
s = ""

authors = {}
author_posts = {}
has_flair = {}
date_flair = {}

for x in f:
    cnt = cnt + 1
    if cnt % 200000 == 0:
        print(cnt)
    s = x

    s_json = ast.literal_eval(s)

    this_author = s_json['author']
    this_author_flair = str(s_json['author_flair_text']).replace(',', '')
    this_post = s_json['id']
    # this_title_sentiment = TextBlob(s_json['title']).sentiment.polarity
    # this_selftext_sentiment = TextBlob(s_json['selftext']).sentiment.polarity
    this_date = s_json['created']
    this_date_readable = dt.datetime.fromtimestamp(
        int(this_date)
    ).strftime('%Y-%m-%d')

    # print(this_date_readable)
    # print(this_selftext_sentiment)
    # posts[this_post] = {}

    # check if author exists in our dictionary. Increment for how many times that author has posted
    if this_author in author_posts:
        authors[this_author] += 1
        author_posts[this_author].append(this_post)
    else:
        authors[this_author] = 1
        author_posts[this_author] = [this_post]

    # check if the author has a flair for how much weight they have lost
    if(not(this_author_flair == "None" or this_author_flair == "New") and len(this_author_flair) > 0):
        if this_author not in date_flair:
            has_flair[this_author] = this_author_flair
        date_flair[this_author] = this_date_readable

    # check which topics included
    # title_set = set(s_json['title'].split())
    # selftext_set = set(s_json['selftext'].split())
    # title_set & topic_set
    # selftext_set & topic_set

    # print(s_json['title'])
    # if(cnt > 9544):
    #     print(x)

# print(author_posts)
print(len(author_posts))

# prints out the top 100 posters
cntt = 0
for w in sorted(authors, key=authors.get, reverse=True):
    try:
        g.write(w + "," + has_flair[w] + "," + date_flair[w] + "\n")
        # print(w, authors[w], has_flair[w])
    except:
        g.write(w + ",None," + "\n")
        # print(w, authors[w], "No flair")
    # if cntt > 100:
    #     break
    # cntt += 1

print(cnt)
print(s)

f.close()
