import random

#functions
def space():
    print("")


def add_day():
    global food
    food-=5

    global day
    global month
    global year

    day+=1

    global health
    if day == 11 or day == 24:
        health-=1

    if day >=28 and month in months_28_days:
        day = 1
        month +=1
    elif day>=30 and month in months_30_days:
        day = 1
        month +=1
    elif day>=31 and month in months_31_days:
        day = 1
        month +=1

    if month > 12:
        global playing
        month =1
        day =1
        year =1
        print("You did not make it in time!")
        playing = False

def welcome_text():
    global p_name
    p_name = input("What is your name?")
    space()
    print(f"Hello {p_name}, and welcome to the Oregon Trail!")
    print("You're starting in Independance, Missouri.")
    print("It is March 1st and you need to travel 2000 miles to Oregon by December 31st!")
    print("You have 500lbs of food and your health is 5 so you will need to hunt and rest. Good Luck!")
    space()
    
#travel
def travel():
    global playing
    global miles_traveled

    random_miles_traveled = random.randint(min_miles_every_travel, max_miles_every_travel)

    miles_traveled += random_miles_traveled
    milesremaining = total_miles - miles_traveled
    random_days_traveled = random.randint(min_days_every_travel, max_days_every_travel)

    print(f"You've traveled {random_days_traveled} days for {random_miles_traveled} miles for a total of {miles_traveled} miles traveled")
    print(f"You have {milesremaining} miles left until Oregon")

    for day in range(random_days_traveled):
        add_day()
#rest
def rest():
    global health

    if health < 5:
        health+=1
        randomdaysresting = random.randint(min_days_every_rest, max_days_every_rest)
        for day in range(randomdaysresting):
            add_day()
        print(f"You rested for {randomdaysresting} days and your health is {health}")
    else:
        print("You're fully healed!")
    

#hunt
def hunt():
    global food
    food+=100
    randomDaysHunting = random.randint(min_days_every_hunt, max_days_every_hunt)
    print(f"You took {randomDaysHunting} days to gather 100 pounds of food!")
    for day in range(randomDaysHunting):
        add_day()
    
def check_status():
    global month
    global day
    global health
    global food
    print(f"Health: {health}  Food: {food} pounds  Month: {month}  Day: {day}")

def help():
    print("Reminder the question is:  What would you like to do? (travel, rest, hunt, status, help or quit)")
    

#variables and basics
months_31_days = [1,3,5,7,8,10,12]
months_30_days = [4,6,9,11]
months_28_days = [2]
min_miles_every_travel = 30
max_miles_every_travel= 60
min_days_every_travel = 3
max_days_every_travel = 7
min_days_every_rest = 2
max_days_every_rest = 5
min_days_every_hunt = 2
max_days_every_hunt = 5
min_food = 1
max_food =10
min_river_days = 1
max_river_days = 10
min_health = 0
max_health = 1
day=1
month=3
year=0
health = 5
food =500 
miles_traveled = 0
total_miles =2000
playing = True

welcome_text()


#game loop
while playing:
    space()
    p_answer = input("What would you like to do? (travel, rest, hunt, status, help or quit)")
    if p_answer == 'rest':
        space()
        rest()
    elif p_answer == 'quit':
        space()
        print("Sorry to see you go!")
        playing = False
    elif p_answer == 'hunt':
        space()
        hunt()
    elif p_answer == 'status':
        space()
        check_status()
    elif p_answer == 'travel':
        space()
        travel()
    elif p_answer == 'help':
        space()
        help()
    else:
        space()
        print("This is not one of the commands!")
    if health ==0:
        print("You died, remember to rest next time...")
        playing=False



