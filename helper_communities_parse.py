import ast
import timeit
import datetime as dt
from textblob import TextBlob

listOf_Diet = []
listOf_Fitness = []
listOf_Food = []

# g = open("authors_loseit_posts.txt", "a")
# g = open("all_communities.txt", "r")
g = open("all_communities_includingamount.txt", "r")
# gg = open("all_communities_before_loseit.txt", "r")
# gg = open("all_communities_before_progresspics.txt", "a")


# f = open("C:/Users/burha/Desktop/Weight Loss/authors_loseit_comments.txt", "r")
# f = open("C:/Users/burha/Desktop/Weight Loss/authors_progresspics_posts.txt", "r")

cnt = 0
s = ""

authors = {}
# subreddits = {}

# numDiet = {}
# numFitness = {}

for line in g:
    # cnt += 1
    # if cnt > 20:
    #     break
    line = line.strip()
    components = line.split(",")
    author = components[0]
    subs = components[1].split("|")

    print(subs)

    # for sub in subs:
    #     sub_list = sub.split(":")
    #     sub_name = sub_list[0]
    #     sub_count = sub_list[1]
    #     print(sub_name, sub_count)

g.close()
