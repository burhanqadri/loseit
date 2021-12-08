import ast
import timeit
import datetime as dt
from textblob import TextBlob

# t_1 = {'water', 'drink', 'lot', 'drinking', 'make', 'soda',
#        'cut', 'diet', 'beer', 'bit', 'thing', 'alcohol', 'eat', 'food', 'meal', 'eating', 'lunch', 'dinner', 'hungry', 'calorie', 'breakfast', 'pizza', 'food', 'diet', 'eating', 'eat', 'low', 'protein', 'fat', 'calorie', 'lot', 'high', 'carbs', 'cico', 'veggie', 'chicken', 'salad', 'cheese', 'add', 'recipe', 'make', 'cook', 'egg', 'rice', 'meat'}

# t_2 = {'doctor', 'body', 'issue', 'problem', 'health',
#        'level', 'pain', 'energy', 'effect', 'surgery'}

# t_3 = {'friend', 'family', 'guy', 'kid', 'mom',
#        'school', 'husband', 'life', 'live', 'told', 'girl'}

# t_4 = {'calorie', 'deficit', 'exercise', 'tdee', 'eat',
#        'counting', 'count', 'eating', 'daily', 'mfp', 'calorie', 'chocolate', 'sugar', 'sweet', 'snack', 'coffee', 'craving', 'bar', 'fruit', 'cal', 'cup'}

# t_5 = {'run', 'running', 'walk', 'minute', 'time',
#        'walking', 'mile', 'step', 'hour', 'half', 'long', 'gym', 'exercise', 'muscle', 'workout', 'start', 'working', 'work', 'body', 'cardio'}

# t_6 = {'lb', 'year', 'lost', 'month', 'started', 'pound',
#        'back', 'ago', 'gained', 'weight', 'starting', 'weight', 'lose', 'loss', 'fat', 'body', 'gain', 'healthy', 'bmi', 'height', 'normal', 'range', 'week', 'scale', 'weight', 'pound', 'number', 'plateau', 'drop', 'weighing', 'daily'}

# t_7 = {'thing', 'work', 'make', 'find', 'lot', 'time',
#        'hard', 'put', 'give', 'won', 'easy', 'worry', 'goal', 'hit', 'progress', 'end', 'picture', 'feel', 'close', 'happy', 'set', 'time', 'challenge', 'feel', 'feeling', 'eating', 'binge', 'bad', 'stop', 'time', 'control', 'hard', 'stress', 'struggle'}

# t_8 = {'good', 'pretty', 'yeah', 'luck', 'lol', 'idea', 'feel', 'kind', 'sound', 'guess', 'bit', 'haha', 'stuff', 'people', 'person', 'health', 'comment', 'understand', 'talk', 'mental', 'life',
#        'care', 'post', 'read', 'check', 'https_www', 'question', 'loseit', 'app', 'mfp', 'reddit', 'http', 'great', 'love', 'awesome', 'job', 'amazing', 'congrats', 'hope', 'sound', 'glad', 'similar'}

# t_9 = {'day', 'week', 'back', 'track', 'maintenance',
#        'couple', 'plan', 'log', 'logging', 'cheat', 'change', 'time', 'make', 'start', 'long', 'life', 'habit', 'making', 'thing', 'choice', 'healthy', 'time', 'thought', 'made', 'felt', 'wanted', 'started', 'back', 'needed', 'decided', 'found'}

# t_10 = {'fit', 'size', 'clothes', 'big', 'wear', 'buy',
#         'pant', 'bought', 'short', 'shirt', 'dress', 'store'}

# t_11 = {'today', 'morning', 'night', 'yesterday',
#         'work', 'tomorrow', 'weekend', 'day', 'home'}

