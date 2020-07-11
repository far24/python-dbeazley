# bounce.py

# initialization
bounce_height = 100
bounce_num = 0

while bounce_num < 10:
    bounce_height = bounce_height * (3/5)
    bounce_num += 1
    # print like table
    print( bounce_num, round(bounce_height, 2))

# Exercise 1.5
