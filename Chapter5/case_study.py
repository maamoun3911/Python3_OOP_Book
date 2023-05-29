class Character:
    def __init__(self, character: str, bold=False, italic=False, underline=False) -> None:
        
        assert len(character) == 1
        
        self.character = character
        self.bold, self.italic, self.underline = bold, italic, underline
    
    def __str__(self):
        bold = "*" if self.bold else ""
        italic = "/" if self.italic else ""
        underline = "_" if self.underline else ""
        return bold+italic+underline+self.character


class Cursor:
    def __init__(self, documet) -> None:
        self.document = documet
        self.position = 0
    
    def forward(self):
        self.position += 1
        
    def back(self):
        self.position -= 1
    
    def home(self):
        while self.document.characters[self.position-1].character != "\n":
            self.position -= 1
            if self.position == 0:
                # Go to begging of file before newlines
                break
    
    def end(self):
        while self.position < len(self.document.characters) and \
            self.document.characters[self.position].character != "\n":
            self.position += 1


class Document:
    def __init__(self) -> None:
        self.characters: list[str] = []
        self.cursor: Cursor = Cursor(self)
        self.filename: str = ""
    
    def insert(self, character: Character | str):
        if not hasattr(character, "character"):
            character = Character(character)
        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()
    
    def delete(self):
        del self.characters[self.cursor.position]
        # self.cursor -= 1
    
    def save(self):
        f = open(self.filename, "w")
        f.write("".join(str(c) for c in self.characters))
        f.close()

    @property
    def string(self):
        return "".join("".join(str(c) for c in self.characters))


d = Document()
d.insert("h")
d.insert(Character("e"))
d.insert("l")
d.insert("l")
d.insert("o")
d.cursor.back()
d.cursor.back()
d.cursor.home()
print(d.cursor.position)
# d.insert("l")
# d.insert("o")
# d.insert("\n")
# d.insert("w")
# d.insert("o")
# d.insert("r")
# d.insert("l")
# d.insert("d")
# d.insert("*")
print(d.string)