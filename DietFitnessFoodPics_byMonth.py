import ast
import timeit
import datetime as dt
from textblob import TextBlob

listOf_Food = {'askculinary',
               'CollegeCooking',
               'cookbooks',
               'cooking',
               'cookingforbeginners',
               'cookingwithcondiments',
               'cookiedecorating',
               'cookwithbeer',
               'ketorecipes',
               'KitchenConfidential',
               'MimicRecipes',
               'onceamonthcooking',
               'pressurecooking',
               'recipes',
               'slowcooking',
               'smoking',
               'sousvide',
               'AskFoodHistorians',
               'AskFastFoodEmployees',
               'breakfast',
               'culinaryporn',
               'dessert',
               'dessertporn',
               'DixieFood',
               'fffffffuuuuuuuuuuuud',
               'foodie',
               'FoodNews',
               'foodporn',
               'foodvideos',
               'foodtheory',
               'FoodWriting',
               'glutenfree',
               'HealthProject',
               'healthyfood',
               'ifilikefood',
               'ironchef',
               'KnightsOfPineapple',
               'food2',
               'mexicanfood',
               'organic',
               'spicy',
               'todaysbreakfast',
               'tonightsdinner',
               'todayIate',
               'WorldofPancakes',
               'WhatYouEat',
               'budgetfood',
               'Cheap_Meals',
               'EatCheapAndHealthy',
               'Food_Bank',
               'fastfood',
               'fastfoodreview',
               'BurgerKing',
               'bys',
               'CarlsJr',
               'ChickFilA',
               'Chipotle',
               'Dominos',
               'DunkinDonuts',
               'fiveguys',
               'Hooters',
               'innout',
               'KFC',
               'McDonalds',
               'OliveGarden',
               'Panera',
               'PapaJohns',
               'PizzaHut',
               'qdoba',
               'Starbucks',
               'Subway',
               'tacobell',
               'TimHortons',
               'WaffleHouse',
               'Wendys',
               'Whataburger',
               'appetizers',
               'asianeats',
               'BBQ',
               'bento',
               'BreakfastFood',
               'burgers',
               'BurgersGoneWild',
               'cakewin',
               'Canning',
               'cereal',
               'charcuterie',
               'Cheese',
               'chinesefood',
               'condiments',
               'crepes',
               'curry',
               'eatsandwiches',
               'eatwraps',
               'fishtew',
               'fried',
               'grease',
               'grilledcheese',
               'honey',
               'icecreamery',
               'indianfood',
               'irishfood',
               'JapaneseFood',
               'jello',
               'KoreanFood',
               'meat',
               'melts',
               'pasta',
               'PeanutButter',
               'pizza',
               'plus_size_tarts',
               'ramen',
               'seafood',
               'steak',
               'sushi',
               'SushiRoll',
               'veg',
               'veganfood',
               'Vitamix',
               'energydrinks',
               'juice',
               'milk',
               'water',
               'beer',
               'showerbeer',
               'ShowerBeerGoneWild',
               'drunk',
               'firewater',
               'homebrewing',
               'liquor',
               'rum',
               'cider',
               'wine',
               'vodka',
               'scotch',
               'bourbon',
               'gin',
               'tequila'}
listOf_Diet = {'4hourbodyslowcarb',
               'caloriecount',
               'diabeats',
               'EatCheapAndHealthy',
               'fasting',
               'fitmeals',
               'fixmydiet',
               'food',
               'food2',
               'frugalsupplements',
               'gainitmeals',
               'intermittentfasting',
               'juicing',
               'keto',
               'ketogains',
               'leangains',
               'lowcarb',
               'mealprepsunday',
               'Nootropics',
               'nutrition',
               'nutritionscience',
               'paleo',
               'runmeals',
               'smoothies',
               'soylent',
               'StackAdvice',
               'supplements',
               'supplementation',
               'swolefood',
               'theketodiet',
               'vegan',
               'vegetarian',
               'vegrecipes',
               'xxketo',
               'cico',
               'Myfitnesspal',
               'keto',
               'eatcheapandhealthy',
               'mealprepsunday',
               'intermittentfasting',
               'Volumeeating',
               '1200isplenty',
               '1200isplentyketo',
               'vegan1200isplenty',
               '1500isplenty'}
