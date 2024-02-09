class parent:
    def m(self):
        print("In parent")


class child:
    def m(self):
        print("In Child")


# class child(parent):
#     def m(self):
#         print("parent")


class Child(child, parent):
    pass


obj = child()
obj.m()
