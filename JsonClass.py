import json

class Json:
    def save(self, object_list):
        with open("pokedex.json", "w") as pokedex:
            json.dumps(object_list, pokedex)

    def load(self):
        with open("pokedex.json", "r") as pokedex:
            json_format = json.loads(json_format)  
        return json_format