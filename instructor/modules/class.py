
# with arguement
# class Myclass:
#     name = "mangesh"

#     def __init__(self,mangesh):
#        self.name =name

# def Myclass(self):
#     return self.name

#     obj = Myclass("mangesh")
#     obj.name="mangesh"
#     obj.myname(mangesh)


# # without arguement
# class Myclass:
#     name = "mangesh"

#     def __init__(self):
#        self.name =name

# def Myclass(self):
#     return self.name

#     obj = Myclass()
#     obj.name="mangesh"
#     obj.myname()
    
class Userinfo:
    def __init__(self,**kwrgs):
        self.name=kwrgs["name"]
        # self.age=kwrgs["age"]

    def userderails(self):
        return self.name
        # return self.age
    
obj=Userinfo(name="mangesh")
# obj=Userinfo(age="27")
print(obj.userderails())
