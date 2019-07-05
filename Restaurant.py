import random
name = input("Who is using restaurant picker? ")

rlist = ["Rio Chico", \
         "BurgerCo", \
         "Easterbys", \
         "OCharleys", \
         "Habachihut"]

rchoice=random.choice(rlist)

print(name + ', I suggest '+ rchoice)