# topics_categories = [{'water', 'drink', 'drinking', 'soda', 'sugar', 'sweet', 'snack', 'coffee', 'craving',
#                       'diet', 'beer', 'alcohol', 'eat', 'food', 'meal', 'eating', 'lunch', 'dinner', 'hungry', 'calorie', 'breakfast', 'food', 'diet', 'eating', 'protein', 'carbs', 'veggie', 'recipe', 'cook'}, {'doctor', 'health',
#                                                                                                                                                                                                                    'pain', 'energy', 'surgery'}, {'friend', 'family', 'kid', 'mom',
#                                                                                                                                                                                                                                                   'school', 'husband', 'girlfriend'}, {'calorie', 'deficit', 'exercise', 'tdee', 'cico',
#                                                                                                                                                                                                                                                                                        'counting', 'count', 'mfp', 'cal'}, {'run', 'running', 'walk',
#                                                                                                                                                                                                                                                                                                                             'walking', 'mile', 'gym', 'exercise', 'muscle', 'workout', 'cardio'}, {'lb', 'lost', 'pound',
#                                                                                                                                                                                                                                                                                                                                                                                                    'gained', 'weight', 'starting', 'weight', 'lose', 'loss', 'fat', 'gain', 'bmi', 'height', 'range', 'scale', 'number', 'plateau', 'drop', 'weighing'}, {
#     'hard', 'won', 'easy', 'worry', 'goal', 'hit', 'progress', 'end', 'picture', 'feel', 'close', 'happy', 'set', 'challenge', 'feel', 'feeling', 'eating', 'binge', 'bad', 'stop', 'time', 'control', 'hard', 'stress', 'struggle'}, {'pretty', 'luck', 'understand', 'talk', 'mental',
#                                                                                                                                                                                                                                        'care', 'check', 'great', 'love', 'awesome', 'job', 'amazing', 'congrats', 'hope', 'glad'}, {'day', 'week', 'track', 'maintenance',
#                                                                                                                                                                                                                                                                                                                                     'plan', 'log', 'logging', 'time', 'start', 'habit', 'choice', 'healthy', 'time', 'thought', 'felt', 'wanted', 'started', 'back', 'needed', 'decided', 'found'}, {'fit', 'size', 'clothes', 'big', 'wear', 'buy',
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      'pant', 'bought', 'shirt', 'dress', 'store'}, {'today', 'morning', 'night', 'yesterday',
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     'work', 'tomorrow', 'weekend', 'day'}, {'quarantine', 'lockdown', 'covid', 'coronavirus', 'home', 'inside'
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             }]

topics_categories = {'water', 'drink', 'drinking', 'soda', 'sugar', 'sweet', 'snack', 'coffee', 'craving',
                     'diet', 'beer', 'alcohol', 'eat', 'food', 'meal', 'eating', 'lunch', 'dinner', 'hungry', 'calorie', 'breakfast', 'food', 'diet', 'eating', 'protein', 'carbs', 'veggie', 'recipe', 'cook', 'doctor', 'health',
                     'pain', 'energy', 'surgery', 'friend', 'family', 'kid', 'mom',
                     'school', 'husband', 'girlfriend', 'calorie', 'deficit', 'exercise', 'tdee', 'cico',
                     'counting', 'count', 'mfp', 'cal', 'run', 'running', 'walk',
                     'walking', 'mile', 'gym', 'exercise', 'muscle', 'workout', 'cardio', 'lb', 'lost', 'pound', 'kg'
                     'gained', 'weight', 'starting', 'weight', 'lose', 'loss', 'fat', 'gain', 'bmi', 'height', 'range', 'scale', 'number', 'plateau', 'drop', 'weighing', 'hard', 'won', 'easy', 'worry', 'goal', 'hit', 'progress', 'end', 'picture', 'feel', 'close', 'happy', 'set', 'challenge', 'feel', 'feeling', 'eating', 'binge', 'bad', 'stop', 'time', 'control', 'hard', 'stress', 'struggle', 'pretty', 'luck', 'understand', 'talk', 'mental',
                     'care', 'check', 'great', 'love', 'awesome', 'job', 'amazing', 'congrats', 'hope', 'glad', 'day', 'week', 'track', 'maintenance',
                     'plan', 'log', 'logging', 'time', 'start', 'habit', 'choice', 'healthy', 'time', 'thought', 'felt', 'wanted', 'started', 'back', 'needed', 'decided', 'found', 'fit', 'size', 'clothes', 'big', 'wear', 'buy',
                     'pant', 'bought', 'shirt', 'dress', 'store', 'today', 'morning', 'night', 'yesterday',
                     'work', 'tomorrow', 'weekend', 'day', 'quarantine', 'lockdown', 'covid', 'coronavirus', 'home', 'inside'}

# g = open("authors_loseit_posts.txt", "a")
# g = open("authors_loseit_comments.txt", "a")
# g = open("Merged_loseitcomments_plus_topics.txt", "a")
g = open("Merged_loseitcomments_plus_topicsAMENDED.txt", "a")


