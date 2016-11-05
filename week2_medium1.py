#Write a function
#https://www.hackerrank.com/challenges/write-a-function/submissions/code/26968725

def is_leap(year):
    leap = False
    # Write your logic here
    if year % 4 == 0:
        leap = True
    if year % 100 == 0:
        leap = False
        if (year % 100) == 0 and (year % 400) == 0:
            leap = True
    return leap
