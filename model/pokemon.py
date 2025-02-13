from model.moove import Moove
class Pokemon (Moove): 
    '''Class to create a pokemon'''

    def __init__(self,name,sprite,pkmn_type,attack,defence,moove1,moove2,level = 5,life = 100):
        '''Initialize the pokemon'''
        self.name = name
        self.sprite = sprite
        self.pkmn_type = pkmn_type
        self.level = level
        self.life = life
        self.attack = attack
        self.defence = defence
        Moove.__init__(self,moove1,moove2)
        self.moove_type_2 = pkmn_type
    
    def get_pokemon(self):
        return f"Name: {self.name}, Type: {self.pkmn_type}, Level: {self.level}, Attack: {self.attack}, Defence: {self.defence}, Moove: {self.moov1},' ',{self.moov2}; Life: {self.life}"
    
    def level_up(self):
        '''Level up the pokemon'''
        self.level += 1
        self.attack += 5
        self.defence += 5
        return f"{self.name} is now level {self.level}"
    
    def evolve(self,new_name,new_pkmn_type,new_sprite):
        '''Evolve the pokemon'''
        temp_str = self.name
        self.name = new_name
        self.pkmn_type = new_pkmn_type
        self.sprite = new_sprite
        return f"{temp_str} has evolved into {new_name}!"
    
    def attack_damage(self,opponent):
        '''Calculate the damage of an attack'''
        damage = self.attack * self.level * 0.2 - opponent.defence * opponent.level * 0.05
        opponent.life -= damage
        return f"{self.name} has inflicted {damage} damage to {opponent.name}!"
    
    def get_moove_accuracy(self):
        '''Get the accuracy of a moove'''
        return f"{self.moov1} has an accuracy of {self.accuracy_mouv1} and {self.moov2} has an accuracy of {self.accuracy_mouv2}"

