"""with open("file.txt","a")as f:
    f.write("ahsh")
with open("file.txt")as f:
    print(f.read())"""

"""f=open("file.txt")
print(f.read())"""
'''f=open("C:\\Users\\Netcom\\Desktop\\saijer\\file.txt")
print(f.read())'''
"""with open("file.txt") as f:
    print(f.readline(5))"""
'''with open("C:\\Users\\Netcom\\Desktop\\saijer\\file.txt") as f:
  print(f.read(8))
  print(f.readline())
  print(f.readline())'''
"""with open("C:\\Users\\Netcom\\Desktop\\saijer\\file.txt","w") as f:
    f.write("foh")
    f.write("asd")
with open("C:\\Users\\Netcom\\Desktop\\saijer\\file.txt") as f:
    print(f.read())
    f.close()"""
"""with open("saijer.txt","x") as f:
  print( f.write("dfhjh"))"""
"""import os
os.remove("files.txt")"""
"""import os""
if os.path.exists("saijer.txt"):
    os.remove("saijer.txt")
else:
    print("file not exist")"""
"""import os
os.rmdir("fd")"""
"""for i in range(10):
    print("hello world")"""
"""for i in range(1,10):
    print(i/i)"""
"""for ch in "python":
    print(ch)"""
"""for i in range(1,6):
    print(i)"""
"""fruits=["bannana,apple,orange"]
for i in fruits:
    print(i)"""
"""fruits=["apple","bannana","orange"]
for i in fruits:
    print(i)
    if i=="bannana":
      break"""
"""fruits=["apple","bannana","orange"]
for i in fruits:
    if i=="bannana":
        break
    print(i)"""
"""fruits=["apple","bannana","cherry"]
for i in fruits:
    if i=="bannana" or i=="apple":
        continue
    print(i)"""
"""for i in range(1,11):
    print(i*i)"""
"""for i in range(1,21):
    if i%2==1:
      print(i)"""
"""for i in range(1,20,2):
    print(i)"""
# for i in range(1,100):
#     if i%5==0:
# #         print(i)
# for i in range(0,100,5):
#     print(i)
# i=1
# while i<=5:
    # print(i)
    # i+=1

# i=1
# while i<=10:
#     print(i*i)
# #     i+=1
# i=1
# while i<=20:
#     if i%2==1:
#        print(i) 
#     i+=1
"""i=10
while i>=1:
    print(i)
    i-=1"""
"""for i in range(1,4,1):
   x=int(input("enter a num:"))
   if x>0:
      print("positive")
   elif x<0:
      print("negative")
   else:
      print("zero")"""
"""i=1
while i<=10:
    x=int(input("enter a num:"))
    if x>0:
        print("positive")
    elif x<0:
        print("negetive")
    else:""
        print("zero")
    i+=1"""
"""for i in range(1,11):
    print(i*3,"=",i,"x 3")"""
"""i=1
while i<=100:
    print(i*8,"=",i,"x 8")
    i+=1"""
"""i=0
while i<6:9
    i+=1
    if i ==3:
      continue
    print(i)"""
"""for i in ("apple","bannana","cherry"):
    if i=="bannana":
        break
    print(i)"""
"""for i in ["apple","bannana","cherry"]:
    if i=="bannana":
        break
    print(i)"""
"""for i in ("apple","bannana","cherry"):
    if i=="bannana":
        continue
    print(i)"""
"""i=1
while i<=6:
    if i ==3:
      break
    print(i)
    i+=1
"""
"""i=1
while i<=6:
    print(i)
    if i ==3:
      break
    i+=1"""
"""i=1
while i<10:
    print(i)
    i+=1
else:
    print("i is not lesser than 10")"""
"""mylist=["apple","bannana","cherry"]
print(mylist)"""
"""ist=["apple","bannana","cherry"]
for x in mylist:
     print(x)"""
"""i=0
while i<10:
    i+=1
    print(i)"""
