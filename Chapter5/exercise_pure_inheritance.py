class DeskTop:
    def __init__(self, *specifications: tuple[bool, str]) -> None:
        self.specifications = specifications # (portable, electricity, performance)
        self.purposes = []
    
    def add_purpose(self, purpose):
        self.purposes.append(purpose)
        
    def __repr__(self) -> str:
        return f"Prtable: {self.specifications[0]}, Need electricity: {self.specifications[1]}, Performance: {self.specifications[2]}"
    
    
class LapTop(DeskTop):
    def __init__(self, *specifications: tuple[bool, str]) -> None:
        super().__init__(specifications)
        self._charge_percent = 0
    
    def _set_charge(self, quantity: int):
        self._charge_percent += quantity

    def _get_charge(self):
        return f"Your charge is {self._charge_percent}"
    
    charge = property(_get_charge, _set_charge)

desktop = DeskTop(False, True, "High")
laptop = LapTop(True, False, "Medium To High")

desktop.add_purpose("Gaming")
desktop.add_purpose("Programming")
desktop.add_purpose("Surfing")
desktop.add_purpose("Accounting")
print(desktop.purposes)

laptop.add_purpose("Programming")
laptop.add_purpose("podacast listening")
print(laptop.purposes)

laptop.charge = 50
print(laptop.charge)

laptop.charge = 20
print(laptop.charge)