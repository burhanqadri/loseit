import ast
import datetime as dt

# f = open("C:/Users/burha/Desktop/Weight Loss/Merged_loseitcomments_plus_topics.txt", "r")
f = open("C:/Users/burha/Desktop/Weight Loss/Merged_loseitcomments_plus_topics.txt", "r")
g = open("authors_flairs_dates.txt", "r")

cnt = 0
s = ""

authors = {}
date_flair = {}
lastSeen = {}

month_posts = {}

first_post = {}
month_first_post = {}

has_flair_first_post = {}
has_flair_month_first_post = {}

no_flair_first_post = {}
no_flair_month_first_post = {}

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
    # if cnt > 100:
    #     break
    s = x

    s_json = ast.literal_eval(s)

    this_author = s_json['author']
    this_author_flair = str(s_json['author_flair_text'])
    # this_author_link_flair = str(s_json['link_flair_text'])
    this_date_readable = dt.datetime.fromtimestamp(
        int(s_json['created'])
    ).strftime('%m')

    first_post[this_author] = this_date_readable

    try:
        month_posts[this_date_readable] += 1
    except:
        month_posts[this_date_readable] = 1

    # check if author exists in our dictionary. Increment for how many times that author has posted
    if this_author in authors:
        authors[this_author] += 1
    else:
        authors[this_author] = 1

    # date of last recorded comment by this author
    if this_author not in lastSeen:
        lastSeen[this_author] = this_date_readable

    # store date in has flair if author has a flair
    if this_author in date_flair:
        has_flair_first_post[this_author] = this_date_readable
    else:
        no_flair_first_post[this_author] = this_date_readable


for key in first_post:
    x = first_post[key]
    try:
        month_first_post[x] += 1
    except:
        month_first_post[x] = 1

for key in has_flair_first_post:
    x = has_flair_first_post[key]
    try:
        has_flair_month_first_post[x] += 1
    except:
        has_flair_month_first_post[x] = 1

for key in no_flair_first_post:
    x = no_flair_first_post[key]
    try:
        no_flair_month_first_post[x] += 1
    except:
        no_flair_month_first_post[x] = 1

sorted_month_posts = {key: value for key, value in sorted(month_posts.items())}
sorted_month_first_post = {key: value for key,
                           value in sorted(month_first_post.items())}
sorted_has_flair_month_first_post = {
    key: value for key, value in sorted(has_flair_month_first_post.items())}
sorted_no_flair_month_first_post = {
    key: value for key, value in sorted(no_flair_month_first_post.items())}

print(sorted_month_posts)
print(sorted_month_first_post)
print(sorted_has_flair_month_first_post)
print(sorted_no_flair_month_first_post)


# # prints out the top 100 posters
# cntt = 0
# for w in sorted(authors, key=authors.get, reverse=True):
#     try:
#         print(w, authors[w], has_flair[w])
#     except:
#         print(w, authors[w], "NA")
#     if cntt > 300:
#         break
#     cntt += 1

f.close()
