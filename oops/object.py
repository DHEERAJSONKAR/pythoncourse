# class student:
#     rollno = 101
#     name = "john"
#     def display(self):
#         print("i am a college student.")
# obj = student()
# print(obj.name)
# print(obj.rollno)
# obj.display()


# class Factory:
#     def __init__(self,material,zips,pokets):
        
#         self.material = material
#         self.zips = zips
#         self.pokets = pokets 
#     def show(self):
#         print(f"material is {self.material} and zips are {self.zips} and pokets are {self.pokets}")
# campus = Factory("leather",5,4)
# hp = Factory("plastic",2,6)
# campus.show()
# hp.show()


class Animal:
    def __init__(self,age):
        self.age= age #instance variable
    
    def show(self): #instance method
        print(f"age of animal is {self.age}")

    @classmethod
    def info(cls):
        print("this is animal class")
    
    @staticmethod
    def static():
        print("animal makes sound")
    
obj = Animal(5)
obj.show()
obj.info()
obj.static()
        