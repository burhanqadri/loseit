import ast
import datetime as dt

# f = open("C:/Users/burha/Desktop/Weight Loss/Merged_loseitcomments_plus_topics.txt", "r")
f = open("C:/Users/burha/Desktop/Weight Loss/progresspics_posts_w_sentiment.txt", "r")
g = open("authors_progresspics_stats.txt", "a")

cnt = 0

authors = {}
date_flair = {}

for x in f:
    # cnt = cnt + 1
    # if cnt > 100:
    #     break

    s_json = ast.literal_eval(x)

    this_author = s_json['author']
    this_title = str(s_json['title'])

    if this_author not in authors:
        authors[this_author] = "seen"
        try:
            pieces = this_title.split('/')
            if(len(pieces[0]) == 1 and len(pieces[1]) == 2):
                g.write(this_author + "," + pieces[0] + "," + pieces[1] + "\n")
                # print(, )
        except:
            print("not available ", this_title)

    # first_post[this_author] =

f.close()
g.close()
