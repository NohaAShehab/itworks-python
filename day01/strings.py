# # # string encoding ---> each character is represented using code ,, code
# # # value --? 0 to 255
# # # machine ---> 0,1 ---> encoding ---> output
# #
# # # unicode --> utf8
# # ## encoding ===>
# #
# # x = "itidgfdg"  # as an array
# # print(len(x))
# #
# # # access string part according index --? start from 0
# # print(x[-1])
#
# # string functions
# # # interpretation
# # name = "Noha Abd El-Hady Abd El-H@dy Shehab"
# # print(name[100])  # index 1 to 6
# #
# # fname = "Noha "
# #
# # mid= "Abd El-Hady "
# #
# # lastname = "Shehab"
# #
# # fullname = fname + mid * 2+ lastname
# #
# # print(fullname)
# # x = "mohamed sayed"
# # print(x.capitalize(), x)  # capatalize return with new string 0--> start with capital letter.
# #
# #
# # greet = "my name is @ and I lives in @ ,,,, @ ..... @ "   # pattern
# # print(greet.replace("@", "iti"))
#
#
# name, email  = "noha", "nshehab@iti.gov.eg"
# x = "10"
# # string functions
# # is_digit
# print(x.isdigit())  # check the value inside the string is digit
#
# #is_alpha # check all symbols value inside the string are characters
# print(email.isalpha())
# # is_numeric
# print(name.isnumeric())


x = "556"  # ---> convert to float then covert to int
x = float(x)
print(x)