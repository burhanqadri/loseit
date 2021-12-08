import ast
import timeit
import datetime as dt
from textblob import TextBlob

listOf_Diet = []
listOf_Fitness = []
listOf_Food = []


# Author, flair, date flair changed

# g = open("authors_loseit_posts.txt", "a")
g = open("test1.txt", "a")
# g = open("authors_loseit_comments.txt", "a")

# C:/Users/burha/Desktop/Weight Loss/
f = open("C:/Users/burha/Desktop/Weight Loss/authors_loseit_comments.txt", "r")

cnt = 0
s = ""

authors = {}
subreddits = {}

numDiet = {}
numFitness = {}

for line in f:
    cnt += 1
    # if cnt > 2:
    #     break
    username = (line.strip())
    sub_dict = {}
    # filename = "C:/Users/burha/Desktop/Weight Loss/User_comment_files/" + username + "_comments.txt"
    filename = "C:/Users/burha/Desktop/Weight Loss/User_post_files/" + \
        username + "_posts.txt"

    try:
        h = open(filename, "r")
        for x in h:
            s_json = ast.literal_eval(x)
            this_subreddit = str(s_json['subreddit'])
            if this_subreddit in sub_dict:
                # print("1111111111111111111")
                sub_dict[this_subreddit] += 1
            else:
                # print("here instead")
                sub_dict[this_subreddit] = 1
                # subreddits[this_subreddit] = {this_subreddit: 1}

            if this_subreddit in listOf_Diet:
                try:
                    numDiet[username] += 1
                except:
                    numDiet[username] = 1

            elif this_subreddit in listOf_Fitness:
                try:
                    numFitness[username] += 1
                except:
                    numFitness[username] = 1

        communities_counter = 0
        communities_ATLEAST5_counter = 0
        dict_string = "{"
        for w in sorted(sub_dict, key=sub_dict.get, reverse=True):
            communities_counter += 1
            if(sub_dict[w] >= 5):
                communities_ATLEAST5_counter += 1
            dict_string = dict_string + str(w) + ": " + str(sub_dict[w]) + ", "
        dict_string = dict_string[:-1]
        print(communities_counter, communities_ATLEAST5_counter)
        g.write(dict_string + "}\n")

    except:
        continue
        # print(username)

    # this_author_flair = str(s_json['author_flair_text'])
    # this_post = s_json['id']
    # this_date_readable = dt.datetime.fromtimestamp(
    #     int(s_json['created'])
    # ).strftime('%m')

    # check if author exists in our dictionary. Increment for how many times that author has posted
    # if this_author in author_posts:
    #     authors[this_author] += 1
    #     author_posts[this_author].append(id)
    # else:
    #     authors[this_author] = 1
    #     author_posts[this_author] = [id]

    # check if the author has a flair for how much weight they have lost
    # if(not(this_author_flair == "None" or this_author_flair == "New") and len(this_author_flair) > 0):
    #     has_flair[this_author] = this_author_flair


# prints out the top 100 posters
# cntt = 0
# for w in sorted(authors, key=authors.get, reverse=True):
#     # try:
#     #     print(w, authors[w], has_flair[w])
#     # except:
#     #     print(w, authors[w], "NA")
#     g.write(str(w) + "," + str(authors[w]) + "\n")
#     cntt += 1

f.close()
h.close()
g.close()
