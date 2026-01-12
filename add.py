"""try:
 a=int(input("Enter a Number"))
 b=int(input("Enter a Number"))
 result=a/b
except ZeroDivisionError:
 print("error:division by zero is not allowed")
except ValueError:
 print("error:invalid input,please enter numeric values")
else:
 print(result)
finally:
 print("exuction completed")"""
try:
    num=[20,40,30,70]
    x=int(input("enter a index"))
    print("element at index",num[x])
except ValueError:
    print("value error:please enter integer value")
except IndexError:
    print("index error:index out of range")
except KeyboardInterrupt:
    print("keyboard interrupt:program interrupted by user")
except Exception as e:
    print("unexpected error",e)
finally:
    print("execution completed")


