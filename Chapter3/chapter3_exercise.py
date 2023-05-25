class Rectangle:
    def __init__(self, length: int, width: int, **kwargs) -> None:
        self.length, self.width = length, width
        super().__init__(**kwargs)
    
    def area(self) -> int:
        return self.width * self.length
    
    def perimeter(self) -> int:
        return 2 * (self.width+self.length)
    

class Square(Rectangle):
    def __init__(self, length: int, **kwargs) -> None:
        super().__init__(length=length, width=length, **kwargs)

class Triangle:
    def __init__(self, triangle_length: int, **kwargs) -> None:
        self.triangle_length = triangle_length
        super().__init__(**kwargs)
    
    def triangle_area(self, height: int) -> int:
        self.height = height
        return int(0.5*self.triangle_length*self.height)
    
    def triangle_perimeter(self) -> int:
        return 3*self.length


class Pyramid(Square, Triangle):
    def __init__(self, triangle_length: int, length: int, **kwargs) -> None:
        super().__init__(triangle_length=triangle_length, length=length, **kwargs)
    
    def pyramid_area(self, pyramid_height: int) -> int:
        self.base = super().area()
        return int(0.5*pyramid_height*self.base)

    def pyramid_perimeter(self, triangle_height: int) -> int:
        base_perimeter = super().area()
        side_perimeter = 4 * super().triangle_area(height=triangle_height)
        return side_perimeter+base_perimeter


pr = Pyramid(6, 4)
print(pr.pyramid_area(8))
print(pr.pyramid_perimeter(7))
