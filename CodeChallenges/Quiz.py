# ONE - What does the following code do? This code creates a function (a) that takes three arguments (b,c,d), then nothing happens.
#
#  def a(b, c, d):
#      pass

# TWO - You are driving a little too fast, and a police officer stops you.
# Write code to compute the result, encoded as an int value:
#  0=no ticket, 1=small ticket, 2=big ticket.
#  If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1.
#  If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.
#
def get_a_ticket(x, y, z):  # x = speed   y = birthday  z = today
    result = 0
    if y == z:
        if x <= 65:
            result = 0
        elif x >= 66 and x <= 85:
            result = 1
        else:
            result = 2

    else:
        if x <= 60:
            result = 0
        elif x >= 61 and x <= 80:
            result = 1
        else:
            result = 2
    print(result)
#
#
# # THREE - Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat,
# # and a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring.
# # Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00".
# #  Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".
def alarm(day, vacation):
    time = "0:00"
    if vacation == False:
        if 1 <= day <= 5:
            time = "7:00"
        elif day == 0 or day == 6:
            time = "10:00"
    else:
        if 1 <= day <= 5:
            time = "10:00"
        elif day == 0 or day == 6:
            time = "off"
    print(time)

# #
# # FOUR - Define a function max() that takes two numbers as arguments and returns the largest of them.
def max(x,y):
    if x > y:
        return x
    else:
        return y

#
# # FIVE - Define a function that computes the length of a given list or string.
# def length_of_string(something):
#     print(len(something))

#
# SIX - Define a function reverse() that computes the reversal of a string.
# For example, reverse("I am testing") should return the string "gnitset ma I".

def reverse_order(test):
    print(test[::-1])

#
# SEVEN - Create a function that takes in a string and sorts each word in that string into a
# dictionary where the key is a word from the string and the value is how many times that word is in the string.
# The end output should look something like this:
#    {'word from string': number of times the word is in string}

def are_you_kidding_me_chris(text):
    words = text.split()
    word_dict = {}

    for word in words:
        if word in word_dict.keys():
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    print(word_dict)

are_you_kidding_me_chris("It is true for all that that that that that that that refers to is not the same that that that that refers to.")




#

