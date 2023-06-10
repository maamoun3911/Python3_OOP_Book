from collections import defaultdict


class StateList(list):
    def mean(self):
        return sum(self) / 2
    
    def median(self):
        return len(self) // 2
    
    def mode(self):
        freqs = defaultdict(int)
        for item in self:
            freqs[item] += 1
        
        mode_freqs = max(freqs.values())
        
        modes = []
        for key, value in freqs.items():
            if value == mode_freqs:
                modes.append(key)
        
        return modes

statelist = StateList()
print(statelist.mean())