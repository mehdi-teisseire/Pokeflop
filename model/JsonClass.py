import json, copy

class Json:
    def save_json(self, object_list, filename):
        """ To write changes in the JSON"""
        temp_list = self.create_temp_list(object_list)
       
        try:
            with open("./data/" + filename + ".json", "w") as file:
                json.dump(temp_list, file, default=lambda o: o.__dict__, indent=4)
        except Exception:
            print("Couldn't save JSON data!")

    def load_json(self, filename):
        """ To load JSON to display it(for the pokedex). Return a LIST that contain DICT!"""
        try:
            with open("./data/" + filename + ".json", "r") as file:
                return json.load(file)
        except Exception:
            print("Couldn't load JSON data!")
            return [] 


    def convert_moovs(self, object_list):
        """Convert moovs objects in string to stock in json"""
        moov_list = []
        for object in object_list:
            for moov in object.moov:
                moov_list.append(moov.name)
        return moov_list
    
    def create_temp_list(self, object_list):
        """Create temp list to avoid editing real object (may have another way to not get a reference)"""
        #TODO have to not paste the erference (copy.copy())
        temp_list = []
        for object in object_list:
            temp_list.append(copy.copy(object))
            
        for temp_object in temp_list:
            temp_object.moov = self.convert_moovs(object_list)
        
        return temp_list