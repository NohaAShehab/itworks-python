
# python provide different built-in packages can be used with application

# import math
#
# a = 3.444
# print(math.floor(a))
#
#
# print(math.sqrt(9))
#
#
# print(math.fabs(9))  # return float
#
#
# print(math.factorial(7))
# # copy sign
# print(math.copysign(10, -77))
#
# # gcd
# print(math.gcd(15, 75, 120, 135, 400))

# time module
import time
print(time.time())  # return time from 1 jan 1970 to now in seconds



# time tuple ---? consists of 9 fields
# 1- 4digit year
# 2- Month 1 to 12
# 3- Day 1 to 31   of month
# 4- Hour 0 to 59
# 5- second 0 to 59
# 6- second 0 to 59
# 7- Day of week 0 to 6
# 8- Day of year 1 to 365
# 9- Daylight saving -1 0 1


# print(time.localtime(7867868798))  # time in struct time
# time.localtime(time.time()) --> get time in seconds, then add it to the format struct time
# print(time.asctime(time.localtime(time.time()))) # coverting time into human readable form


import calendar
yy = 1992
mm = 6
print(calendar.calendar(2021,2,1,1))
