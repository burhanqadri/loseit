import csv
import ast
# 2 author
# 3 flair
# 4 flair-change-date
# 5 gender
# 6 age
# 7 last-date
# 8 first-date
# 9 first-date-month
# 10 duration
# 11 consistency-months-commented

# topics_categories_grouped = [{'water', 'drink', 'drinking', 'soda', 'sugar', 'sweet', 'snack', 'coffee', 'craving',
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

# //0-28
# //29-33
# //34-39
# //40-48
# //49-58
# //59-77
# //78-102
# //103-117
# //118-138
# //139-149
# //150-157
# //158-163
topics_categories = ['water', 'drink', 'drinking', 'soda', 'sugar', 'sweet', 'snack', 'coffee', 'craving',
                     'diet', 'beer', 'alcohol', 'eat', 'food', 'meal', 'eating', 'lunch', 'dinner', 'hungry', 'calorie', 'breakfast', 'food', 'diet', 'eating', 'protein', 'carbs', 'veggie', 'recipe', 'cook', 'doctor', 'health',
                     'pain', 'energy', 'surgery', 'friend', 'family', 'kid', 'mom',
                     'school', 'husband', 'girlfriend', 'calorie', 'deficit', 'exercise', 'tdee', 'cico',
                     'counting', 'count', 'mfp', 'cal', 'run', 'running', 'walk',
                     'walking', 'mile', 'gym', 'exercise', 'muscle', 'workout', 'cardio', 'lb', 'lost', 'pound', 'kg'
                     'gained', 'weight', 'starting', 'weight', 'lose', 'loss', 'fat', 'gain', 'bmi', 'height', 'range', 'scale', 'number', 'plateau', 'drop', 'weighing', 'hard', 'won', 'easy', 'worry', 'goal', 'hit', 'progress', 'end', 'picture', 'feel', 'close', 'happy', 'set', 'challenge', 'feel', 'feeling', 'eating', 'binge', 'bad', 'stop', 'time', 'control', 'hard', 'stress', 'struggle', 'pretty', 'luck', 'understand', 'talk', 'mental',
                     'care', 'check', 'great', 'love', 'awesome', 'job', 'amazing', 'congrats', 'hope', 'glad', 'day', 'week', 'track', 'maintenance',
                     'plan', 'log', 'logging', 'time', 'start', 'habit', 'choice', 'healthy', 'time', 'thought', 'felt', 'wanted', 'started', 'back', 'needed', 'decided', 'found', 'fit', 'size', 'clothes', 'big', 'wear', 'buy',
                     'pant', 'bought', 'shirt', 'dress', 'store', 'today', 'morning', 'night', 'yesterday',
                     'work', 'tomorrow', 'weekend', 'day', 'quarantine', 'lockdown', 'covid', 'coronavirus', 'home', 'inside']

topic_seen = {}
topic_by_month = {}
topic_by_monthYear = {}

sentiment_seen = {}
sentiment_by_month = {}
sentiment_by_monthYear = {}

# exclude_vets = ["15-01", "15-02", "15-03", "15-04"]


