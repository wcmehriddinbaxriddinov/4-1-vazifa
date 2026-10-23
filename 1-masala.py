class Athlete:
    def __init__(self, ism, tur, yosh):
        self.ism = ism
        self.tur = tur
        self.yosh = yosh

    def show_info(self):
        print(
            f"Ism: {self.ism}\n"
            f"Sport turi: {self.tur}\n" \
            f"Yosh: {self.yosh}"
        )


athlate1 = Athlete("Ali", "Futbol", 20) 

athlate1.show_info()