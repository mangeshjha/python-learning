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
        

obj = child()
obj.result()