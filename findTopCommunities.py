import csv

g = open("topcomsMen.txt", "a")
seen = set()
cnt = 0
s = ""

# Men
top25Men = ["loseit", "progresspics", "Fitness", "keto", "food", "Fitness", "running", "1200isplenty", "intermittentfasting", "Cooking", "EatCheapAndHealthy",
            "MealPrepSunday", "FoodPorn", "food", "C25K", "xxfitness", "bodyweightfitness", "fasting", "1500isplenty", "ketorecipes", "nutrition", "Brogress", "CICO", "vegan", "1200isplenty", "drunk", "intermittentfasting"]
top25Women = ["loseit", "progresspics", "xxfitness", "1200isplenty", "EatCheapAndHealthy", "1200isplenty", "keto", "intermittentfasting", "food", "Cooking", "MealPrepSunday", "Fitness", "running",
              "1500isplenty", "C25K", "CICO", "xxketo", "fasting", "ketorecipes", "vegan", "nutrition", "FoodPorn", "vegetarian", "Fitness", "intermittentfasting", "bodyweightfitness", "food"]
with open('nodes_Edges.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        s_source = row['Source']
        s_target = row['Target']
        s_weight = row['weight']

        # if(s_source not in seen len(seen) > 25):
        #     break
        # if s_source not in top25Women or s_target not in top25Women:
        if s_source not in top25Men or s_target not in top25Men:
            continue
        # if cnt > 25:
        #     break

        g.write(str(s_source) + "," + str(s_target) +
                "," + str(s_weight) + "\n")
    print(s)

g.close()
