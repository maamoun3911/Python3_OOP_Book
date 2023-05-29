# composition

from collections import namedtuple

class Character:
    def __init__(self, char: str) -> None:
        self.char = char
        self.word_expression: list[tuple[str, str]] = []

    def _add(self, dicitonary, word: str, expression: str):
        lang = dicitonary.lang
        forma = namedtuple(lang, f"word expression")
        adding_tuple = forma(word, expression)
        self.word_expression.append(adding_tuple)
    
    def _delete(self, word: str) -> str:
        # binary search on words
        index, length = 0, len(self.word_expression)
        while index < length:
            binary = self.word_expression[index]
            if binary[0] == word:
                self.word_expression.pop(index)
                return f"{word} deleted successfully"
            i += 1
        return f"There is no word like {word} in the Dictionary"
    
    def _read(self, word: str):
        # binary search on words
        for binary in self.word_expression:
            if binary[0] == word:
                return binary[1]
        return f"There is no word like '{word}' in the Dictionary"

    def add(self, dictionary, word):
        pass


class Dictionary:
    def __init__(self, lang: str) -> None:
        self.lang = lang
        self.lang_dict: dict[str, Character] = {}
    
    def add(self, word: str, expression: str):
        first_letter: str = word[0]
        char_obj: Character | None = self.lang_dict.get(first_letter)
        if not char_obj:
            char_obj: Character = Character(first_letter)
        char_obj._add(self, word, expression)
        self.lang_dict[first_letter] = char_obj
    
    def delete(self, word: str) -> str:
        first_letter: str = word[0]
        char_obj: Character | None = self.lang_dict.get(first_letter)
        if not char_obj:
            return f"Sorry but your word first letter '{first_letter}' has no section in the Dictionary"
        result = char_obj._delete(word)
        self.lang_dict[first_letter] = char_obj
        return result
    
    def read(self, word: str):
        first_letter = word[0]
        char_obj: Character | None = self.lang_dict.get(first_letter)
        if char_obj:
            return char_obj._read(word)
        return f"Dictionary has no section with character {first_letter}"


eng_dict = Dictionary("Eng")
eng_dict.add("Table", "Some kind of listed content")
eng_dict.add("list", "Some kind of lista")
print(eng_dict.read("list"))
print(eng_dict.delete("list"))
print(eng_dict.read("list"))
print(eng_dict.read("Table"))
print(eng_dict.delete("Table"))
print(eng_dict.read("Table"))
print(eng_dict.delete("panma"))