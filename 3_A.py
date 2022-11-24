class Rect: #creating a class
    x=1
    y=1
    def _init_(self,x,y): #defining a constructor for the class to initialize the dimensions
        self.x=x
        self.y=y
    def findArea(self):#function to find area of rectangle
        return self.x*self.y
myRect = Rect()#creating an object
myRect.x =9
myRect.y =91
area=myRect.findArea()#finding the area
print(area)
