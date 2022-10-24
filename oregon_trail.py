playing =True
global p_rest
global day
global health
global food
p_name = input("What is your name?")
print("")
print(f"Well, hello there {p_name}")
print("")
print("Your destination is Oregon by December 31st!")
def rest():
    global p_rest
    global health
    p_rest = 5
    health = 5
    return
rest()

def travel():
    global day
    day = 1
    print(day)
    return
def hunt():
    global food
    food = 100
    print("You have gathered 100 pounds of food! Congratulations!")
    return
def status():
    fs = 3
while playing:
    p_answer = input("What would you like to do? (travel, rest, hunt, status, help or quit)")
    if p_answer == 'rest':
        rest()
    elif p_answer == 'quit':
        playing = False
    elif p_answer == 'hunt':
        hunt()
    elif p_answer == 'status':
        status()
    elif p_answer == 'travel':
        travel()
    elif p_answer == 'help':
        help()
    else:
        print("This is not one of the commands!")

    

