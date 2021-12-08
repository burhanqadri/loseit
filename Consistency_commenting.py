import ast
import datetime as dt

# f = open("C:/Users/burha/Desktop/Weight Loss/Merged_loseitcomments_plus_topics.txt", "r")
f = open("C:/Users/burha/Desktop/Weight Loss/Merged_loseitcomments_plus_topics.txt", "r")
g = open("authors_flairs_dates.txt", "r")

writefile = open("authors_consistency.txt", "a")

cnt = 0
s = ""

authors = {}
date_flair = {}

lastSeen = {}
first_post = {}
consistency_tracker = {}
helper_lastMonthPosted = {}

month_posts = {}

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
    if cnt > 100000:
        break
    s = x

    s_json = ast.literal_eval(s)

    this_author = s_json['author']
    this_author_flair = str(s_json['author_flair_text'])
    # this_author_link_flair = str(s_json['link_flair_text'])
    this_date_readable = dt.datetime.fromtimestamp(
        int(s_json['created'])
    ).strftime('%y-%m')
    # print(this_date_readable)

    first_post[this_author] = this_date_readable

    # check if author exists in our dictionary. Increment for how many times that author has posted
    if this_author in consistency_tracker:
        if this_date_readable in consistency_tracker[this_author]:
            consistency_tracker[this_author][this_date_readable] += 1
        else:
            consistency_tracker[this_author][this_date_readable] = 1
    else:
        consistency_tracker[this_author] = {}
        consistency_tracker[this_author][this_date_readable] = 1

    # date of last recorded comment by this author
    if this_author not in lastSeen:
        lastSeen[this_author] = this_date_readable
    else:
        continue

# remove authors whose last date is within 6 months of start of 2015 since their data might be cutoff
for author in lastSeen:
    if first_post[this_author] < "16-01":
        continue
    writefile.write(lastSeen[author] + ", " + first_post[this_author] + "\n")
    writefile.write(str(consistency_tracker[author]) + "\n")

    # print(lastSeen[author], first_post[this_author])
    # print(consistency_tracker[author])
# for key in first_post:
#     x = first_post[key]
#     try:
#         month_first_post[x] += 1
#     except:
#         month_first_post[x] = 1

f.close()
