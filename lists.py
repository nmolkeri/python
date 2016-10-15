import sys

a = []
a.append("x")
print (a[0])

inc = input()
comm, value = inc.split(" ")
while(inc!="quit"):
   if(comm == "insert"):
      print("Insert")
   if(comm == "delete"):
      print("Delete")
   print("Input")
   inc = input()
   if(inc != "quit"):
      comm, value = inc.split(" ")
