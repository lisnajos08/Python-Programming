class Rectangle:
    def __init__(self ,breadth, length):
        self.breadth = breadth
        self.length = length
    def area(self):
        return self.breadth * self.length
    def perimeter(self):
        return 2 * (self.breadth + self.length)
print("Rectangle 1")
a=int(input("enter the length:"))
b= int(input("enter the breadth:"))
obj=Rectangle(a,b)

print("Area 1 = ",obj.area())
print("Perimeter = ",obj.perimeter())

print("Rectangle 2")
a=int(input("enter the length:"))
b= int(input("enter the breadth:"))
ob=Rectangle(a,b)

print("Area 2= ",ob.area())
print("Perimeter=",ob.perimeter())

if  obj.area() == ob.area():
    print("The 2 rectangle have same area")
else:
    print("not equal")