listOf_Fitness = {'fitness',
                  'xxfitness',
                  'bodyweightfitness',
                  'c25k',
                  'running',
                  'hiit',
                  '90daysgoal',
                  'athleanx',
                  'b210k',
                  'bodybeast',
                  'bodybuilding',
                  'bodyweightfitness',
                  'briskwalking',
                  'BTFC',
                  'BulkOrCut',
                  'crossfit',
                  'c25k',
                  'cutit',
                  'cuttingweight',
                  'eood',
                  'firstmarathon',
                  'fitnessonline',
                  'flexibility',
                  'gettingshredded',
                  'GripTraining',
                  'gsprushfit',
                  'homefitness',
                  'homegym',
                  'Insanity',
                  'insanityworkout',
                  'kettlebell',
                  'kettlebellsport',
                  'LiftingRoutines',
                  'naturalbodybuilding',
                  'necromancers',
                  'p90x',
                  'posture',
                  'soccerfitness',
                  'steroids',
                  'strength_training',
                  'stronglifts5x5',
                  'TacticalAthlete',
                  'tapoutxt',
                  'walking',
                  'weightroom',
                  'WorldStreetWorkout',
                  'zumba',
                  'AdvancedFitness',
                  'fitness30plus',
                  'fitnessplus',
                  'fitpregnancy',
                  'GBFit',
                  'ownit',
                  'RunnersInChicago',
                  'runnyc',
                  'veganfitness',
                  'xxfitness',
                  'aikido',
                  'amateur_boxing',
                  'amateurfights',
                  'American_Kenpo',
                  'bajiquan',
                  'balintawak',
                  'bjj',
                  'Boxing',
                  'Bujinkan',
                  'Bushi',
                  'capoeira',
                  'combatarts',
                  'Eskrima',
                  'Fencing',
                  'hapkido',
                  'HwaRangDo',
                  'iaido',
                  'internal_arts',
                  'jkd',
                  'Ju_Jutsu',
                  'judo',
                  'karate',
                  'kendo',
                  'Kickboxing',
                  'kravmaga',
                  'kungfu',
                  'kungfucinema',
                  'kungfuonyoutube',
                  'kyokushin',
                  'martialarts',
                  'MMA',
                  'mmafights',
                  'MuayThai',
                  'sambo',
                  'Sanda',
                  'Savate',
                  'ShorinjiKempo',
                  'silat',
                  'systema',
                  'taekwondo',
                  'taijiquan',
                  'tangsoodo',
                  'TraditionalNinjutsu',
                  'TrueQiGong',
                  'ufc',
                  'WingChun',
                  'wma'}
listOf_Pics = {'bodygallery',
               'brogress',
               'GuessMyBF',
               'nakedprogress',
               'progresspics',
               'runwild'}


mosyears = ["15-01", "15-02", "15-03", "15-04", "15-05",
            "15-06", "15-07", "15-08", "15-09", "15-10", "15-11", "15-12", "16-01", "16-02", "16-03", "16-04", "16-05", "16-06", "16-07", "16-08", "16-09", "16-10", "16-11", "16-12", "17-01", "17-02", "17-03", "17-04", "17-05", "17-06", "17-07", "17-08", "17-09", "17-10", "17-11", "17-12", "18-01", "18-02", "18-03", "18-04", "18-05", "18-06",
            "18-07", "18-08", "18-09", "18-10", "18-11", "18-12", "19-01", "19-02", "19-03", "19-04", "19-05", "19-06", "19-07", "19-08", "19-09", "19-10", "19-11", "19-12", "20-01", "20-02", "20-03", "20-04", "20-05", "20-06", "20-07", "20-08", "20-09", "20-10", "20-11", "20-12", "21-01", "21-02", "21-03", "21-04", "21-05", "21-06", "21-07", "21-08"]


# g = open("authors_loseit_posts.txt", "a")
g = open("DietFitnessFoodPics_byMonth.txt", "a")
g.write('username,date,username_date_combined, numFood,numDiet,numFitness,numPics\n')

# C:/Users/burha/Desktop/Weight Loss/
f = open("C:/Users/burha/Desktop/Weight Loss/authors_loseit_comments.txt", "r")
# f = open("C:/Users/burha/Desktop/Weight Loss/authors_loseit_comments.txt", "r")
# f = open("C:/Users/burha/Desktop/Weight Loss/authors_progresspics_posts.txt", "r")

fileData = open("Metrics_Data_Communities.txt", "a")


cnt = 0
s = ""

authors = {}

numCommsInEachType = {}
numFood = {}
numDiet = {}
numFitness = {}
numPics = {}

for line in f:
    cnt += 1
    # if cnt > 10:
    #     break
    if cnt % 200 == 0:
        print(cnt)

    before_joining_loseit = set()

    username = (line.strip())
    sub_dict = {}
    filename = "C:/Users/burha/Desktop/Weight Loss/User_post_files/" + \
        username + "_posts.txt"

    if username not in numCommsInEachType:
        numCommsInEachType[username] = {}

    try:
        h = open(filename, "r")
        for x in h:
            s_json = ast.literal_eval(x)
            this_date = s_json['created_utc']
            this_date_readable = dt.datetime.fromtimestamp(
                int(this_date)
            ).strftime('%y-%m')

            this_subreddit = str(s_json['subreddit'])

            if this_date_readable not in numCommsInEachType[username]:
                numCommsInEachType[username][this_date_readable] = [0, 0, 0, 0]

            if this_subreddit in listOf_Food:
                numCommsInEachType[username][this_date_readable][0] += 1

            if this_subreddit in listOf_Diet:
                numCommsInEachType[username][this_date_readable][1] += 1

            if this_subreddit in listOf_Fitness:
                numCommsInEachType[username][this_date_readable][2] += 1

            if this_subreddit in listOf_Pics:
                numCommsInEachType[username][this_date_readable][3] += 1

        for m in numCommsInEachType[username]:
            timeid = mosyears.index(m)
            uniquestring = username + str(timeid)
            s = username + "," + str(timeid) + "," + uniquestring + "," + \
                str(numCommsInEachType[username][m])[1:-1]
            fileData.write(s + "\n")
        # g.write(username + "," + str(numFood[username]) + "," + str(numDiet[username]) + "," + str(
        #     numFitness[username]) + "," + str(numPics[username]) + "\n")

    except:
        continue


f.close()
h.close()
g.close()