# f = open("loseit_comments.txt", "r")
# f = open("loseit_posts_w_sentiment.txt", "r")
f = open("lMerged_loseitcomments_w_sentiment.txt", "r")
# f = open("sample_loseit_posts_w_sentiment.txt", "r")
# f = open("sample_loseit_posts.txt", "r")
# f = open("progresspics_comments.txt", "r")
# f = open("progresspics_posts.txt", "r")

cnt = 0
s = ""

authors = {}
author_posts = {}
posts = {}
has_flair = {}

start = timeit.default_timer()
for x in f:
    cnt = cnt + 1
    # print(x)
    # if cnt > 100:
    #     break
    if(cnt % 100000 == 0):
        print(cnt)
    s = x

    s_json = ast.literal_eval(s)

    # this_author = s_json['author']
    # this_author_flair = str(s_json['author_flair_text'])
    # this_post = s_json['id']
    this_body = set(s_json['body'].split())
    this_body_sentiment = s_json['body_sentiment']
    # this_title = set(s_json['title'].split())
    # this_selftext = set(s_json['selftext'].split())

    # overlap_1 = t_1 and this_selftext
    overlap_body = [-10, -10, -10, -10, -
                    10, -10, -10, -10, -10, -10, -10, -10]
    for i in range(0, 12):
        if len(topics_categories[i].intersection(this_body)) > 0:
            overlap_body[i] = this_body_sentiment

    # title_overlap_1 = len(t_1.intersection(this_title))
    # title_overlap_2 = len(t_2.intersection(this_title))
    # title_overlap_3 = len(t_3.intersection(this_title))
    # title_overlap_4 = len(t_4.intersection(this_title))
    # title_overlap_5 = len(t_5.intersection(this_title))
    # title_overlap_6 = len(t_6.intersection(this_title))
    # title_overlap_7 = len(t_7.intersection(this_title))
    # title_overlap_8 = len(t_8.intersection(this_title))
    # title_overlap_9 = len(t_9.intersection(this_title))
    # title_overlap_10 = len(t_10.intersection(this_title))
    # title_overlap_11 = len(t_11.intersection(this_title))

    s_json['body_topics'] = overlap_body
    g.write(str(s_json)+"\n")

    # overlap_1 = t_1.intersection(this_body)
    # overlap_2 = t_2.intersection(this_body)
    # overlap_3 = t_3.intersection(this_body)
    # overlap_4 = t_4.intersection(this_body)
    # overlap_5 = t_5.intersection(this_body)
    # overlap_6 = t_6.intersection(this_body)
    # overlap_7 = t_7.intersection(this_body)
    # overlap_8 = t_8.intersection(this_body)
    # overlap_9 = t_9.intersection(this_body)
    # overlap_10 = t_10.intersection(this_body)
    # overlap_11 = t_11.intersection(this_body)

    # if len(overlap_1) > 0:
    #     print(overlap_1)

f.close()
g.close()

# this_date_readable = dt.datetime.fromtimestamp(
#     int(s_json['created'])
# ).strftime('%m')

# # check if author exists in our dictionary. Increment for how many times that author has posted
# if this_author in author_posts:
#     authors[this_author] += 1
#     author_posts[this_author].append(id)
# else:
#     authors[this_author] = 1
#     author_posts[this_author] = [id]

# # check if the author has a flair for how much weight they have lost
# if(not(this_author_flair == "None" or this_author_flair == "New") and len(this_author_flair) > 0):
#     has_flair[this_author] = this_author_flair


# prints out the top 100 posters
# cntt = 0
# for w in sorted(authors, key=authors.get, reverse=True):
#     # try:
#     #     print(w, authors[w], has_flair[w])
#     # except:
#     #     print(w, authors[w], "NA")
#     g.write(w + "\n")
#     if authors[w] <= 2:
#         g.write("2**********************************************************")
#     elif authors[w] <= 5:
#         g.write("3*******************************************")
#     elif authors[w] <= 10:
#         g.write("10****************************")
#     elif authors[w] <= 25:
#         g.write("25**************")
#     elif authors[w] <= 50:
#         g.write("50*********")
#     elif authors[w] <= 100:
#         g.write("100***")
#     cntt += 1

# f.close()
# # g.close()
