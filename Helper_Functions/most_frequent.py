# Date    : 15/08/22 5:47 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0

def most_frequent(arg):
    count = 0
    num = arg[0]
    for i in arg:
        curr_frequency = arg.count(i)
        if curr_frequency > count:
            count = curr_frequency
            num = i
    num = str(num)
    num = num.replace('_', ' ')
    number = "1234567890"
    num1 = ""
    for i in num:
        if i not in number:
            num1 += i
    return num1
