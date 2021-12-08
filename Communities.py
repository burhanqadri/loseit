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

# g = open("authors_loseit_posts.txt", "a")
g = open("all_communities.txt", "a")
g_includingamount = open("all_communities_includingamount.txt", "a")
gg = open("all_communities_before_loseit.txt", "a")
# gg = open("all_communities_before_progresspics.txt", "a")

g.write('username,numFood,numDiet,numFitness,numPics,fullList\n')
g_includingamount.write(
    'username,numFood,numDiet,numFitness,numPics,fullList\n')
gg.write('username,numFood,numDiet,numFitness,numPics,fullList\n')


# C:/Users/burha/Desktop/Weight Loss/
f = open("C:/Users/burha/Desktop/Weight Loss/authors_loseit_comments.txt", "r")
# f = open("C:/Users/burha/Desktop/Weight Loss/authors_progresspics_posts.txt", "r")

cnt = 0
s = ""

authors = {}
subreddits = {}

numFood = {}
numDiet = {}
numFitness = {}
numPics = {}

for line in f:
    debug = "start"
    cnt += 1
    # if cnt > 200:
    #     break
    if cnt % 2000 == 0:
        print(cnt)

    before_joining_loseit = set()

    username = (line.strip())
    sub_dict = {}
    BeforeLoseIt_sub_dict = {}
    filename = "C:/Users/burha/Desktop/Weight Loss/User_post_files/" + \
        username + "_posts.txt"

    before_food = 0
    before_diet = 0
    before_fitness = 0
    before_pics = 0

    numFood[username] = 0
    numDiet[username] = 0
    numFitness[username] = 0
    numPics[username] = 0

    try:
        h = open(filename, "r")
        for x in h:
            s_json = ast.literal_eval(x)
            this_subreddit = str(s_json['subreddit'])

            if this_subreddit == 'loseit':
                before_joining_loseit.clear()
                before_food = 0
                before_diet = 0
                before_fitness = 0
                before_pics = 0
                BeforeLoseIt_sub_dict = {}
            else:
                before_joining_loseit.add(this_subreddit)

            if this_subreddit in sub_dict:
                sub_dict[this_subreddit] += 1
            else:
                sub_dict[this_subreddit] = 1

            if this_subreddit in BeforeLoseIt_sub_dict:
                BeforeLoseIt_sub_dict[this_subreddit] += 1
            else:
                BeforeLoseIt_sub_dict[this_subreddit] = 1

            if this_subreddit in listOf_Food:
                numFood[username] += 1
                before_food += 1

            if this_subreddit in listOf_Diet:
                numDiet[username] += 1
                before_diet += 1

            if this_subreddit in listOf_Fitness:
                numFitness[username] += 1
                before_fitness += 1

            if this_subreddit in listOf_Pics:
                numPics[username] += 1
                before_pics += 1
        debug += "potato"

        BeforeLoseIt_dict_string = ""
        dict_string = ""
        simple_dict_string = ""

        debug += "GPTJERE"

        for w in sorted(BeforeLoseIt_sub_dict, key=BeforeLoseIt_sub_dict.get, reverse=True):
            if not w == "loseit":
                BeforeLoseIt_dict_string = BeforeLoseIt_dict_string + \
                    str(w) + "|"
            # BeforeLoseIt_dict_string = BeforeLoseIt_dict_string + \
            #     str(w) + ":" + str(BeforeLoseIt_sub_dict[w]) + "|"

        for w in sorted(sub_dict, key=sub_dict.get, reverse=True):

            dict_string = dict_string + str(w) + ":" + str(sub_dict[w]) + "|"
            simple_dict_string = simple_dict_string + str(w) + "|"

        BeforeLoseIt_dict_string = BeforeLoseIt_dict_string[:-1].replace(
            "\'", '')
        dict_string = dict_string[:-1].replace("\'", '')
        simple_dict_string = simple_dict_string[:-1].replace("\'", '')

        # debug += "15"
        g_includingamount.write(username + "," + str(numFood[username]) + "," + str(numDiet[username]) + "," + str(
            numFitness[username]) + "," + str(numPics[username]) + "," + dict_string + "\n")
        g.write(username + "," + str(numFood[username]) + "," + str(numDiet[username]) + "," + str(
            numFitness[username]) + "," + str(numPics[username]) + "," + simple_dict_string + "\n")

        if "set" not in str(before_joining_loseit):
            before_string = str(before_joining_loseit)[1:-1].replace(", ", "|")
            before_string = before_string.replace("\'", '')
            gg.write(username + "," + str(before_food) + "," + str(before_diet) + "," +
                     str(before_fitness) + "," + str(before_pics) + "," + BeforeLoseIt_dict_string + "\n")

            # gg.write(username + "," + str(before_food) + "," + str(before_diet) + "," +
            #          str(before_fitness) + "," + str(before_pics) + "," + before_string + "\n")
        else:
            gg.write(username + ",,,,," + "\n")

    except:
        print(username, debug)
        continue


f.close()
h.close()
g.close()
