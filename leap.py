import sys


def leapYear(year):
   leap = False
   if(year % 4 == 0):
      if(year % 100 == 0):
         if(year % 400 == 0):
            leap = True
         else:
            leap = False
      else:      
         leap = False
   else:
      leap = False
   return leap


year = int(input())
x =  leapYear(year)
print(x)
