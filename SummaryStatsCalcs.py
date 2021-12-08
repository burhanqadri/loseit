import csv
from os import remove
import statistics

removeDuplicates = set()

flairedList = []
f_flair = []
m_flair = []

f = open("all_flaired.txt", "r")
for line in f:
    flairedList.append(line.strip())

ff = open("f_authors.txt", "r")
for line in ff:
    f_flair.append(line.strip())

fff = open("m_authors.txt", "r")
for line in fff:
    m_flair.append(line.strip())

# exclude_vets = ["15-01", "15-02", "15-03", "15-04", "15-05",
#                 "15-06"]

mosyears = ["15-01", "15-02", "15-03", "15-04", "15-05",
            "15-06", "15-07", "15-08", "15-09", "15-10", "15-11", "15-12", "16-01", "16-02", "16-03", "16-04", "16-05", "16-06", "16-07", "16-08", "16-09", "16-10", "16-11", "16-12", "17-01", "17-02", "17-03", "17-04", "17-05", "17-06", "17-07", "17-08", "17-09", "17-10", "17-11", "17-12", "18-01", "18-02", "18-03", "18-04", "18-05", "18-06",
            "18-07", "18-08", "18-09", "18-10", "18-11", "18-12", "19-01", "19-02", "19-03", "19-04", "19-05", "19-06", "19-07", "19-08", "19-09", "19-10", "19-11", "19-12", "20-01", "20-02", "20-03", "20-04", "20-05", "20-06", "20-07", "20-08", "20-09", "20-10", "20-11", "20-12", "21-01", "21-02", "21-03", "21-04", "21-05", "21-06", "21-07", "21-08"]


activeAtDate = {}
keywordAtDate = {}
comm_len_AtDate = {}
comm_sent_AtDate = {}

genderDummy = {}
flairDummy = {}

fileData = open("Metrics_Data_LoseIt.txt", "a")


