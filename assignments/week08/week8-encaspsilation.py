class Rectangle:
    def __init__(self,length,width):
        self.__length=length
        self.__width=width

    def get_area(self):
        area=self.__length * self.__width   
        return f"area ={area}"
    
    def getPerimeter(self):
        perimeter=2*(self.__length+self.__width)
        print('perimeter = '+perimeter)
    
    def inSquare(self):
        if self.__width==self.__length:
            return True
        else :
            return False
    #main
myrectangle=Rectangle(10,3)
print(myrectangle.get_area())
myrectangle.getPerimeter()
print(myrectangle.inSquare())