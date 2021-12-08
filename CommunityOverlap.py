import ast
import itertools
import datetime as dt
from textblob import TextBlob

# make list of all F authors
# make list of all M authors
auths_f = []
auths_m = []

temp = open("f_authors.txt", "r")
for lin in temp:
    auths_f.append(lin.strip())
temp.close()

temp = open("m_authors.txt", "r")
for lin in temp:
    auths_m.append(lin.strip())
temp.close()

g = open("subreddits_overlap.txt", "a")

# C:/Users/burha/Desktop/Weight Loss/
# f = open("C:/Users/burha/Desktop/Weight Loss/authors_loseit_comments.txt", "r")
f = open("C:/Users/burha/Desktop/Weight Loss/authors_gendered.txt", "r")

cnt = 0

authors = {}
subreddits = {}
frequency = {}
F_frequency = {}
M_frequency = {}

all_count = 0
f_count = 0
m_count = 0

numDiet = {}
numFitness = {}

subreddit_pairs = {}

for line in f:
    cnt += 1
    # if cnt > 500:
    #     break
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

        h.close()

        combos_list_2 = list(itertools.combinations(subreddits, 2))
        # combos_list_3 = list(itertools.combinations(subreddits, 3))
        # print(combos_list_2)
        all_count += 1
        for pair in combos_list_2:
            pair_string = str(pair)
            # print(pair_string)
            if pair_string in frequency:
                frequency[pair_string] += 1
            else:
                frequency[pair_string] = 1

        if username in auths_f:
            f_count += 1
            for pair in combos_list_2:
                pair_string = str(pair)
                if pair_string in F_frequency:
                    F_frequency[pair_string] += 1
                else:
                    F_frequency[pair_string] = 1

        elif username in auths_m:
            m_count += 1
            for pair in combos_list_2:
                pair_string = str(pair)
                if pair_string in M_frequency:
                    M_frequency[pair_string] += 1
                else:
                    M_frequency[pair_string] = 1
            # print(F_frequency)

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

print(all_count)
for w in sorted(frequency, key=frequency.get, reverse=True):
    try:
        print(w, ": ", frequency[w])
    except:
        print("Error")
    if cntt > 50:
        break
    cntt += 1

print("******************FFFFFFFFFFFFFFFF**********************************")
print(f_count)
for ww in sorted(F_frequency, key=F_frequency.get, reverse=True):
    try:
        # print(ww, ": ", F_frequency[ww])
        pairing = str(ww).replace("'", "").replace(
            ",", "")[1:-1]
        comps = pairing.split(" ")
        print(comps[0] + "," + comps[1] + "," + str(F_frequency[ww]))
    except:
        print("Error")
    if cntt > 250:
        break
    cntt += 1
print("******************MMMMMMMMMMMMMMMM**********************************")
print(m_count)
for www in sorted(M_frequency, key=M_frequency.get, reverse=True):
    try:
        pairing = str(www).replace("'", "").replace(
            ",", "")[1:-1]
        comps = pairing.split(" ")
        print(comps[0] + "," + comps[1] + "," + str(M_frequency[www]))
    except:
        print("Error")
    if cntt > 450:
        break
    cntt += 1

f.close()
h.close()
g.close()
