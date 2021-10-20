# falsy values

# None, "", 0, False, [], (), {}

names = ["Mohamed", "Rana", "Zeina"]
# names[3] = "fff"
names.append("Noha")
# pop ---> last item ---> pop with index
print(names)
# remove item
names.remove("Noha")
print(names)

####

x = [5,6,7]
x = "test"
del(x)  # remove the reference from the memory
print(x)

l = ["abc"]