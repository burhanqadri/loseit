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

author_comments = {}
# consistency_howlong = {}
# dict_month_howlong = {}

# exclude_vets = ["15-01", "15-02", "15-03", "15-04"]

with open('authors_comments.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if(line_count > 10):
            break
        if line_count < 2:
            print(row)
            line_count += 1
            continue
            # print(f'Column names are {", ".join(row)}')
        else:
            try:
                print("hello", row)
                author = row['author']
                if author in author_comments:
                    author_comments[author] += 1
                else:
                    author_comments[author] = 1
                # first_date = row['first-date']
                # month = int(float(row['first-date-month']))

            except:
                line_count += 1
                continue

        line_count += 1

    # print(dict_month_howlong)
    print(f'Processed {line_count} lines.')
