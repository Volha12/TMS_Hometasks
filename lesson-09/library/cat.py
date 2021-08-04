from library.animal import Animal


class Cat(Animal):

    def bark(self):
        print(f"{self.name} is meowing")
