'''
##############
Lab 3.01
##############
1.  Practice importing random** — Use randint with different arguments. Simulate a dice roll, printing out to the user what number they rolled.
import random

input("Hit enter to roll the dice")
user_roll = random.randint(0,6)
print(f"You rolled a {user_roll}")

2.  Look at the documentation of the random library — Experiment with another function (not randint) that returns a value.
import random
random_thing =random.choice(['rock' , 'paper', 'scissors'])
print(random_thing)

3.  Create a program that simulates a magic 8-ball​
    1.  Store all of the 8-ball's possible responses (shown below) in a list

    2.  Have the program prompt the user to ask the magic 8-ball a question

        then return and print a random response.

Magic 8-Ball Response Examples
Outlook is good

Ask again later

Yes

No

Most likely no

Most likely yes

Maybe

Outlook is not good
'''
import random
Playing =True
player_question = input('Ask any question!')
ball_responses =random.choice(['Outlook is good', 'Ask again Later', 'Yes', 'No', 'Most likely no', 'Most likely yes', 'Maybe', 'Outlook is not good'])
print(ball_responses)
answer = input("Would you like to ask another question? (y/n)")
if answer == 'y':
    player_question = input('Ask any question!')
    ball_responses =random.choice(['Outlook is good', 'Ask again Later', 'Yes', 'No', 'Most likely no', 'Most likely yes', 'Maybe', 'Outlook is not good'])
    print(ball_responses)
elif answer == 'n':
    print("Thanks for playing")
    