# with open('Merged4.csv', mode='r') as csv_file:
with open('authors_comments.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0

    for row in csv_reader:
        # if(line_count > 100):
        #     break
        if(line_count % 10000 == 0):
            print(line_count)
        if line_count < 2:
            line_count += 1
            continue
            # print(f'Column names are {", ".join(row)}')
        else:
            try:
                # print(row)
                auth = row['author']
                comm_len = len(row['comment-text'])
                comm_sent = float(row['sentiment'])
                comm_date = row['month-year'][2:]
                comm_keywords = row['topics']

                # comm_keywords_commaseparated = ""
                # for i in range(len(comm_keywords)):
                #     comm_keywords_commaseparated += comm_keywords[i] + ","
                # comm_keywords_commaseparated = comm_keywords_commaseparated[:-1]

                if (auth in ["AutoModerator", "[deleted]"]):
                    continue

                if(auth in flairedList):
                    flairDummy[auth] = 1

                if auth in m_flair:
                    genderDummy[auth] = 0
                elif auth in f_flair:
                    genderDummy[auth] = 1
                # print(auth, comm_date, comm_month, comm_year)

                if auth in keywordAtDate:
                    try:
                        for j in range(len(comm_keywords)):
                            keywordAtDate[auth][comm_date][j] += int(
                                comm_keywords[j])
                    except:
                        keywordAtDate[auth] = {}
                        keywordAtDate[auth][comm_date] = [0] * 165
                        for j in range(len(comm_keywords)):
                            index = int(comm_keywords[j])
                            keywordAtDate[auth][comm_date][j] += index
                else:
                    # print(emptylist)
                    keywordAtDate[auth] = {}
                    keywordAtDate[auth][comm_date] = [0] * 165
                    for jj in range(len(comm_keywords)):
                        keywordAtDate[auth][comm_date][jj] += int(
                            comm_keywords[jj])

                if auth in activeAtDate:
                    try:
                        activeAtDate[auth][comm_date] += 1
                        comm_len_AtDate[auth][comm_date] += comm_len
                        comm_sent_AtDate[auth][comm_date] += comm_sent

                    except:
                        activeAtDate[auth][comm_date] = 1
                        comm_len_AtDate[auth][comm_date] = comm_len
                        comm_sent_AtDate[auth][comm_date] = comm_sent

                else:
                    activeAtDate[auth] = {}
                    comm_len_AtDate[auth] = {}
                    comm_sent_AtDate[auth] = {}

                    activeAtDate[auth][comm_date] = 1
                    comm_len_AtDate[auth][comm_date] = comm_len
                    comm_sent_AtDate[auth][comm_date] = comm_sent

                # print(comm_date, activeAtDate[comm_date])

            except:
                continue

        line_count += 1

    # print(statistics.median(durationMen),
    #       statistics.median(durationWomen), statistics.median(durationFlairs), statistics.median(durationNonFlairs))
    # print(activeAtDate, comm_len_AtDate)
    # for key in mosyears:
    #     try:
    #         print(key, activeAtDate[key])
    #     except:
    #         print(key, 0)
    fileData.write("author,flair,gender,timeid,uniquestring,month,year,num_coms,avg_len,avg_sent,kw0_water,kw1_drink,kw2_drinking,kw3_soda,kw4_sugar,kw5_sweet,kw6_snack,kw7_coffee,kw8_craving,kw9_diet,kw10_beer,kw11_alcohol,kw12_eat,kw13_food,kw14_meal,kw15_eating,kw16_lunch,kw17_dinner,kw18_hungry,kw19_calorie,kw20_breakfast,kw21_food,kw22_diet,kw23_eating,kw24_protein,kw25_carbs,kw26_veggie,kw27_recipe,kw28_cook,kw29_doctor,kw30_health,kw31_pain,kw32_energy,kw33_surgery,kw34_friend,kw35_family,kw36_kid,kw37_mom,kw38_school,kw39_husband,kw40_girlfriend,kw41_calorie,kw42_deficit,kw43_exercise,kw44_tdee,kw45_cico,kw46_counting,kw47_count,kw48_mfp,kw49_cal,kw50_run,kw51_running,kw52_walk,kw53_walking,kw54_mile,kw55_gym,kw56_exercise,kw57_muscle,kw58_workout,kw59_cardio,kw60_lb,kw61_lost,kw62_pound,kw63_kggained,kw64_weight,kw65_starting,kw66_weight,kw67_lose,kw68_loss,kw69_fat,kw70_gain,kw71_bmi,kw72_height,kw73_range,kw74_scale,kw75_number,kw76_plateau,kw77_drop,kw78_weighing,kw79_hard,kw80_won,kw81_easy,kw82_worry,kw83_goal,kw84_hit,kw85_progress,kw86_end,kw87_picture,kw88_feel,kw89_close,kw90_happy,kw91_set,kw92_challenge,kw93_feel,kw94_feeling,kw95_eating,kw96_binge,kw97_bad,kw98_stop,kw99_time,kw100_control,kw101_hard,kw102_stress,kw103_struggle,kw104_pretty,kw105_luck,kw106_understand,kw107_talk,kw108_mental,kw109_care,kw110_check,kw111_great,kw112_love,kw113_awesome,kw114_job,kw115_amazing,kw116_congrats,kw117_hope,kw118_glad,kw119_day,kw120_week,kw121_track,kw122_maintenance,kw123_plan,kw124_log,kw125_logging,kw126_time,kw127_start,kw128_habit,kw129_choice,kw130_healthy,kw131_time,kw132_thought,kw133_felt,kw134_wanted,kw135_started,kw136_back,kw137_needed,kw138_decided,kw139_found,kw140_fit,kw141_size,kw142_clothes,kw143_big,kw144_wear,kw145_buy,kw146_pant,kw147_bought,kw148_shirt,kw149_dress,kw150_store,kw151_today,kw152_morning,kw153_night,kw154_yesterday,kw155_work,kw156_tomorrow,kw157_weekend,kw158_day,kw159_quarantine,kw160_lockdown,kw161_covid,kw162_coronavirus,kw163_home,kw164_inside\n")
    for auth in activeAtDate:
        # try:
        #     print(keywordAtDate[auth])
        # except:
        #     print("can't do it")
        for entry in activeAtDate[auth]:
            x_numcoms = activeAtDate[auth][entry]
            x_avg_len = comm_len_AtDate[auth][entry] / \
                activeAtDate[auth][entry]
            x_avg_sent = comm_sent_AtDate[auth][entry] / \
                activeAtDate[auth][entry]
            x_flair = 0
            x_gender = -1
            try:
                x_keywords = str(keywordAtDate[auth][entry])[1:-1]
            except:
                x_keywords = str([0] * 165)[1:-1]

            comm_month = entry[-2:]
            comm_year = "20" + entry[:2]
            timeid = mosyears.index(entry)
            uniquestring = str(auth) + str(timeid)

            try:
                x_flair = flairDummy[auth]
            except:
                potato = ""

            try:
                x_gender = genderDummy[auth]
            except:
                potato = ""

            this_line = auth + "," + str(x_flair) + "," + str(x_gender) + "," + str(timeid) + "," + uniquestring + "," + comm_month + \
                "," + comm_year + "," + \
                str(x_numcoms) + "," + str(x_avg_len) + \
                "," + str(x_avg_sent) + "," + x_keywords

            fileData.write(this_line + "\n")
    # for key in sorted(start_dates):
    #     print(key, start_dates[key])
    print(f'Processed {line_count} lines.')
