# ## sometimes you need to return with a function
# def test(varr):
#     return f"{varr}"
#
# # divide function behaviour
# def sayhello(name):
#     print(f"Good morining team {name}, Hope you will sweet Nov")
#     # return True  # retrun with function
#     return lambda lastname: f"Good morning Eng {name} {lastname}"  #Anoymous
#     # return test("abc")
#
#
# print(sayhello("Ahmed")("Ali"))  # retrurn with function


# x = sayhello("Rana") # return with function can be callled
# x is not the function name
# print(x("Sameh"))
# print(x)


#### iter
l = [3, 45, 566, "test"]
# for i in l:
#     print(i)

m = iter(l)
print(m)
# print(next(m)) # iterator
# print(next(m))
# print(next(m))
# print(next(m))
# print(next(m))
while True:
    try:
        print(next(m))
    except:
        break

l = [5,6,7,8]
a,b,c,d = l
print("test")
