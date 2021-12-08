import ast
import timeit
import datetime as dt
from textblob import TextBlob

# g = open("authors_loseit_posts.txt", "a")
g = open("test1.txt", "a")
# g = open("authors_loseit_comments.txt", "a")


# f = open("loseit_comments.txt", "r")
# f = open("loseit_posts_w_sentiment.txt", "r")
f = open("lMerged_loseitcomments_w_sentiment.txt", "r")
# f = open("sample_loseit_posts_w_sentiment.txt", "r")
# f = open("sample_loseit_posts.txt", "r")
# f = open("progresspics_comments.txt", "r")
# f = open("progresspics_posts_w_sentiment.txt", "r")

cnt = 0
s = ""

authors = {}
author_posts = {}
posts = {}
has_flair = {}

start = timeit.default_timer()
for x in f:
    cnt = cnt + 1
    if(cnt % 100000 == 0):
        print(cnt)
    s = x

    s_json = ast.literal_eval(s)

    this_author = s_json['author']
    # this_author_flair = str(s_json['author_flair_text'])
    this_post = s_json['id']
    this_date_readable = dt.datetime.fromtimestamp(
        int(s_json['created'])
    ).strftime('%m')

    # check if author exists in our dictionary. Increment for how many times that author has posted
    if this_author in author_posts:
        authors[this_author] += 1
        author_posts[this_author].append(id)
    else:
        authors[this_author] = 1
        author_posts[this_author] = [id]

    # check if the author has a flair for how much weight they have lost
    # if(not(this_author_flair == "None" or this_author_flair == "New") and len(this_author_flair) > 0):
    #     has_flair[this_author] = this_author_flair


# prints out the top 100 posters
cntt = 0
for w in sorted(authors, key=authors.get, reverse=True):
    # try:
    #     print(w, authors[w], has_flair[w])
    # except:
    #     print(w, authors[w], "NA")
    g.write(str(w) + "," + str(authors[w]) + "\n")
    # g.write("\n")
    # if authors[w] <= 2:
    #     g.write("2**********************************************************")
    # elif authors[w] <= 5:
    #     g.write("3*******************************************")
    # elif authors[w] <= 10:
    #     g.write("10****************************")
    # elif authors[w] <= 25:
    #     g.write("25**************")
    # elif authors[w] <= 50:
    #     g.write("50*********")
    # elif authors[w] <= 100:
    #     g.write("100***")
    cntt += 1

f.close()
g.close()
