from project.decoration.base_decoration import BaseDecoration


class Plant(BaseDecoration):
    comfort_value = 5
    price = 10

    def __init__(self):
        super().__init__(self.comfort_value, self.price)
