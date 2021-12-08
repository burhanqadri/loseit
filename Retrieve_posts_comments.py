# import praw
import datetime as dt
import ast
from psaw import PushshiftAPI

api = PushshiftAPI()

start_epoch = int(dt.datetime(2018, 2, 28).timestamp())
end_epoch = int(dt.datetime(2018, 3, 31).timestamp())
# gen = api.search_submissions(after=start_epoch, before=end_epoch, subreddit='loseit', filter=[
#     'url', 'author', 'author_flair_text', 'is_robot_indexable', 'id', 'num_comments', 'is_original_content', 'is_self', 'score', 'selftext', 'title', 'subreddit', 'subreddit_subscribers', 'upvote_ratio'])

gen = api.search_comments(after=start_epoch, before=end_epoch, subreddit='loseit', filter=['author', 'author_flair_text', 'body', 'controversiality', 'gilded', 'id', 'is_submitter', 'link_id', 'parent_id', 'score', 'send_replies'
                                                                                           ])

# gen = api.search_comments(after=start_epoch, before=end_epoch, subreddit='progresspics', filter=[
#   'author', 'author_flair_text', 'body', 'controversiality', 'gilded', 'id', 'is_submitter', 'link_id', 'parent_id',  'score', 'send_replies'])

# gen = api.search_submissions(after=start_epoch, before=end_epoch, subreddit='progresspics', filter=[
#                              'author', 'author_flair_text', 'id', 'is_robot_indexable', 'is_self', 'link_flair_text',  'num_comments', 'score', 'selftext', 'send_replies', 'subreddit', subreddit_subscribers', 'title', 'upvote_ratio'])

max_response_cache = 100
cache = []


# f = open("progresspics_posts.txt", "a")
# f = open("progresspics_comments.txt", "a")
# f = open("loseit_posts.txt", "a")
f = open("loseit_comments_missing_months.txt", "a")

for c in gen:
    cache.append(c)

    try:
        cc = str(c)
        print(cc)
        loc = cc.find("d_={")
        # if "indexable=True" not in cc:
        #     continue
        f.write(cc[loc+3: -1]+"\n")
    except:
        continue

    if len(cache) >= max_response_cache:
        break

# # If you really want to: pick up where we left off to get the rest of the results.
# if False:
#     for c in gen:
#         cache.append(c)

f.close()
# # import praw
# import datetime as dt
# import ast
# from psaw import PushshiftAPI

# api = PushshiftAPI()

# start_epoch = int(dt.datetime(2015, 1, 1).timestamp())
# end_epoch = int(dt.datetime(2018, 3, 7).timestamp())
# gen = api.search_submissions(after=start_epoch, before=end_epoch, subreddit='loseit', filter=[
#     'url', 'author', 'author_flair_text', 'send_replies', 'is_robot_indexable', 'id', 'num_comments', 'is_original_content', 'is_self', 'score', 'selftext', 'title', 'subreddit', 'subreddit_subscribers', 'upvote_ratio'])

# # gen = api.search_comments(after=start_epoch, before=end_epoch, subreddit='loseit', filter=['author', 'author_flair_text', 'body', 'controversiality', 'gilded', 'id', 'is_submitter', 'link_id', 'parent_id', 'score', 'send_replies'
# #                                                                                            ])

# # gen = api.search_comments(after=start_epoch, before=end_epoch, subreddit='progresspics', filter=[
# #   'author', 'author_flair_text', 'body', 'controversiality', 'gilded', 'id', 'is_submitter', 'link_id', 'parent_id',  'score', 'send_replies'])

# # gen = api.search_submissions(after=start_epoch, before=end_epoch, subreddit='progresspics', filter=[
# #                              'author', 'author_flair_text', 'id', 'is_robot_indexable', 'is_self', 'link_flair_text',  'num_comments', 'score', 'selftext', 'send_replies', 'subreddit', subreddit_subscribers', 'title', 'upvote_ratio'])

# # max_response_cache = 10
# max_response_cache = 1000000

# cache = []


# # f = open("progresspics_posts.txt", "a")
# # f = open("progresspics_comments.txt", "a")
# # f = open("delete_loseit_posts.txt", "a")
# f = open("loseit_posts.txt", "a")
# # f = open("loseit_comments.txt", "a")

# for c in gen:
#     cache.append(c)

#     try:
#         cc = str(c)
#         loc = cc.find("d_={")
#         # if "indexable=True" not in cc:
#         #     continue
#         # if "send_replies=True" not in cc:
#         #     continue
#         if "[deleted]" in cc:
#             continue
#         f.write(cc[loc+3: -1]+"\n")
#     except:
#         continue

#     if len(cache) >= max_response_cache:
#         break

# # # If you really want to: pick up where we left off to get the rest of the results.
# # if False:
# #     for c in gen:
# #         cache.append(c)

# f.close()
