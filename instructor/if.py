a = "test"
b = "test"
print(a)

if a==b:
    print("pass")

if a>b:
    print("test pass")
elif (a==b):
    print("eaual pass")
    if isinstance(123,int):
        print("datatype pass")
    elif(a<b):
        print("opeartor pass")
else:
    print("whole program fail")