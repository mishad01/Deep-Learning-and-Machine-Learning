class studet :
    roll = ""
    gpa = ""

#Object
kamal = studet()
kamal.roll = 10
kamal.gpa = 3.5

print(f"Roll = {kamal.roll}, Gpa = {kamal.gpa}")

#Method -> Function Inside class is method
class studet:
    def self_value(self,a,b): #we use self to indicate it's a method of class
        self.roll = a
        self.gpa = b

    def display(self):
        print(f"Roll = {self.roll}, Gpa = {self.gpa}")

kamal = studet()
kamal.self_value(22100,3.78)
kamal.display()

#Constructor -> Assigning value inside class
class student:
    def __init__(self):
        self.section = "A"
    def display(self):
        print(f"Section = {self.section}")

kamal = student()
kamal.display()

#Pararneterized Constructors - > Parameter in class
class student:
    def __init__(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa
    def display(self):
        print(f"Roll = {self.roll}, Gpa = {self.gpa}")

kamal = student(10,3.75)
kamal.display()

#Pass Statement-> If we want to declare method or others later we use this
class person:
    pass #if we use this , we can skip this class and write code for it later
class student:
    def display(self):
        print("Test")

#Inheritance
class person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname,self.lastname)

class Student(person):
    pass

mishad = Student("Sakif ", "Rahman")
mishad.printname()

#Single Inheritance #Multiple Inheritance

class A :
    def displayl(self):
        print("This is class A")

class B(A):
    def display2(self):
        print("This is class B")

class C(B):
    def display3(self):
        print("This is class C")

objB = C()
objB.displayl()
objB.display2()
objB.display3()

#Hierarchical Inheritance
class Parent: # Base class
  def func1(self):
   print("This function is in parent class.")
class Childl(Parent): # Derived classl
  def func2(self):
    print("This function is in child 1.0")
class Child2(Parent): # Derivied class2
 def func3(self):
  print("This function is in child 2.1")
# Driver's code
objectl = Childl()
object2 = Child2()
objectl.func1()
objectl.func2()
object2.func1()
object2.func3()

#Polyrnorphism
def add(x,y,z = 0):
    return  x+y+z;

print(add(30,20))
print(add(10,20,30))

