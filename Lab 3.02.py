'''
############
Lab 3.02
    ############
Lab Exercise 1
--------------
Create a function, birthday_song, that prints out the happy birthday song to whatever name is input as an argument. The contract should be:

  # Name: birthday_song
  # Purpose: birthday_song prints out a personalized birthday song
  # Arguments: name, string     #your code goes here

  # Returns: none

birthday_song_name = input("What's your name?")
def birthday_song(name):
    print("Happy birthday to " + name)
    print("Happy birthday to " + name)
    print("Happy birthday to " + name + " happy birthday to you!")

    return

birthday_song(birthday_song_name)

    

Lab Exercise 2
---------------
Create a function that randomly picks 5 cards from a deck 

The cards can repeat

Write out the contract for this function using the list.

number = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
Bonus
Practice passing in lists as an argument to a function.

What is different about passing in a list as an argument?

Read about list aliasing in section 3.4 of the associated reading, and write down what is happening in this case.
Remember, the associated reading is in the "SWBAT" section on moodle!
'''

import random
def random_card_picker():
    
    number = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    card1 = number[random.randint(0,12)] + " "
    card2 = number[random.randint(0,12)] + " "
    card3 = number[random.randint(0,12)] + " "
    card4 = number[random.randint(0,12)] + " "
    card5 = number[random.randint(0,12)] + " "

    print("The cards picked in order are: " + card1 + card2 + card3 + card4 + card5)

    return
    
random_card_picker()

