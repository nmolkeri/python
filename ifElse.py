import sys

n = int(input())
if n%2 == 0 and n<2:
   print("Not Weired")
elif n%2 ==0 and  n >= 2  and n <= 5:
   print("Not Wiered")
elif n%2==0 and n >= 6 and n<=20:
   print("Weired")
elif n%2 == 0 and n > 20:
   print("Not Wiered")
elif(n%2 != 0):
   print("Weired")
 
