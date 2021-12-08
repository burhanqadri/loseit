import csv
import statistics

# exclude_vets = ["15-01", "15-02", "15-03", "15-04", "15-05",
#                 "15-06", "15-07", "15-08", "15-09", "15-10", "15-11", "15-12"]

exclude_vets = ["15-01", "15-02", "15-03", "15-04", "15-05",
                "15-06"]

with open('Merged4.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0

    haveGender = 0
    haveFlair = 0
    excluded = 0

    Women_timeTillFlairChange = []
    Men_timeTillFlairChange = []
    Overall_timeTillFlairChange = []

    durationWomen = {}
    durationMen = {}
    durationFlairs = {}

    flairContent = {}
    counter = 0
    # durationNonFlairs = {}

    # g = open("author_timetillflairchange_excl2015.txt", "a")
    gF = open("f_authors.txt", "a")
    gM = open("m_authors.txt", "a")
    # h = open("authors_gendered.txt", "a")

    for row in csv_reader:
        # if(line_count > 10000):
        #     break
        if(line_count % 300000 == 0):
            print(line_count)
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
        else:
            try:
                auth = row['author']
                first_date = row['first-date']

                flairText = row['flair']

                flairChangeDate = row['flair-change-date'][2:-3]
                # month = int(float(row['first-date-month']))
                # duration = int(float(row['duration'])) + 1
                # consistency = int(float(row['consistency-months-commented']))
                # this_gender = row['loseItGender']

                if len(flairChangeDate) < 1:
                    # print("NO FLAIR")
                    continue

                # if first_date in exclude_vets:
                #     excluded += 1
                #     # line_count += 1
                #     continue
                if len(flairText) < 2:
                    counter = counter
                    # print(flairText, len(flairText), first_date)
                else:
                    counter += 1
                if flairText not in ["None", "New"] and flairText in flairContent:
                    flairContent[flairText] += 1
                else:
                    flairContent[flairText] = 1

            except:
                continue

        line_count += 1

    # print(statistics.median(durationMen),
    #       statistics.median(durationWomen), statistics.median(durationFlairs), statistics.median(durationNonFlairs))
    cntt = 0

# print(all_count)
for w in sorted(flairContent, key=flairContent.get, reverse=True):
    try:
        print(w, ": ", flairContent[w])
    except:
        print("Error")
    if cntt > 50:
        break
    cntt += 1
print(counter)
print(f'Processed {line_count} lines.')
