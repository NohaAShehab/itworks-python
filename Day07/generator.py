# create generator for a value
def genItems(end):
    for i in range(end):
        yield i


genn = genItems(500000000000)  # generator object 0
# print(next(genn)) #0
# print(next(genn))
# print(next(genn))
# print(next(genn))
# print(next(genn))

# one place is re
# served for the generator , start ,step =1

# l = []
# for i in range(50000000000):
#     l.append(i)
#
# # print(l)
#
# for i in genn:
#     print(i)

# apply logic on itertable

# l = [10,30,50,70]

# newl = map(lambda x:x+10,l)
# print(newl)  #map object
# print(type(newl))  # map
# print(list(newl))
#
# ll = []
# for i in l:
#     ll.append(i+10)
#
# print(ll)


# def myfun(*args):
#     data = map(lambda item:item.strip(), args)
#     data = list(data)
#     print(data)
#
# myfun("Ahmed", "    Ali ", "Rana   ", "Zeina ")


# filter items that satisfy condition in itertable

x = [10, 45, 88, 666, 7666, 105]
y = []
# for i in x :
#     if i %5 ==0:
#         y.append(i)
#
# print(y)
# y = filter(lambda m: m % 5 == 0, x) #filter object ---> casting to any sequence
# print(list(y))


# casting dic into list
# dictt = {"track":"python", "students":10}
# mylist = list(dictt)
# print(mylist)
#
# l = [5,6,7,7]  # dictionary key and value  ,
# mydic = dict(l)  #{0:5, 1:6}
# print(mydic)