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
    # durationNonFlairs = {}

    # g = open("author_timetillflairchange_excl2015.txt", "a")
    g = open("full_authors_gendered.txt", "a")
    # h = open("authors_gendered.txt", "a")

    for row in csv_reader:
        # if(line_count > 1000):
        #     break
        if(line_count % 300000 == 0):
            print(line_count)
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
        else:
            try:
                auth = row['author']
                first_date = row['first-date']
                flairChangeDate = row['flair-change-date'][2:-3]
                month = int(float(row['first-date-month']))
                duration = int(float(row['duration'])) + 1
                consistency = int(float(row['consistency-months-commented']))
                this_gender = row['loseItGender']

                if len(flairChangeDate) < 1:
                    # print("NO FLAIR")
                    continue

                # if first_date in exclude_vets:
                #     excluded += 1
                #     # line_count += 1
                #     continue

                helper_firstYear = int(first_date[:2])
                helper_firstMonth = int(first_date[-2:])
                helper_changeYear = int(flairChangeDate[:2])
                helper_changeMonth = int(flairChangeDate[-2:])

                months_till_flair_change = 1000

                if(helper_changeYear == helper_firstYear):
                    months_till_flair_change = helper_changeMonth - helper_firstMonth
                else:
                    months_till_flair_change = (
                        helper_changeYear - helper_firstYear)*12 + (helper_changeMonth - helper_firstMonth)

                # if first_date == flairChangeDate:
                # print(this_gender, first_date, flairChangeDate,
                #       months_till_flair_change, duration)

                if(len(this_gender) == 1 or len(row['gender']) == 1):
                    haveGender += 1
                    if(months_till_flair_change != 1000):
                        # g.write(auth + "," + this_gender + "," +
                        #         str(months_till_flair_change) + "\n")

                        g.write(auth + "\n")
                    # if('F' in this_gender.upper()):

                    # else:

                # if not(row['flair'] == 'None' or row['flair'] == 'New'):

                # else:

                #     try:
                #         durationNonFlairs[months_till_flair_change].append(
                #             duration)
                #     except:
                #         durationNonFlairs[months_till_flair_change] = [
                #             duration]

            except:
                continue

        line_count += 1

    # print(statistics.median(durationMen),
    #       statistics.median(durationWomen), statistics.median(durationFlairs), statistics.median(durationNonFlairs))

    print(f'Processed {line_count} lines.')
