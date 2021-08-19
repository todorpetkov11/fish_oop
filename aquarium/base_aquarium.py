from abc import ABC, abstractmethod

from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Aquarium name cannot be an empty string.")
        else:
            self._name = value

    def calculate_comfort(self):
        result = sum([x.comfort for x in self.decorations])
        return result

    def add_fish(self, fish):
        if len(self.fish) >= self.capacity:
            return "Not enough capacity."
        if isinstance(fish, FreshwaterFish) or isinstance(fish, SaltwaterFish):
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result = f"{self.name}:\nFish: "
        if not self.fish:
            result += "none"
        else:
            for fish in self.fish:
                result += f"{fish.name} "
        result += f"\nDecorations: {len(self.decorations)}"
        result += f"\nComfort: {self.calculate_comfort()}\n"
        return result
