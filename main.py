class Vector():
    
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def __str__(self):
        return f"number =  {self.__x} {self.__y}"

    def __add__(self, other):
        y = self.__y * other.__y
        ch1 = self.__x * other.__y
        ch2 = other.__x * self.__y
        ch3 = ch1 + ch2
        return Vector(ch3, y)

    def __sub__(self, other):
        y = self.__y * other.__y
        ch1 = self.__x * other.__y
        ch2 = other.__x * self.__y
        ch3 = ch1 - ch2
        return Vector(ch3, y)
    
    def __mul__(self, other):
        x = self.__x * other.__x
        y = self.__y * other.__y
        return Vector(x, y)
    
    def __truediv__(self, other):
        x = self.__x * other.__y
        y = self.__y * other.__x
        return Vector(x,y)

I = Vector(5, 7)
I2 = Vector(4, 20)
I5 = I.__add__(I2)
print(I5)
I6 = I.__sub__(I2)
print(I6)
I7 = I.__mul__(I2)
print(I7, "Сокращайте сами")
I8 = I.__truediv__(I2)
print(I8, "Сокращайте сами")