with open('authors_comments.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        # if(line_count > 1000):
        #     break
        if(line_count % 100000 == 0):
            print(line_count)
        if line_count < 2:
            line_count += 1
            continue
        else:
            try:
                # print("hello", row)
                topics = row['topics']
                sentiment = float(row['sentiment'])
                month = row['month']
                monthYear = row['month-year']

                topicCat = 0

                for index in range(0, 165):
                    if index < 29:
                        topicCat = 0
                    elif index < 33:
                        topicCat = 1
                    elif index < 39:
                        topicCat = 2
                    elif index < 48:
                        topicCat = 3
                    elif index < 58:
                        topicCat = 4
                    elif index < 77:
                        topicCat = 5
                    elif index < 102:
                        topicCat = 6
                    elif index < 117:
                        topicCat = 7
                    elif index < 138:
                        topicCat = 8
                    elif index < 149:
                        topicCat = 9
                    elif index < 157:
                        topicCat = 10
                    else:
                        topicCat = 11
                    if topics[index] == '1':
                        try:
                            topic_seen[topicCat] += 1
                            sentiment_seen[topicCat] += sentiment
                        except:
                            topic_seen[topicCat] = 1
                            topic_by_month[topicCat] = {}
                            topic_by_monthYear[topicCat] = {}

                            sentiment_seen[topicCat] = sentiment
                            sentiment_by_month[topicCat] = {}
                            sentiment_by_monthYear[topicCat] = {}

                        if month in topic_by_month[topicCat]:
                            topic_by_month[topicCat][month] += 1
                            sentiment_by_month[topicCat][month] += sentiment
                        else:
                            topic_by_month[topicCat][month] = 1
                            sentiment_by_month[topicCat][month] = sentiment

                        if monthYear in topic_by_monthYear[topicCat]:
                            topic_by_monthYear[topicCat][monthYear] += 1
                            sentiment_by_monthYear[topicCat][monthYear] += sentiment
                        else:
                            topic_by_monthYear[topicCat][monthYear] = 1
                            sentiment_by_monthYear[topicCat][monthYear] = sentiment

                # if author in author_comments:
                #     author_comments[author] += 1
                # else:
                #     author_comments[author] = 1
                # first_date = row['first-date']
                # month = int(float(row['first-date-month']))

            except:
                line_count += 1
                continue

        line_count += 1

    # for key in sorted(topic_seen.items(), key=lambda x: x[1], reverse=True):
    #     # print(key[0])
    #     this_key = key[0]
    #     avg_sentiment = sentiment_seen[this_key] / topic_seen[this_key]
    #     print(this_key, topics_categories[this_key],
    #           topic_seen[this_key], avg_sentiment)
    mos = ["01", "02", "03", "04", "05", "06",
           "07", "08", "09", "10", "11", "12"]

    mosyears = ["2015-01", "2015-02", "2015-03", "2015-04", "2015-05", "2015-06", "2015-07", "2015-08", "2015-09", "2015-10", "2015-11", "2015-12", "2016-01", "2016-02", "2016-03", "2016-04", "2016-05", "2016-06", "2016-07", "2016-08", "2016-09", "2016-10", "2016-11", "2016-12", "2017-01", "2017-02", "2017-03", "2017-04", "2017-05", "2017-06", "2017-07", "2017-08", "2017-09", "2017-10", "2017-11", "2017-12", "2018-01", "2018-02", "2018-03", "2018-04", "2018-05", "2018-06",
                "2018-07", "2018-08", "2018-09", "2018-10", "2018-11", "2018-12", "2019-01", "2019-02", "2019-03", "2019-04", "2019-05", "2019-06", "2019-07", "2019-08", "2019-09", "2019-10", "2019-11", "2019-12", "2020-01", "2020-02", "2020-03", "2020-04", "2020-05", "2020-06", "2020-07", "2020-08", "2020-09", "2020-10", "2020-11", "2020-12", "2021-01", "2021-02", "2021-03", "2021-04", "2021-05", "2021-06", "2021-07", "2021-08", "2021-09", "2021-10", "2021-11", "2021-12"]

    fileOps = open("cat_topics_month", "a")
    fileOpsSent = open("cat_topics_month_sent", "a")

    for i in range(12):
        str_mos = str(i) + "," + topics_categories[i] + ","
        str_mos_sent = str_mos
        try:
            for looper in range(len(mos)):
                mo = mos[looper]
                try:
                    avg_sent = sentiment_by_month[i][mo] / \
                        topic_by_month[i][mo]
                    str_mos += str(topic_by_month[i][mo]) + ","
                    str_mos_sent += str(avg_sent) + ","
                    # print(
                    #     mo, ",", i, ",", topics_categories[i], topic_by_month[i][mo], ",", avg_sent)
                except:
                    str_mos += "0,"
                    str_mos_sent += "0,"
                    continue

            fileOps.write(str_mos[:-1] + "\n")
            fileOpsSent.write(str_mos_sent[:-1] + "\n")
        except:
            print("skip")
    fileOps.close()
    fileOpsSent.close()

    yearOps = open("cat_topics_monthYear", "a")
    yearOpsSent = open("cat_topics_monthYear_sent", "a")

    for i in range(12):
        str_mosyears = str(i) + "," + topics_categories[i] + ","
        str_mosyears_sent = str_mosyears
        try:
            for looper in range(len(mosyears)):
                # print(i, looper)
                mo = mosyears[looper]
                try:
                    avg_sent = sentiment_by_monthYear[i][mo] / \
                        topic_by_monthYear[i][mo]
                    str_mosyears += str(topic_by_monthYear[i][mo]) + ","
                    str_mosyears_sent += str(avg_sent) + ","
                    # print(
                    #     mo, ",", i, ",", topics_categories[i], topic_by_monthYear[i][mo], ",", avg_sent)
                except:
                    str_mosyears += "0,"
                    str_mosyears_sent += "0,"
                    # print(mo, ",", i, ",", topics_categories[i])
                    continue

            yearOps.write(str_mosyears[:-1] + "\n")
            yearOpsSent.write(str_mosyears_sent[:-1] + "\n")
        except:
            print("skip")
    yearOps.close()
    yearOpsSent.close()

    print(f'Processed {line_count} lines.')
