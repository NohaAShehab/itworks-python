# strings primitive data structure
# strings are immutable ---> cannot be changed after created

x = "iti"
x = "itworks"


# concatination
y = x + " " + "python training"

# repeated string *

# format string
name = "Noha"
faculty = "Engineering"
# greet = "My name is {0} I graduated from faculty of {1}"  # create common format
# print(greet.format(name, faculty))
# greet = "My name is {n} I graduated from faculty of {f}"  # create common format
# print(greet.format(f=faculty, n=name))

name = 10
# f-string
greet = f"My name is {name} I graduated from faculty of {faculty}"  #string template
# create common format
print(greet)

# greet = "My name is " + name + "I graduated from  faculty of " + faculty
# print(greet)

# template strings --

#formatter class  (%) --> built-in ---> interpolation operator


# string replace ---> search inside string  --> replace


# search inside string ---> find

# s1 = "I need a break"
# s2 = "break"
# print(s1.find(s2))  # return index , else -1
# # count substring
# print(s1.count("breakh"))
# # count spaces
# s3 = " "   #space
# print(s3.isspace())
# capital or small
name = "itI" #  ---> islower ---> conver .lower()
print(name.lower())
# string strip
# string.strip , lstrip , rstrip
greet = "     welcome to day02       "
print(len(greet))
greet = greet.rstrip()
print(len(greet))


