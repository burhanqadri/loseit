import ast
import itertools
import datetime as dt
from textblob import TextBlob

date_flair = {}
flairFile = open("authors_flairs_dates.txt", "r")

for x in flairFile:
    components = x.split(",")
    this_author = components[0]
    try:
        if len(components) > 2 and components[-1][4] == '-':
            date_flair[this_author] = components[-1].strip()
    except:
        continue

g = open("subreddits_overlap.txt", "a")

# C:/Users/burha/Desktop/Weight Loss/
f = open("C:/Users/burha/Desktop/Weight Loss/authors_loseit_comments.txt", "r")

cnt = 0

authors = {}
subreddits = {}
frequency = {}

numDiet = {}
numFitness = {}

subreddit_pairs = {}

for line in f:
    cnt += 1
    if cnt > 1000:
        break
    username = (line.strip())
    sub_dict = {}
    subreddits = set()
    filename = "C:/Users/burha/Desktop/Weight Loss/User_post_files/" + \
        username + "_posts.txt"

    try:
        h = open(filename, "r")
        for x in h:
            s_json = ast.literal_eval(x)
            this_subreddit = str(s_json['subreddit'])
            subreddits.add(this_subreddit)

            if this_subreddit in sub_dict:
                sub_dict[this_subreddit] += 1
            else:
                sub_dict[this_subreddit] = 1

            # if this_subreddit in listOf_Diet:
            #     try:
            #         numDiet[username] += 1
            #     except:
            #         numDiet[username] = 1

        combos_list_2 = list(itertools.combinations(subreddits, 2))
        # combos_list_3 = list(itertools.combinations(subreddits, 3))
        # print(combos_list_2)

        for pair in combos_list_2:
            pair_string = str(pair)
            # print(pair_string)
            if pair_string in frequency:
                frequency[pair_string] += 1
            else:
                frequency[pair_string] = 1

        # communities_counter = 0
        # communities_ATLEAST5_counter = 0
        # dict_string = "{"
        # for w in sorted(sub_dict, key=sub_dict.get, reverse=True):
        #     communities_counter += 1
        #     if(sub_dict[w] >= 5):
        #         communities_ATLEAST5_counter += 1
        #     dict_string = dict_string + str(w) + ": " + str(sub_dict[w]) + ", "
        # dict_string = dict_string[:-2]
        # print(communities_counter, communities_ATLEAST5_counter)
        # g.write(dict_string + "}\n")

    except:
        continue

# prints out the top 100 posters
cntt = 0
for w in sorted(frequency, key=frequency.get, reverse=True):
    try:
        print(w, ": ", frequency[w])
    except:
        print("Error")
    if cntt > 200:
        break
    cntt += 1

f.close()
h.close()
g.close()
