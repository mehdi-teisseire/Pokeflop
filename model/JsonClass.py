import json, copy

class Json:
    def save_json(self, object_list, filename):
        """ To write changes in the JSON"""
        if not isinstance(object_list, dict):
            temp_list = object_list
            with open("./data/" + filename + ".json", "w") as file:
                json.dump(temp_list, file, default=lambda o: o.__dict__, indent=4)
        else:
            temp_list = self.create_temp_list(object_list)
            with open("./data/" + filename + ".json", "w") as file:
                json.dump(temp_list, file, default=lambda o: o.__dict__, indent=4)
         
    def load_json(self, filename):
        """ To load JSON to display it(for the pokedex). Return a LIST that contain DICT!"""
        try:
            with open("./data/" + filename + ".json", "r") as file:
                return json.load(file)
        except Exception:
            print("Couldn't load JSON data!")
            return [] 


    def convert_obj_moovs_to_str(self, object_list):
        """Convert moovs objects in string to stock in json"""
        moov_list = []
        for object in object_list:
            moov_list.append(object.name)
        #     for moov in object.moov:
        #         moov_list.append(moov.name)
        return moov_list
    
    def create_temp_list(self, object_list):
        """Create temp list to avoid editing real object (may have another way to not get a reference)"""
        temp_list = []
        for object in object_list:
            temp_list.append(copy.copy(object))
            
        for temp_object in temp_list:
            # temp_object.moov = self.convert_moovs(object_list)
            temp_object.moov = self.convert_obj_moovs_to_str(temp_object.moov)
        
        return temp_list