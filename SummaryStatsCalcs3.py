import csv
import statistics

exclude_vets = ["15-01", "15-02", "15-03", "15-04"]

with open('Merged4.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0

    haveGender = 0
    haveFlair = 0
    excluded = 0

    durationWomen = []
    consistencyWomen = []

    durationMen = []
    consistencyMen = []

    durationFlairs = []
    consistencyFlairs = []

    durationNonFlairs = []
    consistencyNonFlairs = []

    for row in csv_reader:
        # if(line_count > 100):
        #     break
        if(line_count % 300000 == 0):
            print(line_count)
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
        else:
            try:
                first_date = row['first-date']
                month = int(float(row['first-date-month']))
                duration = int(float(row['duration'])) + 1
                consistency = int(float(row['consistency-months-commented']))
                this_gender = row['loseItGender']

                # print(first_date, month, duration, consistency)

                if first_date in exclude_vets:
                    excluded += 1
                    line_count += 1
                    continue

                if(len(this_gender) == 1):
                    haveGender += 1
                    if('F' in this_gender.upper()):
                        durationWomen.append(duration)
                        consistencyWomen.append(consistency/duration)
                    else:
                        durationMen.append(duration)
                        consistencyMen.append(consistency/duration)

                elif len(row['gender']) == 1:
                    haveGender += 1
                    if('F' in row['gender'].upper()):
                        durationWomen.append(duration)
                        consistencyWomen.append(consistency/duration)
                    else:
                        durationMen.append(duration)
                        consistencyMen.append(consistency/duration)

                if not(row['flair'] == 'None' or row['flair'] == 'New'):
                    haveFlair += 1
                    durationFlairs.append(duration)
                    consistencyFlairs.append(consistency/duration)
                else:
                    durationNonFlairs.append(duration)
                    consistencyNonFlairs.append(consistency/duration)

            except:
                continue

        line_count += 1

    print(statistics.median(durationMen),
          statistics.median(durationWomen), statistics.median(durationFlairs), statistics.median(durationNonFlairs))

    print(statistics.mean(durationMen),
          statistics.mean(durationWomen), statistics.mean(durationFlairs), statistics.mean(durationNonFlairs))

    print(statistics.median(consistencyMen),
          statistics.median(consistencyWomen), statistics.median(consistencyFlairs), statistics.median(consistencyNonFlairs))

    print(statistics.mean(consistencyMen),
          statistics.mean(consistencyWomen), statistics.mean(consistencyFlairs), statistics.mean(consistencyNonFlairs))

    print(f'Processed {line_count} lines.')
