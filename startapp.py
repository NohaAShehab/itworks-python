from userinfo import loginfun, registerfun

choice = input("plz enter your choice r , l ")
if choice == "r" or choice == "l":
    if choice == "r":
        loginfun()
    else:
        registerfun()
else:
    print("plz provide valid choice,,,")

