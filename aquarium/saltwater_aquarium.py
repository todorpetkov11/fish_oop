from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    initial_capacity = 25
    type = "Saltwater"

    def __init__(self, name):
        super().__init__(name, self.initial_capacity)
