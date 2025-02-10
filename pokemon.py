from moove import Moove
class Pokemon (Moove): 
    '''Class to create a pokemon'''

    def __init__(self,name,pkmn_type,attack,defence,sprite,moov1,moov2):
        '''Initialize the pokemon'''
        Moove.__init__(self,moov1,moov2)
        self.name = name
        self.pkmn_type = pkmn_type
        self.level = 5
        self.attack = attack
        self.defence = defence
        self.sprite = sprite
        self.moove_type_2 = pkmn_type
        self.moove_type_1 = 'Normal'
    
    def get_pokemon(self):
        return f"Name: {self.name}, Type: {self.pkmn_type}, Level: {self.level}, Attack: {self.attack}, Defence: {self.defence}, Moove: {self.moov1},' ',{self.moov2};"
    
    def level_up(self):
        '''Level up the pokemon'''
        self.level += 1
        self.attack += 5
        self.defence += 5
        return f"{self.name} is now level {self.level}"
    
    def evolve(self,new_name,new_pkmn_type,new_sprite):
        '''Evolve the pokemon'''
        self.name = new_name
        self.pkmn_type = new_pkmn_type
        self.sprite = new_sprite
        return f"{self.name} has evolved into {new_name}!" # TODO FIX:  self.name display the new name and not the old one 
    
    def attack_damage(self,opponent):
        '''Calculate the damage of an attack'''
        damage = self.attack * self.level * 0.2 - opponent.defence * opponent.level * 0.05
        return f"{self.name} has inflicted {damage} damage to {opponent.name}!"
    
    def get_moove_accuracy(self):
        '''Get the accuracy of a moove'''
        return f"{self.moov1} has an accuracy of {self.accuracy_mouv1} and {self.moov2} has an accuracy of {self.accuracy_mouv2}"

pokemon_template = [
    {'name':'Squirtle','type':'eau','attack':50,'defence':50,'sprite':'sprite.png','moov1':'Charge','moov2':'Watter gun'},
    {'name':'Pikachu','type':'electric','attack':50,'defence':50,'sprite':'sprite.png','moov1':'Charge','moov2':'Thunder'},
    {'name':'Bulbasaur','type':'plante','attack':50,'defence':50,'sprite':'sprite.png','moov1':'Charge','moov2':'Leaf'},
    {'name':'Charmander','type':'fire','attack':50,'defence':50,'sprite':'sprite.png','moov1':'Charge','moov2':'Flamethrower'},
    {'name':'Pidgey','type':'normal','attack':45,'defence':45,'sprite':'sprite.png','moov1':'Tackle','moov2':'Gust'},
    {'name':'Rattata','type':'normal','attack':48,'defence':43,'sprite':'sprite.png','moov1':'Tackle','moov2':'Quick Attack'}
]

player_pokemons = []
trainer_pokemons = []

for pokemon in pokemon_template:
    player_pokemons.append(Pokemon(pokemon['name'],pokemon['type'],pokemon['attack'],pokemon['defence'],pokemon['sprite'],pokemon['moov1'],pokemon['moov2']))
    trainer_pokemons.append(Pokemon(pokemon['name'],pokemon['type'],pokemon['attack'],pokemon['defence'],pokemon['sprite'],pokemon['moov1'],pokemon['moov2']))

print(player_pokemons[2].get_pokemon())
print(player_pokemons[2].level_up())
print(player_pokemons[2].attack_damage(trainer_pokemons[3]))
print(player_pokemons[2].get_moove_accuracy())
print(player_pokemons[2].evolve('Ivysaur','plante','sprite.png'))
print(player_pokemons[2].get_pokemon())