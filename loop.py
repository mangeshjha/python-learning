# loop statement
# for_loop
# examples

# for x = ["mangesh","jha"]
# for x in name:
#     print(x)

# for x in"broadways":
#     print("\n",x)


# dict_data = {
#     "name":mangesh,
#     "age":45
# }

# for x in dict_data:
#     print(dict_data[x])

# fruits=["mango","orange"]
# fruits.append("apple")
# for items in fruits:
#     if items=="orange":
#         break
#     print(items)


# fruits=["mango","orange"]
# fruits.append("apple")
# for items in fruits:
#     print(items)
#     if items=="orange":
#         break


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue

# print(x)


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     continue

# data_types = [ "mangesh",'30',10]
# for x in data_types:
#     if isinstance(x,int):
#         break
# print(x)
#   print(x)
#   if x == "int":
#     break

# for i in range(1,10,1):
#     print(i)

# multiplication_table (3,10,1):
#     for i in range (3,10,1):
#         for j in range (3,10,1):
#             x=i*j
#             print(f"{i}*{j}={x}")


# x=int(input("which number's table you want to generate?"))
# for i in range(3,10,1):
#    multiply = x*1
#    print(f'{x}*{1}={multiply}')

# a=int(input("number of multilication"))
# list_data = []
# if(a>5):
#     for i in range(1,a+1):
#         data = input(enter a number)
#         list_data.append(data)
# else:
#     print("number should not less than 5")

list_data = []
user_data = int(input("enter a number for multiplication"))
if user_data < 5:
    for item in range(1, user_data + 1, 1):
        multi_data = int(input("enter a number ==>"))
        list_data.append(multi_data)

        #
else:
    print("number should not be grater than 5")

for x in list_data:
    print("for loop ended")
    for i in range(1, 11, 1):
        print(f"{x} X {i} = {x*i}")
