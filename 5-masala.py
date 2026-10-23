class Player:
    def __init__(self, name, energy=100):
        self.name = name
        self.energy = energy

    def use_energy(self, amount):
        self.energy -= amount
        if self.energy < 0:
            self.energy = 0

    def show_status(self):
        print(f"O‘yinchi: {self.name}")
        print(f"Energiya: {self.energy}")


player = Player('Hero')
player.use_energy(35)
player.show_status()