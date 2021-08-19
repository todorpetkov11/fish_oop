from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    valid_types_fish = ["FreshwaterFish", "SaltwaterFish"]
    valid_types_aquariums = ["FreshwaterAquarium", "SaltwaterAquarium"]
    valid_types_decoration = ["Ornament", "Plant"]

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type == self.valid_types_aquariums[0]:
            self.aquariums.append(FreshwaterAquarium(aquarium_name))
            return f"Successfully added {aquarium_type}."
        elif aquarium_type == self.valid_types_aquariums[1]:
            self.aquariums.append(SaltwaterAquarium(aquarium_name))
            return f"Successfully added {aquarium_type}."
        else:
            return "Invalid aquarium type."

    def add_decoration(self, decoration_type: str):
        if decoration_type == self.valid_types_decoration[0]:
            self.decorations_repository.add(Ornament())
            return f"Successfully added {decoration_type}."
        elif decoration_type == self.valid_types_decoration[1]:
            self.decorations_repository.add(Plant())
            return f"Successfully added {decoration_type}."
        else:
            return "Invalid decoration type."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration_to_add = self._find_object(decoration_type, self.decorations_repository.decorations)
        aquarium_to_decorate = self._find_object(aquarium_name, self.aquariums)
        if decoration_to_add and aquarium_to_decorate:
            aquarium_to_decorate.add_decoration(decoration_to_add)
            self.decorations_repository.remove(decoration_to_add)
            return f"Successfully added {decoration_type} to {aquarium_name}."
        else:
            return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type == self.valid_types_fish[0]:
            fish = FreshwaterFish(fish_name, fish_species, price)
        elif fish_type == self.valid_types_fish[1]:
            fish = SaltwaterFish(fish_name, fish_species, price)
        else:
            return f"There isn't a fish of type {fish_type}."
        new_fish_aquarium = self._find_object(aquarium_name, self.aquariums)
        if new_fish_aquarium.type != fish.type:
            return "Water not suitable"
        else:
            return new_fish_aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str):
        aquarium_to_feed = self._find_object(aquarium_name, self.aquariums)
        aquarium_to_feed.feed()
        return f"Fish fed: {len(aquarium_to_feed.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium_to_calc = self._find_object(aquarium_name, self.aquariums)
        result = sum([decoration.price for decoration in aquarium_to_calc.decorations])
        result += sum([fish.price for fish in aquarium_to_calc.fish])
        return f"The value of Aquarium {aquarium_to_calc.name} is {result:.2f}."

    def report(self):
        result = ''
        for aquarium in self.aquariums:
            result += str(aquarium)
        return result

    @staticmethod
    def _find_object(obj_name, obj_list):
        for obj in obj_list:
            if obj_name == obj.name:
                return obj
            elif obj_name == obj.__class__.__name__:
                return obj
            else:
                return None


control = Controller()
print(control.add_aquarium("SaltwaterAquarium", 'FWAQ'))
print(control.add_aquarium("FreshwaterAquarium", 'bb'))
print(control.add_decoration("Plant"))
print(control.add_decoration("Ornament"))
print(control.add_fish("bb", "SaaaltwaterFish", "big d", "tuna", 10.5))
print(control.insert_decoration("FWAQ", "Plant"))
print(control.insert_decoration("fwaq", "Ornament"))

print(control.feed_fish("FWAQ"))
print(control.calculate_value("SWAQ"))
print(control.report())
