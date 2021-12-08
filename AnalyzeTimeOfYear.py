import csv

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

dict_howlong = {}
consistency_howlong = {}
dict_month_howlong = {}

consistency_ratio_sum = {}

exclude_vets = ["15-01", "15-02", "15-03", "15-04"]

with open('Merged4.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if(line_count > 10):
            break
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
        else:
            try:
                first_date = row['first-date']
                month = int(float(row['first-date-month']))
                duration = int(float(row['duration'])) + 1
                consistency = int(float(row['consistency-months-commented']))
                # print(first_date, month, duration, consistency)

                if first_date in exclude_vets:
                    continue

                if first_date in dict_howlong:
                    dict_howlong[first_date] += 1
                    consistency_ratio_sum[first_date] += consistency/duration
                    if duration > 1:
                        consistency_howlong[first_date] += 1
                    # consistency_howlong[first_date] += consistency
                else:
                    dict_howlong[first_date] = 1
                    consistency_ratio_sum[first_date] = consistency/duration
                    if duration > 1:
                        consistency_howlong[first_date] = 1

                # if month in dict_month_howlong:
                #     dict_month_howlong[month] += 1
                # else:
                #     dict_month_howlong[month] = 1

            except:
                continue

        line_count += 1

    for key in sorted(dict_howlong):
        print(key, dict_howlong[key],
              consistency_howlong[key]/dict_howlong[key], consistency_ratio_sum[key]/dict_howlong[key])
    # print(dict_month_howlong)
    print(f'Processed {line_count} lines.')
