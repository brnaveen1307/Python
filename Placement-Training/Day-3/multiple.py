class Naveen:
    def intro(self):
        print("Naveen: Photographer")

class Superman:
    def powers(self):
        print("Superman: Cosmic powers")

class Hero(Naveen, Superman):
    def reveal_identity(self):
        print("Naveen = Superman")

character = Hero()
character.intro()
character.powers()