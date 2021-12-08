import csv

author_comments = {}
# consistency_howlong = {}

# exclude_vets = ["15-01", "15-02", "15-03", "15-04"]

# with open('all_communities.csv', mode='r') as csv_file:
with open('all_communities_includingamount.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if(line_count > 10):
            break
        if line_count < 1:
            print(row)
            line_count += 1
            continue
        else:
            try:
                listOf_Comms = row['fullList'].split("|")
                countGreaterThan5 = 0
                for comm in listOf_Comms:
                    splitString = comm.split(":")
                    # print(splitString)
                    if int(splitString[1]) >= 5:
                        countGreaterThan5 += 1
                    # splitString[0]

                print(row['username'], row['numFood'], row['numDiet'],
                      row['numFitness'], row['numPics'], len(listOf_Comms), countGreaterThan5)
                # author = row['author']
                # if author in author_comments:
                #     author_comments[author] += 1
                # else:
                #     author_comments[author] = 1

            except:
                line_count += 1
                continue

        line_count += 1

    # print(dict_month_howlong)
    print(f'Processed {line_count} lines.')
