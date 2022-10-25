import random
#variables and basics
global p_rest
global day
global month
global year
global health
global food
global p_name
global miles_traveled
months_31_days = [1,3,5,7,8,10,12]
months_30_days = [4,6,9,11]
months_28_days = [2]
min_miles = 30
max_miles = 60
min_days_every_travel = 3
max_days_every_travel = 7
day=1
month=3
year=0
health = 5
miles_traveled = 0
total_miles =2000
playing = True

#functions
def space():
    print("")
    return

def add_day():
    global food
    global day
    global month
    global year
    if day >=28 and month in months_28_days:
        day = 1
        month +=1
    elif day>=30 and month in months_30_days:

        day = 1
        month +=1
    elif day>=31 and month in months_31_days:
        day = 1
        months +=1
    if month > 12:
        month =1
        day =1
        year =1
def welcome_text():
    global p_name
    p_name = input("What is your name?")
    space()
    print(f"Hello {p_name}, and welcome to the Oregon Trail!")
    print("You're starting in Independance, Missouri.")
    print("It is March 1st and you need to travel 2000 miles to Oregon by December 31st!")
    print("You have 500lbs of food and your health is 5 so you will need to hunt and rest. Good Luck!")
    space()
    return
welcome_text()
def rest():
    global p_rest
    global health
    p_rest = 5
    health = 5
    return

def travel():
    global miles_traveled
    random_miles_traveled = random.randint(min_miles, max_miles)
    miles_traveled += random_miles_traveled
    milesremaining = total_miles - miles_traveled
    random_days_traveled = random.randint(min_days_every_travel, max_days_every_travel)
    for day in range(random_days_traveled):
        add_day()

    
    return
def hunt():
    global food
    food = 100
    print("You have gathered 100 pounds of food! Congratulations!")
    return

def status():
    

#game loop
while playing:
    space()
    p_answer = input("What would you like to do? (travel, rest, hunt, status, help or quit)")
    if p_answer == 'rest':
        space()
        rest()
    elif p_answer == 'quit':
        space()
        print("Sorry to see you go! Come back soon!")
        playing = False
    elif p_answer == 'hunt':
        space()
        hunt()
    elif p_answer == 'status':
        space()
        status()
    elif p_answer == 'travel':
        space()
        travel()
    elif p_answer == 'help':
        space()
        help()
    else:
        space()
        print("This is not one of the commands!")



