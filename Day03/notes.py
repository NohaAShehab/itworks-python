#
# print(name)
# if name.isspace():

# while True:
#     name = input("plz enter your name ... : ")
#     if not name.isspace() and len(name) != 0 and name.isalpha():
#         print(name)
#         break
#     # validate name only characters noha20
#

# numbers
# task01 --> validate the string input to be only numbers or float, other -
while True:
    salary = input("plz enter your salary ... ")
    print(type(salary))
    # isdigit ---> make sure ---> only digits
    if not salary.isspace() and len(salary) > 0 and salary.isdigit():
        salary = float(salary)
        print(salary)
        break
