from typing import Any


class AdaptedList(list):
    def pop(self, __index = 0) -> Any:
        return super().pop(__index)
    
    def remove(self, __value: Any) -> None:
        try:
            return super().remove(__value)
        except ValueError:
            return super().remove(self.index(__value))
    
    def append(self, __object: Any) -> None:
        return super().insert(0, __object)
    
    def insert(self, __object: Any,  __index= -1) -> None:
        return super().insert(__index, __object)    


adaptedlist = AdaptedList(range(10))
adaptedlist.append("a")
print(adaptedlist)
adaptedlist.remove("a")
print(adaptedlist)
adaptedlist.insert("a")
print(adaptedlist)

############################################################################################

class KeyValue:
    def __init__(self, key: str, value: int) -> None:
        self.key, self.value = key, value
        
    def __lt__(self, object) -> bool:
        return self.key < object.key
    
    def __repr__(self) -> str:
        return f"object key: {self.key}, object value: {self.value}"

kv = KeyValue("one", 1)
kv1 = KeyValue("two", 2)

a = [kv, kv1]
a.sort()
print(a)