"""thislist=["apple","bannana","cherry","kiwi","orange","melon"]
print(thislist[2:5])"""
"""thislist=["apple","bannana","cherry"]
thislist[1]="kiwi"
print(thislist)"""
"""thislist=["apple","bannana","cherry","kiwi","orange","melon"]
thislist[1:4]="jackfruit","lemon"
print(thislist)"""
"""movies=["animal","kgf","they call him og","lucky bhaskar"]
print("first movie",movies[0])
print("last movie",movies[-1])
movies[1]="bahubali"
print("updated list",movies)"""
"""fruits=["kiwi","cherry","jackfruit","pappaya","orange"]
fruits.append("apple")
fruits.insert(2,"mango")
print(fruits)"""
"""marks=[60,40,30,20,90]
marks[1]=35
marks.append(45)
marks.pop(3)
print(marks)"""
"""evenlist=[]
oddlist=[]
for x in range(1,31):
    if x%2==0:
        evenlist.append(x)
    else:
        oddlist.append(x)
print("evenlist",evenlist)
print("oddlist",oddlist)"""
"""evenlist=[]
oddlist=[]
i=1
while i<31:
    if i%2==0:
        evenlist.append(i)
    else:
        oddlist.append(i)
    i+=1
print(evenlist)
print(oddlist)"""
"""num=[23,45,56,78,90]
smallest=min(num)
largest=max(num)
print(smallest)
print(largest)"""
"""list=[]
evenlist=[]
oddlist=[]
n=int(input("enter the number of elements:"))
for i in range(n):
    user_input=int(input("enter a number"))
    list.append(user_input)
    print(list)
for i in list:
    if i%2==0:
        evenlist.append(i)
    else:
        oddlist.append(i)
print("even numbers in list",evenlist)
print("odd numbers in list",oddlist)"""


"""list=[]
unique=[]
repeat=[]
n=int(input("enter number of elements:"))
for i in range(n):
    user_input=int(input("enter a number:"))
    list.append(user_input)
for i in list:
   if list.count(i)>1:
       repeat.append(i)
   else:
       unique.append(i)
print(repeat)
print(unique)
print(len(unique))"""

"""list=[]
unique=[]
n=int(input("enter number of elements:"))
for i in range(n):
    user_input=int(input("enter a number:"))
    list.append(user_input)
for i in list:
   if list.count(i)==1:
       unique.append(i)
print(unique)
print(len(unique))"""
"""x=("apple","banana","kiwi")
y=list(x)
y[1]="cherry"
x=tuple(y)
print(x)"""
"""thistuple=("apple","banana","cherry")
y=list(thistuple)
y.append("kiwi")
del y[0]
thistuple=tuple(y)
print(thistuple"""
"""tuple=("orange","red","green")
print(tuple[0])
print(tuple[-1])
num=(1,2,4,6,8,145)
largest=max(num)
smallest=min(num)
print(largest)
print(smallest)
print(len(tuple))"""
"""x=(1,3,6,84,90,20,43)
y=list(x)
y.sort()
secondlargest=y[-2]
print(secondlargest)"""
"""x=(1,34,55,67,88,99)
y=list(x)
y.remove(max(y))
secondlargest=max(y)
x=tuple(y)
print(secondlargest)"""


"""tup=()
n=int(input("enter the number"))
lst=list(tup)
for i in range(n):
    user_input=int(input("enter a num"))
    lst.append(user_input)
    if lst[i]%7==0:
        lst[i]="%"
    elif lst[i]%2==0:
        lst[i]="&"
    else:
        list[i]
tup=tuple(lst)
print(tup)"""
"""thisset={5,8,78,56}
thisset.add(7)
thisset.remove(78)
print(thisset)"""
"""set={23,56,78,90}
maximum=max(set)
minimum=min(set)
print(maximum)
print(minimum)
print(len(set))"""
"""thislist=[1,2,1,3,5,76,88]
list=set(thislist)
print(list)"""
"""n=int(input("enter a num"))
sum=0
for i in range(n+1):
     sum+=i
print(sum)"""
"""n=int(input("enter a number"))
i=1
sum=0
while i<=n:
    sum+=i
    i+=1
print(sum)"""
"""string=input("enter a string")
r=""
for x in string:
    r=x+r
print(r)
if string==r:
    print("palindrome")h
else:
    print("not palindrome")"""
"""x=input("enter a string")
t="(){}\:;<>/?\\#*!@$^&~"
r=""
for y in x:
    if y not in t:
      r+=y
print(r)"""
"""import string
n=input("enter a string")
r=""
for x in n:
    if x not in string.punctuation:
        r+=x
print(r)"""
"""n=int(input("enter a number"))
if n<2:
    print("prime number")
for y in range(2,n):
    if n%y==0:
        print(n,"not a prime number")
        break
else:
    print("prime number")"""
"""def car():
    print("ferari")
car()"""
"""def car():
    return("ferari")
print(car())"""
"""def vehicle(car):
    print("welcome",car)
vehicle("ferari")"""
"""def king(saudiarabia):
   print(saudiarabia +"welcome")
king("salman bin muhammed")"""
def marathon(firstrunner):
    return("hello" +" "+firstrunner)
print(marathon("usain bolt"))