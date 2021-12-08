import csv

exclude_vets = ["15-01", "15-02", "15-03", "15-04"]

with open('Merged4.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0

    haveGender = 0
    numMen = 0
    numWomen = 0
    haveFlair = 0
    excluded = 0

    for row in csv_reader:
        # if(line_count > 100000):
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

                if(len(this_gender) == 1):
                    if('F' in this_gender.upper()):
                        numWomen += 1
                    else:
                        numMen += 1
                    haveGender += 1

                elif len(row['gender']) == 1:
                    haveGender += 1
                    if('F' in row['gender'].upper()):
                        numWomen += 1
                    else:
                        numMen += 1
                if not(row['flair'] == 'None' or row['flair'] == 'New'):
                    haveFlair += 1
                    # print(len(this_gender), this_gender)

            except:
                continue

        line_count += 1

    print(haveGender, haveFlair, excluded, numMen, numWomen)

    print(f'Processed {line_count} lines.')
