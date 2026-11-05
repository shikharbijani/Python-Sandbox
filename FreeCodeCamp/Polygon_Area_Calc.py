class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def set_width(self,n):
        self.width=n

    def set_height(self,n):
        self.height=n

    def get_area(self):
        return self.width *self.height

    def get_perimeter(self):
        return 2*(self.width+self.height)

    def get_diagonal(self):
        return (self.width**2 + self.height**2)**(1/2)

    def get_picture(self):
        picture=""
        if self.height>50 or self.width>50:
            return "Too big for picture."
        for i in range(self.height):
            picture+="*"*self.width+"\n"
        return picture

    def get_amount_inside(self,shape):
        return int(self.width/shape.width)*int(self.height/shape.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self,side):
        self.height=side
        self.width=side

    def set_width(self,n):
        self.width=n
        self.height=n

    def set_height(self,n):
        self.width=n
        self.height=n

    def set_side(self,n):
        self.width=n
        self.height=n

    def __str__(self):
        return f"Square(side={self.height})"



