import math
import os
import random
import re
import sys

s = "12:01:00AM"

def timeConversion(s):
    hour, minute, second_AMPM = s.split(':')

    if second_AMPM[2:] == "PM" and hour != '12':
        hour =str(int(hour)+12)
    if second_AMPM[2:] == "AM" and hour == '12':
        hour = "00"
    if second_AMPM[2:] == "PM" and hour == '12':
        hour = "12"

    conversion_time = hour + ':' + minute + ':' + second_AMPM[0:2]

    return conversion_time

print(timeConversion(s))