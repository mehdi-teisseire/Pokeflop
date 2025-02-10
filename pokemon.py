from moove import Moove
class Pokemon (Moove): 

    def __init__(self,name,pkmn_type,attack,defence,sprite,moov1,moov2):
        Moove.__init__(self,moov1,moov2)
        self.name = name
        self.pkmn_type = pkmn_type
        self.level = 5
        self.attack = attack
        self.defence = defence
        self.sprite = sprite
        self.moove_type_2 = self.pkmn_type
    
    def get_pokemon(self):
        return f"Name: {self.name}, Type: {self.pkmn_type}, Level: {self.level}, Attack: {self.attack}, Defence: {self.defence}, Moove: {self.moov1},' ',{self.moov2};"

carapuce = Pokemon('Carapuce','eau',50,50,'sprite.png','Charge','Watter gun')
print(carapuce.get_pokemon())
