import csv
from os import remove
import statistics

removeDuplicates = set()

flairedList = []
f_flair = []
m_flair = []

f = open("all_flaired.txt", "r")
for line in f:
    flairedList.append(line.strip())

ff = open("f_authors.txt", "r")
for line in ff:
    f_flair.append(line.strip())

fff = open("m_authors.txt", "r")
for line in fff:
    m_flair.append(line.strip())


x_men = []
x_women = []
x_flairs = []
x_others = []


s_men = []
s_women = []
s_flairs = []
s_others = []

# with open('Merged4.csv', mode='r') as csv_file:
with open('authors_comments.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0

    for row in csv_reader:
        # if(line_count > 1000):
        #     break
        if(line_count % 10000 == 0):
            print(line_count)
        if line_count < 2:
            line_count += 1
            continue
            # print(f'Column names are {", ".join(row)}')
        else:
            try:
                # print(row)
                auth = row['author']
                comm_len = len(row['comment-text'])
                comm_sent = float(row['sentiment'])
                # comm_date = row['month-year'][2:]
                # comm_keywords = row['topics']

                if (auth in ["AutoModerator", "[deleted]"]):
                    continue

                if(auth in flairedList):
                    x_flairs.append(comm_len)
                    s_flairs.append(comm_sent)
                else:
                    x_others.append(comm_len)
                    s_others.append(comm_sent)

                if auth in m_flair:
                    x_men.append(comm_len)
                    s_men.append(comm_sent)
                elif auth in f_flair:
                    x_women.append(comm_len)
                    s_women.append(comm_sent)
                # print(auth, comm_date, comm_month, comm_year)

            except:
                continue

        line_count += 1

    print(statistics.median(x_men),
          statistics.median(x_women), statistics.median(x_flairs), statistics.median(x_others))

    print(statistics.mean(x_men),
          statistics.mean(x_women), statistics.mean(x_flairs), statistics.mean(x_others))

    print(statistics.median(s_men),
          statistics.median(s_women), statistics.median(s_flairs), statistics.median(s_others))

    print(statistics.mean(s_men),
          statistics.mean(s_women), statistics.mean(s_flairs), statistics.mean(s_others))
    print(f'Processed {line_count} lines.')
