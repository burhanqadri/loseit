import csv
import statistics

# exclude_vets = ["15-01", "15-02", "15-03", "15-04", "15-05",
#                 "15-06", "15-07", "15-08", "15-09", "15-10", "15-11", "15-12"]

exclude_vets = ["15-01", "15-02", "15-03", "15-04", "15-05",
                "15-06"]

mosyears = ["15-07", "15-08", "15-09", "15-10", "15-11", "15-12", "16-01", "16-02", "16-03", "16-04", "16-05", "16-06", "16-07", "16-08", "16-09", "16-10", "16-11", "16-12", "17-01", "17-02", "17-03", "17-04", "17-05", "17-06", "17-07", "17-08", "17-09", "17-10", "17-11", "17-12", "18-01", "18-02", "18-03", "18-04", "18-05", "18-06",
            "18-07", "18-08", "18-09", "18-10", "18-11", "18-12", "19-01", "19-02", "19-03", "19-04", "19-05", "19-06", "19-07", "19-08", "19-09", "19-10", "19-11", "19-12", "20-01", "20-02", "20-03", "20-04", "20-05", "20-06", "20-07", "20-08", "20-09", "20-10", "20-11", "20-12", "21-01", "21-02", "21-03", "21-04", "21-05", "21-06", "21-07", "21-08"]


activeAtDate = {}

# with open('Merged4.csv', mode='r') as csv_file:
with open('authors_comments.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0

    haveGender = 0
    haveFlair = 0
    excluded = 0

    for row in csv_reader:
        # if(line_count > 200000):
        #     break
        if(line_count % 300000 == 0):
            print(line_count)
        if line_count < 2:
            line_count += 1
            continue
            # print(f'Column names are {", ".join(row)}')
        else:
            try:
                auth = row['author']
                comm_date = row['month-year'][2:]

                # commentingAtDate =
                try:
                    activeAtDate[comm_date].add(auth)
                except:
                    activeAtDate[comm_date] = {auth}
                # print(row)
                # print(auth)
                # first_date = row['first-date']
                # month = int(float(row['first-date-month']))
                # this_gender = row['loseItGender']

                # if first_date in exclude_vets:
                #     excluded += 1
                #     # line_count += 1
                #     continue

                # if first_date in start_dates:
                #     start_dates[first_date] += 1
                # else:
                #     start_dates[first_date] = 1

                # if(len(this_gender) == 1 or len(row['gender']) == 1):
                #     haveGender += 1
                #     if('M' in this_gender.upper()):
                #         if first_date in start_dates:
                #             start_dates[first_date] += 1
                #         else:
                #             start_dates[first_date] = 1
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

    for key in mosyears:
        try:
            print(key, len(activeAtDate[key]))
        except:
            print(0)

    # for key in sorted(start_dates):
    #     print(key, start_dates[key])
    print(f'Processed {line_count} lines.')
