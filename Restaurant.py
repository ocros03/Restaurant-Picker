import random

name = input("Who is using restaurant picker? ")

rlist = ["Rio Chico", \
         "Senor Tequila", \
         "Easterby's", \
         "O'Charley's", \
         "Hibachi Hut"]



while True:

    rchoice=random.choice(rlist)
    
    print(name + ', I suggest '+ rchoice+ ' if you are happy with this choice press 1 if not press anything else')
    
    answer=input()
    
    if answer != '1':
        continue 
        
    else:
        print('Thank you and goodbye')
        break
        
