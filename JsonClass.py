import json

class Json:
    def save_json(self, object_list):
        json_object = json.dumps(object_list, default=lambda o: o.__dict__, indent = 4, sort_keys = True, separators=(',', ': '))
        with open("pokedex.json", "w") as pokedex:
            json.dump(json_object, pokedex)

    def load_json(self):
        with open("pokedex.json", "r") as pokedex:
            return json.load(pokedex)