import random
from datetime import datetime as dt


def main():
    ''' main function'''

    date, name, speed = intro()
    restr_list = make_list(speed)
    

    while True:

        rchoice=random.choice(restr_list)
    
        print(name + ", I suggest "+ rchoice + " if you are happy with this  choice press [1] if not press [anything else]")
    
        answer=input()
    
        if answer != '1':
            continue 
        
        else:
            print('Thank you and goodbye')
            break


def intro():
    ''' basic input information'''

    day = dt.today().strftime('%Y-%m-%d')
    nm = input("Who is using restaurant picker? ")
    spd = input("Do you have time for fast [1], normal [2], slow service [3], or any [any other key]? ")
    
    return day, nm, spd


def make_list(spd):
    ''' creates the list of restaurants'''

    fast   = ["Chick-fil-A", \
              "Hibachi Hut"]

    medium = ["Rio Chico", \
              "Senor Tequila", \
              "Easterby's", \
              "O'Charley's", \
              "Boxcar Betty's",
              "Famulari's Pizzeria"]

    slow =   ["Outback", \
              "Red Lobster", \
              "Crab Shack", \
              "Red Orchid", \
              "La Fontana", \
              "3 Matadors Tequileria"]

    if spd == '1':
        rlist = fast

    elif spd == '2':
        rlist = medium

    elif spd == '3':
        rlist = slow

    else:
        rlist = fast + medium + slow

    return rlist


if __name__ == '__main__':
	main()        
