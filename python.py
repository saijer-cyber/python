"""tup=()
n=int(input("enter a number"))
lst=list(tup)
for i in range(n):
    user_input=int(input("enter a number"))
    lst.append(user_input)
    if lst[i]%7==0:
        lst[i]="%"
    elif lst[i]%2==0:
        lst[i]="$"
    else:
        print(lst[i])
tup=tuple(lst)
print(tup)"""

"""x = input("enter a string: ")
t = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
r = ""

for y in x:
    if y not in t:
        r += y
print(r)"""
"""import string
x=input("enter a string")
r=""
for y in x:
    if y not in string.punctuation:
        r+=y
print(r)"""
"""i=1
sum= 0
while i<=6:
    sum +=i
    i+=1
print(sum)"""
"""a=[1,2,3,4,4,5,6,7]
b=[2,3,4,4,5,6]
i=list(set(a) & set(b))
print(i)"""
"""n=int(input("enter a number"))
print(n**n)"""
"""n=int(input("enter a number"))
f=1
for x in range(1,n+1):
    f*=x
print(f)"""
"""n=int(input("enter a number:"))
if n<2:
    print("prime number")
for y in range(2,n):
    if n%y==0:
         print(n,"not a prime number ")
         break
else:
    print("prime number")"""
"""n=int(input("enter a number"))
f=1
for y in range(1,n+1):
    f*=y
print(f)"""
"""n=int(input("enter a number"))
sum=0
for y in range(1,n+1):
    sum+=y
print(sum)"""
"""n=int(input("enter a num"))
i=1
sum=0
while i<=n:
     sum+=i
     i+=1
print(sum)"""
"""l=[1,2,3,4,5]
b=[3,4,5,6]
i=list(set(l)& set(b))
print(i)"""
"""a=int(input("enter a num"))
b=int(input("enter a num"))
a,b=b,a
print(a,b)"""
"""n=int(input("enter a number"))
a=0
b=1
print("fibonacci series")
for i in range(n):
    print(a,end="")
    c=a+b
    a=b
    b=c"""
"""a=input("enter a string:")
count=0
v="aeiou"
for i in a:
    if i not in v:
        print(i,"constonant")
    else:
        count+=1
print(count)"""
"""n=input("enter a string")
v="aeiouAEIOU"
count=0
for i in n:
    if i in v:
        print(i,end="")
        count+=1
print()
print(count)"""
"""n=input("enter a string")
b=[]
v="aeiouAEIOU"
count=0
for i in n:
    if i in v:
        b.append(i)
        print(i)
print(len(b))"""
"""def farrenheat_to_celsius(fahrenheit):
    return(fahrenheit-32)*5/9
print(farrenheat_to_celsius(77))
print(farrenheat_to_celsius(64))
print(farrenheat_to_celsius(56))"""
"""def man_of_the_match(fastbowler):
    print("hello"+" "+fastbowler)
man_of_the_match("rahul")"""
""" def name(fname,lname):
   print(fname+" "+lname)
name("mohammed","saijer")"""
"""def my_function(animal,name):
    print("I have a",animal)
    print("my",animal,"'s name is",name)
my_function(animal="tiger",name="rocky")"""
"""def my_function(fruits):
    for fruit in fruits:
        print(fruit)
my_fruits=["apple","banana","cherry"]
my_function(my_fruits)"""
"""def my_function(person):
    print("name:",person["name"])
    print("age:",person["age"])
my_person={"name":"rahul","age":"25"}
my_function(my_person)"""
"""def my_function(x,y):
    return x+y
result=my_function(5,3)
print(result)"""
"""def my_function(x,y):
    print(x+y)
my_function(5,3)"""
"""def my_function(x):
    if x%2==0:
        print("even")
    else:
        print("odd")
y=int(input("enter a number"))
my_function(y)"""
"""def my_function(x):
    print(x*x)
y=int(input("enter a num"))
my_function(y)"""
"""def my_function(x):
    return x*x
y=int(input("enter a num:"))
print(my_function(y))"""
"""def my_function(*num):
    sum=0
    for n in num:
        sum+=n
    return sum
print(my_function(1,2,3))
print(my_function(200,5000,69999))
print(my_function(4))"""
"""def my_function(*numbers):
    if len(numbers)==0:
        return None
    max_num=numbers[0]
    for num in numbers:
        if num>max_num:
            max_num=num
    return max_num
print(my_function(3,7,2,8,9,1))"""
"""def my_function(**kid):
    print("his last name "+kid["lname"])
my_function(fname="tobias",lname="refsnus")"""
"""def factorial(n):
    if n==1:
     return n
    else:
       return n*factorial(n-1)
x=int(input("enter a num"))
print(factorial(x))"""
try:
    x=int(input("enter a num"))
    y=int(input("enter a another num"))
    result=x/y
    print(result)
except:
    print("an error occured")
finally:
    print("execution completed")

