

## 装饰器
def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makebold
@makeitalic
def decorators_hello():
    return "hello world"


print(decorators_hello())

from dataclasses import dataclass
@dataclass
class Armor: 
    armor: float 
    description: str 
    level: int = 1
    def power(self) -> float:
        return self.armor * self.level
armor = Armor(5.2, "Common armor.", 2)
armor.power()# 10.4
print(armor)# Armor(armor=5.2, description='Common armor.', level=2)
