# five input from user and store in list 
# and print each index value using f string command 
# also input the user info and store in dict


a1= input("enter a number")
a2= input("enter a number")
a3= input("enter a number")
a4= input("enter a number")
a5= input("enter a number")
a = []
a.append(a1)
a.append(a2)

result = f'first number {a[0]} 2nd number {a[1]}'
data_a = "broadway"
data_b = "test"

data_dict = {}
data_dict['name']=data_a
data_dict['name2']=data_a

a.append(data_dict)
print("result", a)

