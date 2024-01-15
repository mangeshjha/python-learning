# # # for x in fruits:
# # #     print(x)

# # # for x in "broadway":
# # #     print("\n",x)

# # # fruits = ["apple", "banana", "cherry"]
# # # for x in fruits:
# # #   print(x)

# # #   if x == "banana":
# # #     break

# # dict_data = {
# #     "name":"sudan",
# #     "age":45
# # }
# # # fruits = ["mango","orange"]
# # # fruits.append("apple")
# # # for items in fruits:
# # #     if items == "orange":
# # #         break
# # #     print(items)

# # fruits = ["apple", "banana", "cherry"]
# # for x in fruits:
# #   if x == "banana":
# #     continue
# # #   print(x)


# # for i in range(1,10,1):
# #     print(i)

# # # 3 X 1 = 3
# # # 3 X 2 = 6
# # # 3 X 1 =3
# # # 3 X 1 =3

# a = [1,3,5,6,9]
# # f_string = f'first value of list is {a[0]} second value of list is {a[1]}'
# # print(f_string)

for items in range(2,100,2):
    print("\n")
    for x in range(1,11):
        print(f'{items} X {x} = {items*x}')
else:
    print("for loop ended")

# user_data = int(input("enter a number for multification"))
# if user_data<5:
#     for items in range(1,user_data+1,1):
#         multi_data = int(input("enter a number==>"))
#         for i in range(1,11,1):
#             print(f'{multi_data} X {i} = {multi_data*i}')
            
# else:
#     print("number should not be greater than 5")