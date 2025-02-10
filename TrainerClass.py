from JsonClass import Json

# Character-related classes
class Trainers(Json):
    def __init__(self, name):
        self.name = name
        #self.image = image
        self.victory = False
        self.pokedex = [] 
        self.stats = []
    
    def first_pokemon(self, pokemon):
        self.pokedex.append(pokemon)
        self.save()
        self.load()

    def add_pokemon(self, pokemon):
        self.pokedex.append(pokemon)
        
    def remove_pokemon(self, pokemon):
        self.pokedex.remove(pokemon)

# class Monsters:
#     def __init__(self, name, move_list, hp):
#         pass # image = f"{name}.jpg
#     pass

# class Moves:
#     def __init__(self, name, attribute, effect ):
#         pass # sound = f"{sound}.jpg
#     pass

# Gameplay-related classes
# class Graphics:
#     def __init__(self):
#         pass

# class Games:
#     def __init__(self, number, player):
#         pass
#     pass

# class Attributes:
#     def __init__(self):
#         pass
    # pass