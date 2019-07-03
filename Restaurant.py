import random
name = input("Who is using restaurant picker? ")

rlist = ["RioGrande", \
         "BurgerCo", \
         "Easterbys", \
         "OCharleys", \
         "Habachihut"]

rchoice=random.choice(rlist)

print(name + ', I suggest '+ rchoice)
