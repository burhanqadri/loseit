import csv
import statistics

exclude_vets = ["15-01", "15-02", "15-03", "15-04"]

with open('Merged4.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0

    haveGender = 0
    haveFlair = 0

    commsMen = []
    commsWomen = []
    commsFlairs = []
    commsNonFlairs = []

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

                # if first_date in exclude_vets:
                #     excluded += 1
                #     line_count += 1
                #     continue

                authComms = float(row['numLoseItComments'])

                if(len(this_gender) == 1):
                    if('F' in this_gender.upper()):
                        commsWomen.append(authComms)
                    else:
                        commsMen.append(authComms)

                elif len(row['gender']) == 1:
                    if('F' in row['gender'].upper()):
                        commsWomen.append(authComms)
                    else:
                        commsMen.append(authComms)

                if not(row['flair'] == 'None' or row['flair'] == 'New'):
                    haveFlair += 1
                    commsFlairs.append(authComms)
                else:
                    commsNonFlairs.append(authComms)
                    # print(len(this_gender), this_gender)

            except:
                continue

        line_count += 1

    print(statistics.median(commsMen),
          statistics.median(commsWomen), statistics.median(commsFlairs), statistics.median(commsNonFlairs))

    print(statistics.mean(commsMen),
          statistics.mean(commsWomen), statistics.mean(commsFlairs), statistics.mean(commsNonFlairs))

    print(f'Processed {line_count} lines.')
