class Avenger:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def display_info(self):
        print("Name: ", self.name)
        print("Power: ", self.power)

class IronMan(Avenger):
    def show_weapon(self):
        print("Armor Suit")

class Rescue(IronMan):
    def assit(self):
        print(self.name, "is providing backup support")

pepper = Rescue("Recsue", "Tech-enhanced combat")
pepper.display_info()
pepper.show_weapon()
pepper.assist()

tony = IronMan("Iron Man", "Genius")
tony.display_info()
tony.show_weapon()

stark = Avenger("Stark")