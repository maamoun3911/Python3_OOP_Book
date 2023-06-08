# Case 01: main behavior of class
from urllib.request import urlopen
import json

class Settings:
    def __init__(self, url) -> None:
        with urlopen(url) as content:
            self.config = json.load(content)
        
    def __call__(self, value):
        return self.config[value]
    
webpage = Settings("Facebook.com")
print(webpage("db"))


# avoid if-statement;
# use OOP advantage with function syntax;
# when it is hard to name a main behavior of a class;
# implement clear interface for APIs.