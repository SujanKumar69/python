class Mobile:
    def _init_(self,brand,ram,battery):
        self.brand=brand
        self.ram=ram
        self.battery=battery
    def display(self):
        print("Brand: ",self.brand)
        print("Ram: ",self.ram)
        print("Battery: ",self.battery)
obj = Mobile("apple","8gb","4000mah")
obj.display()

#single inheritence
class Parent:
    def one(self):
        print("This is parent class ")
class Child:
    def two(Parent):
        print("This is child class ")
obj=Child()
obj.two()
obj.one()

#multilevel
class Parent:
    def one(self):
        print("This is parent class ")
class Child:
    def two(Parent):
        print("This is child class ")
class Grandchild:
    def three(Parent):
        print("This is grandchild class ")
obj=Child()
obj.one()
obj.two()
obj.three()


#METHOD OVERLOADING
#same class
#same function or method names
#different parameters
class A:
    def sum(self,a,b):
        return a+b
class B:
    def sum(self,a,b,c):
        return a+b+c
obj=A()
print(sum(1,2,3))

#METHOD OVERERIDING
#different class
#same function or method names
#different parameters
class A:
    def display(self):
        print("This is class A")
class B(A):
    def dissplay(self):
        print("This is class B")
        super().dispaly() #we use super keyword to overcome method overriding
obj=B()
obj.display()
