import json
# from objdict import ObjDict 

# TODO Have to use a class to create an object then a dict then on Json then on dict then on object
# TODO Need to have a formated JSON on multiple lines


class Json:
    def save_json(self, object_list, filename):
        """ To write changes in the JSON"""
        try:
            with open(filename + ".json", "w") as file:
                json.dump(object_list, file, default=lambda o: o.__dict__, indent=4)
        except Exception:
            print("Couldn't save JSON data!")

    def load_json(self, filename):
        """ To load JSON to display it(for the pokedex). Return a LIST that contain DICT!"""
        try:
            with open(filename + ".json", "r") as file:
                return json.load(file)
        except Exception:
            print("Couldn't load JSON data!")