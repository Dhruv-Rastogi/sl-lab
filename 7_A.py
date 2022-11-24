class Student: #creating a class
    name = ""
    age = 0
    marks = []
    def __init__(self, name, age): #defining the constructor for the class
        self.name = name
        self.age = age
    def marks(self, mark1, mark2, mark3): #function for taking the marks
        self.marks =[mark1, mark2, mark3]
    def display(self): #function to printing the details of the object
        print("Name of Student is "+self.name)
        print("Age of Student is "+str(self.age))
        print(self.marks)
stud1 = Student("Ramesh", 18) #creating an object
stud1.marks(90,99,98) #taking marks
stud2 = Student("Suresh", 18) # creating another object
stud2.marks(99,98,90)
stud1.display() #calling the display function to print student details
stud2.display()
