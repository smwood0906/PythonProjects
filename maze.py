# Created Week 2 of Bootcamp. Create a game that allows a user to move through a maze, making choices about directions
#and being brought to different rooms. I chose to rewrite mine as a travel adventure, because I like to imagine being on
#vacation.
#This game was written using only Functions, a later version incorporates Classes.
def game():
    print('Are you ready to Choose Your Vacation Adventure?')
    print((' ')*40)
    print('''Make it through at least 7 destinations without getting sent back to Portland!\
    Get your passport stamped in each location to earn First Class status for life!''')

    current_room = room0()

    while current_room != exit:
        current_room = current_room()

    current_room()


def process_user_movement(description, doors):

    print(description)
    options = list(doors.keys())

    print('You could try '+ ', '.join(options[0:-1]) + ' or ' + options[-1] + '.')
    while True:
        choice = input('Which adventure would you like to take? : ')
        if choice.lower() in options:
            return doors[choice]
        else:
            print('I didn\'t understand that, please try again.')
            print((' ')*40)
            print('-->')


def room0():

    description = '''Looks like you\'re at the Portland airport. While the food here is delicious,\
     and reasonably priced, this carpet is making you dizzy.\
     \
     There are three flights leaving soon that you\'ve got time to catch.'''
    doors = {'vegas': room6, 'cabo': room1, 'amsterdam': room2}

    return process_user_movement(description, doors)

def room1():
    description = '''Viva Mexico!  You spend a few days relaxing on Medano beach, sipping 2 for 1 margaritas\
    and getting a tan. You head up to Todos Santos for a day and visit the Hotel California, then come back for\
    an evening water taxi to Lover's Beach.\

    You\'re starting to feel a little dehydrated and worn out from all the heat. A couple you met at Cabo Wabo offered you\
    their hometown apartment as a place to stay while they finish their time in Mexico.\

    You could call the airline and change your flight, or keep your ticket home.'''

    doors = {'apartment': room7, 'home': room0}
    return process_user_movement(description, doors)

def room2():
    description = '''Amsterdam!! Somehow it has been two days since you arrived, but you can\'t remember the first one. \
    \
    You find ticket stubs to the Anne Frank House and the Van Gogh Museum in your wallet, so it seems like a good trip so far!\
    It also appears that you have maxed out your credit card, which limits your options to the $78 in cash you have in \
    your wallet. Well, that and your unmatched charm.\
    \
    There is a bus headed South that you can afford, you can take that stranger up on their offer for a place to crash for the night,\
    or you can call your Mom and beg for a flight home.'''
    doors = {'bus': room3, 'mom': room0, 'stranger': room8}
    return process_user_movement(description, doors)

def room3():
    description = '''Paris! You\'ve managed to squeeze in a trip the Louvre,\
    the Eiffel Tower, and Notre Dame. But, you\'ve also had your fill of wine and cheese and are ready to head to your\
    next destination.\
\
    You get a killer flight deal alert on your phone, but can\'t see where to.\
    You\'ve also been dying to take the Chunnel (underwater train) to London.\
    You\'re also tempted to join some new friends from the hostel on a ski trip to Switzerland.'''

    doors = {'flight': room6, 'chunnel': room4, 'skiing': room5}
    return process_user_movement(description, doors)

def room4():
        description = '''London would probably be more fun if your wallet and passport hadn\'t been stolen on the tube! Lucky for you,\
        you charmed the pants off the security guard at Big Ben. Who could have known it was the Queen\'s third cousin?
        \
        Maybe if you\'re lucky she can help you get back some identification and funding and send you on to your next desination!\
        Do you want to meet the Queen, or take your chances with the embassy?'''
        doors = {'queen': room3, 'embassy': room0}
        return process_user_movement(description, doors)

def room5():
    description = '''Switzerland! What an incredible three days of skiing in the Swiss Alps! It snowed every day making the powder something you\'d\
    only ever dreamed about! Unfortunately, all that snow has closed down most transportation options and it looks like you\'re\
    either going to have to go back the way you came or hitch a ride with that ski racing team on their bus.'''
    doors = {'backtrack': room3, 'bus': room2}
    return process_user_movement(description, doors)

def room6():
    description = '''Vegas baby! You\'ve now been awake for three days straight! \
    You got married by Elvis, then had it anulled a few hours later. You\'ve been a special guest on\
    three separate bachelorette party buses, and you\'re seriously considering a career change to the Cirque du Soleil.\
    \
    You\'re about out of money, but can\'t resist one more roll at the craps table... JACKPOT!\
    Do you want to quit while you\'re ahead and go home? Or, maybe take that expensively dressed gentleman up on his offer\
    to discuss a business proposition in his suite? Shoot, you could also just buy a private jet with your winnings\
    and fly anywhere you want! '''
    doors = {'home': room0, 'business': room8, 'jet': room7}
    return process_user_movement(description, doors)

def room7():
    description = '''You\'ve always wondered what Iceland would be like! After viewing some fantastic northern lights in Reykjavik, \
    and a relaxing spa weekend at the Blue Lagoon hot pools, it\'s time for another adventure.\
    \
    You are tempted by that couple\'s offer to join them on their kayak trip in Greenland to look for narwhals, \
    it is your favorite animal after all.\
    You could also leave all this cold weather behind and head for a nice beach somewhere.\
    There\'s also this guilt that\'s been building, maybe you should learn something historical on your next trip?.\
    Then again, some rowdy American nightlife might be a nice way to mix things up.'''

    doors = {'beach': room1, 'usa': room6, 'kayak': room9, 'history': room10}

    return process_user_movement(description, doors)

def room8():
    description = '''Zanzibar! How were you supposed to know talking with that guy would land you here? \
Accidentally ending up on an island with crystal white beaches isn\'t a bad surprise though.\
\
You hop on the ferry to Tanzania, take a quick jog up Kilimanjaro, then finish off with a short \
safari to the Ngorongoro Crater and the Serengeti. Not a bad trip, but these malaria pills are \
giving you crazy dreams and you\'re ready to head out.\
\
You can take your new friend\'s offer for a flight back to where you started.\
Or, you can let the agent at the travel counter pick your next destination for you.'''

    doors = {'backtrack': room6, 'agent': room10}
    return process_user_movement(description, doors)

def room9():
    description = '''Greenland! After a cold, exhausting, and exciting kayak trip you finally see your favorite animal, the narwhal, \
    in real life! Next up is a visit to the viking ruins and the Hvalsey Fjord Church. Then one more stop at the breathtaking\
    Illulissat ice-fjord.\
    \
    All these chilly endeavors are making you long for those sweet Icelandic hot pools though.\
    One more dip in the springs, or take a chance with your travel app again?'''

    doors = {'springs': room7, 'chance': room10}
    return process_user_movement(description, doors)

def room10():
    description = '''Egypt! This has to be the final destination on your vacation adventure\
     because you are running dangerously low on funds!\
     \
     But you aren\'t heading home without playing tourist at the Great Pyramids, the Sphinx, and\
     the Valley of the Kings.\

     You are ready to show your passport to your travel agency to claim your lifetime First Class status,\
     when a slightly shady looking fellow offers to take you to King Tut's tomb for free.'''

    doors = {"tomb": room0, 'agency': exit}
    return process_user_movement(description, doors)

game()
