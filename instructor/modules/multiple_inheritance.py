class parent:
    def __init__(self):
         self.name = "mangesh"
        

    def testing_name(self):
        return self.name
        

class child:
    def __init__(self):
        self.child_name = "child name"
        
    def testing_name_child(self):
        return self.child_name
        
class Inparent(parent,child):
    def __init__(self):
        child.__init__(self)
        super().__init__()

    def ini(self):
        print(self.testing_name_child()) #child _class
        print(self.testing_name())  #parent _class
        # print(self.child_name())
        return self.child_name  #child _class_return
    
obj = Inparent()
obj.ini()


                