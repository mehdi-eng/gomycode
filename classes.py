#Point3D Class:

class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def get_coordinates(self):
        return (self.x, self.y, self.z)

my_point = Point3D(1, 2, 3)
print(my_point.get_coordinates())  # Output: (1, 2, 3)
##################################################################
#Rectangle Class:

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

my_rectangle = Rectangle(length=4, width=3)
print("Area:", my_rectangle.area())  # Output: Area: 12
print("Perimeter:", my_rectangle.perimeter())  # Output: Perimeter: 14
##################################################################
#Circle Class:

import math

class Circle:
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def is_inside(self, x, y):
        distance = math.sqrt((x - self.center_x) ** 2 + (y - self.center_y) ** 2)
        return distance <= self.radius

my_circle = Circle(center_x=0, center_y=0, radius=5)
print("Area:", my_circle.area())  # Output: Area: 78.53981633974483
print("Perimeter:", my_circle.perimeter())  # Output: Perimeter: 31.41592653589793
print("Is Inside (2, 3):", my_circle.is_inside(2, 3))  # Output: Is Inside (2, 3): True
print("Is Inside (6, 6):", my_circle.is_inside(6, 6))  # Output: Is Inside (6, 6): False
##################################################################
#Bank Class:

class Bank:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

my_account = Bank(balance=1000)
print("Initial Balance:", my_account.balance)  # Output: Initial Balance: 1000
my_account.deposit(500)
print("Balance after Deposit:", my_account.balance)  # Output: Balance after Deposit: 1500
my_account.withdraw(200)
print("Balance after Withdrawal:", my_account.balance)  # Output: Balance after Withdrawal: 1300
my_account.withdraw(1500)  # Output: Insufficient balance
