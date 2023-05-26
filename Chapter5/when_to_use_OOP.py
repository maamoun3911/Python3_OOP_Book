# class Color:
#     def __init__(self, rgb_value, name):
#         self.rgb_value = rgb_value
#         self._name = name
#     def _set_name(self, name):
#         if not name:
#             raise Exception("Invalid Name")
#         self._name = name
#     def _get_name(self):
#         return self._name

#     name = property(_get_name, _set_name)

# c = Color("#ff0000", "red")
# print(c.name)
# c.name = "Bright red"
# print(c.name)

# class WebPage:
#     def __init__(self, url):
#         self.url = url
#         self._content = None
#     @property
#     def content(self):
#         if not self._content:
#             print("mrror")
#             self._content = f"urlopen({self.url}).read()"
#         return self._content

# webpage = WebPage("Facebook.com")
# content1 = webpage.content
# print(content1)
# content2 = webpage.content
# print(content2)

# class IntegersList(list):
#     @property
#     def average(self) -> float:
#         return sum(self) / len(self)

# average_list = IntegersList([1, 2, 3])
# print(average_list.average)

# 1] without DRY

# import sys
# import os
# import shutil
# import zipfile

# class ZipReplace:
#     def __init__(self, filename, search_string, replace_string):
#         self.filename = filename
#         self.search_string = search_string
#         self.replace_string = replace_string
#         self.temp_directory = f"unzipped-{filename}"
    
#     def _full_filename(self, filename):
#         return os.path.join(self.temp_directory, filename)
    
#     def zip_find_replace(self):
#         self.unzip_files()
#         self.find_replace()
#         self.zip_files()
    
#     def unzip_files(self):
#         os.mkdir(self.temp_directory)
#         zip = zipfile.ZipFile(self.filename)
#         try:
#             zip.extractall(self.temp_directory)
#         finally:
#             zip.close()
    
#     def find_replace(self):
#         for filename in os.listdir(self.temp_directory):
#             with open(self._full_filename(filename)) as file:
#                 contents = file.read()
#                 contents = contents.replace(self.search_string, self.replace_string)
#                 with open(self._full_filename(filename), "w") as file:
#                     file.write(contents)
    
#     def zip_files(self):
#         file = zipfile.ZipFile(self.filename, 'w')
#         for filename in os.listdir(self.temp_directory):
#             file.write(self._full_filename(filename), filename)
#             shutil.rmtree(self.temp_directory)
    
# if __name__ == "__main__":
#     ZipReplace(*sys.argv[1:4]).zip_find_replace()

# # 2] With DRY and Inheritance

# class ZipProcessor:
#     def __init__(self, zipname):
#         self.zipname = zipname
#         self.temp_directory = f"unzipped-{zipname[:-4]}"
    
#     def _full_filename(self, filename):
#         return os.path.join(self.temp_directory, filename)
    
#     def process_zip(self):
#         self.unzip_files()
#         self.process_files()
#         self.zip_files()
    
#     def unzip_files(self):
#         os.mkdir(self.temp_directory)
#         zip = zipfile.ZipFile(self.zipname)
#         try:
#             zip.extractall(self.temp_directory)
#         finally:
#             zip.close()
    
#     def zip_files(self):
#         file = zipfile.ZipFile(self.zipname, 'w')
#         for filename in os.listdir(self.temp_directory):
#             file.write(self._full_filename(filename), filename)
#             shutil.rmtree(self.temp_directory)

# class ZipReplace(ZipProcessor):
#     def __init__(self, filename, search_string, replace_string):
#         super().__init__(filename)
#         self.search_string = search_string
#         self.replace_string = replace_string
    
#     def process_files(self):
#         '''perform a search and replace on all files
#         in the temporary directory'''
#         for filename in os.listdir(self.temp_directory):
#             with open(self._full_filename(filename)) as file:
#                 contents = file.read()
#                 contents = contents.replace(
#                 self.search_string, self.replace_string)
#                 with open(
#                 self._full_filename(filename), "w") as file:
#                     file.write(contents)
    
# if __name__ == "__main__":
#     ZipReplace(*sys.argv[1:4]).process_zip()
    
# from pygame import image
# from pygame.transform import scale

# class ScaleZip(ZipProcessor):
#     def process_files(self):
#         '''Scale each image in the directory to 640x480'''
#         for filename in os.listdir(self.temp_directory):
#             im = image.load(self._full_filename(filename))
#             scaled = scale(im, (640,480))
#             image.save(scaled, self._full_filename(filename))

# if __name__ == "__main__":
#     ScaleZip(*sys.argv[1:4]).process_zip()

# composition example
#


    
    
class Square:
    def __init__(self, length) -> None:
        self.length = length
        
    def area(self, rectangle):
        print(rectangle.width_length)
        return rectangle.length*rectangle.width

class Rectangle:
    def __init__(self, length, width, square: Square) -> None:
        self.length = length
        self.width = width
        self.square = square
        
    def area(self):
        return self.square.area(self)
    
    @property
    def width_length(self):
        return f"{self.length}-{self.width}"
# square = Square(5)
# rectangle = Rectangle(5, 4, square)
# print(rectangle.area())

class Area:
    def __init__(self) -> None:
        pass
    
    def find_area(self, object):
        return object.length * object.width

class Rectangle:
    def __init__(self, length, width, area_obj: Area) -> None:
        self.length, self.width = length, width
        self.area_obj = area_obj
    
    def area(self):
        return self.area_obj.find_area(self)

class Square:
    def __init__(self, length, width, area_obj: Area) -> None:
        self.length, self.width = length, width
        self.area_obj = area_obj
    
    def area(self):
        return self.area_obj.find_area(self)

area = Area()
rectangle = Rectangle(5, 4, area)
print(rectangle.area())
square = Square(5, 5, area)
print(square.area())