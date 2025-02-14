from random import randint
from model.moov import Moov
from model.multiplier import type_multiplier
class Pokemon (Moov): 
    '''Class to create a pokemon'''

    def __init__(self,name,sprite,pkmn_type,attack,defence,moov1,moov2,level = 5,life = 100):
        '''Initialize the pokemon'''
        self.name = name
        self.sprite = sprite
        self.pkmn_type = pkmn_type
        self.level = level
        self.life = life
        self.attack = attack
        self.defence = defence
        Moov.__init__(self,moov1,moov2)
        self.moov_type_2 = pkmn_type
    
    def get_pokemon(self):
        return f"Name: {self.name}, Type: {self.pkmn_type}, Level: {self.level}, Attack: {self.attack}, Defence: {self.defence}, Moov: {self.moov1},' ',{self.moov2}; Life: {self.life}"
    
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
        multi = type_multiplier[(self.pkmn_type, opponent.pkmn_type)]
        damage = (self.attack * self.level * 0.2 - opponent.defence * opponent.level * 0.05) * multi
        opponent.life -= damage
        print(opponent.life)
        # return f"{self.name} has inflicted {damage} damage to {opponent.name}!"
    
    def get_moov_accuracy(self, moov):
        '''Get the accuracy of a moov'''
        match moov:
            case self.moov1:
                return self.accuracy_mouv1
            case self.moov2:
                return self.accuracy_mouv2

    def has_missed(self, moov):
        '''Calculate if the move missed with a random number (0-100).
        
        Gen 1 miss included! (which is 1/100 and not 1/256)'''
        random_nb = randint(0,100)
        accuracy = self.get_moov_accuracy(moov)
        if accuracy < random_nb: #Gen 1 miss if randint=100 when acc = 100!! (intentional)
            return True
        else:
            return False
        # return f"{self.moov1} has an accuracy of {self.accuracy_mouv1} and {self.moov2} has an accuracy of {self.accuracy_mouv2}"

    def attacking(self, opponent, moov):
        if self.has_missed(moov):
            print('Too Bad!')
        else:
            self.attack_damage(opponent)