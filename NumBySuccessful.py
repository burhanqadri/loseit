import csv

author_comments = {}

author_numComms = {}
k = open("numCommentsByAuthor.txt", "r")

for line in k:
    line = line.strip()
    components = line.split(",")
    author_numComms[components[0]] = components[1]

k.close()

with open('Merged2_csv.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if(line_count > 100):
            break
        try:
            this_author = row['author']
            this_flair = row['flair'].upper()

            print(this_author, author_numComms[this_author])
            # print(this_gender, this_flair)
        except:
            line_count += 1
            continue

        line_count += 1

    print(f'Processed {line_count} lines.')
