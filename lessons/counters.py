"""practicing counters"""

num_string: int = "123"

num_of_odd: int = 0

if int(num_string[0]) % 2 == 1:
    num_of_odd = num_of_odd + 1

if int(num_string[1]) % 2 == 1:
    num_of_odd = num_of_odd + 1

if int(num_string[2]) % 2 == 1:
    num_of_odd = num_of_odd + 1





print(num_of_odd)


