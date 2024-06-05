'''class User:

    def __init__(self, name: str):
        """Added the name parameter."""
        self.name = name

    def simple_method(self):
        """Example of a simple method."""
        self.name.capitalize()

    def __repr__(self):
        return f'User({self.name})'


user = User('Спенглер')
print(user)'''


# =========================================================

class User:

    def __init__(self, name: str, equipment: list = None):
        self.name = name
        self.equipment = equipment if equipment is not None else []
        self.life = 3

    def __repr__(self):
        return f'User({self.name}, {self.equipment})'


user = User('Венкман', ['протонный ускоритель', 'ловушка'])
print(user)
