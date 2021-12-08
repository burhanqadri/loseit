import praw
import timeit
import ast
from psaw import PushshiftAPI

api = PushshiftAPI()

food_health_fitness = {'askculinary',
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
                       'tequila',
                       'cico',
                       'progresspics',
                       'ownit',
                       'gainit',
                       'Myfitnesspal',
                       'keto',
                       'eatcheapandhealthy',
                       'mealprepsunday',
                       'intermittentfasting',
                       'Volumeeating',
                       '1200isplenty',
                       '1200isplentyketo',
                       'vegan1200isplenty',
                       '1500isplenty',
                       'fitness',
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
                       'gainit',
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
                       'loseit',
                       'loseit_classic',
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
                       '4hourbodyslowcarb',
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
                       'wma',
                       'bodygallery',
                       'brogress',
                       'GuessMyBF',
                       'nakedprogress',
                       'progresspics',
                       'runwild'}

for item in food_health_fitness:
    item = item.lower()

g = open("topLoseitCommenters.txt", "r")
# g = open("authors_gendered.txt", "r")
ggg = open("all_flaired.txt", "r")
# g = open("authors_loseit_comments.txt", "r")

flairedList = []
for line in ggg:
    flairedList.append(line.strip())

cnt = 0
flaircnt = 0

for x in g:
    cnt += 1

    # if(cnt == 34175):
    #     continue
    # if not(cnt % 5 == 4):
    username = (x.strip())

    if username not in flairedList:
        continue
    else:
        flaircnt += 1

    # filename = "C:/Users/burha/Desktop/Weight Loss/User_comment_files/" + username + "_comments.txt"
    filename = "C:/Users/burha/Desktop/Weight Loss/User_post_files/" + \
        username + "_posts.txt"

    try:
        h = open(filename, "r")
        h.close()
        continue
    except:
        print(flaircnt, cnt, username)

        if(cnt == 34175):
            continue

        # username = "Clementine_Fandango"
    start = timeit.default_timer()
    gen = api.search_comments(author=username, filter=['author', 'subreddit']
                              )
    # gen = api.search_comments(author=username, filter=['author', 'body', 'subreddit']
    #                           )
    # gen = api.search_comments(author=username, filter=['author', 'body', 'id', 'is_submitter', 'link_id', 'parent_id', 'score', 'send_replies', 'subreddit']
    #                         )
    # gen = api.search_comments(author=username, filter=['author', 'author_flair_text', 'body', 'controversiality', 'gilded', 'id', 'is_submitter', 'link_id', 'parent_id', 'score', 'send_replies', 'subreddit']
    #                           )
    # gen = api.search_submissions(author='BigAngel92', filter=[
    #                              'author', 'author_flair_text', 'link_flair_text', 'id', 'is_robot_indexable', 'is_self', 'link_flair_text', 'num_comments', 'score', 'selftext', 'send_replies', 'subreddit', 'subreddit_subscribers', 'title', 'upvote_ratio'])

    results = list(gen)
    stop = timeit.default_timer()
    print('Time: ', stop - start)
    # if(len(results) > 5000):
    #     print(username, len(results))
    #     continue

    f = open(filename, "a")
    seen = []
    seen_unrelevant = []
    for c in results:
        try:
            cc = str(c)
            loc = cc.find("d_={")
            cc = cc[loc+3: -1]

            s_json = ast.literal_eval(cc)

            this_subreddit = s_json['subreddit'].lower()
            if this_subreddit in seen:
                f.write(cc + "\n")
            elif this_subreddit in seen_unrelevant:
                continue
            elif this_subreddit in food_health_fitness:
                f.write(cc + "\n")
                seen.append(this_subreddit)
            else:
                seen_unrelevant.append(this_subreddit)
        except:
            continue

    f.close()
