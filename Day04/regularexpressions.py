import re   # stands for regurlar expression
# # regular expressions --> pattern ---> used to validate inputs
#
# p = re.compile('[a,e,i,o,u]')
# print(p)  # create your regular expression
# txt = "We are very calm "
# print(p.findall(txt))
#
# name = "Rana"
# l = ["5",66, 77, 88, 77]
# print(len(name), len(l))
#
# print(name.count("a"))  # count string or substring within the given string
# # return the number of the items with given item
# print(l.count(77))

# dic ={"name":"Ahmed", "lanme":"Ahmed"}
# print(list(dic.values()).count("Ahmed"))

memail = "nshehab@iti.gfjhjkeshfituooutrjg.hfghfhgf@hjghfjj"
mailpattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
print(re.match(mailpattern, memail))
# object ---> re.Match object, else None object

# match --> if zero or more character match pattern ---> return match object
# fullmatch --> whole string must match the regural expression

# re.search()