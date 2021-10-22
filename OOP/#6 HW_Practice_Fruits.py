from abc import abstractmethod


class GardenMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Garden(metaclass=GardenMeta):
    def __init__(self, gardener, fruits, fruit_insects):
        self.gardener = gardener
        self.fruits = fruits
        self.fruit_insects = fruit_insects

    def show_the_garden(self):
        print(f'I am gardener - {self.gardener}')
        print(f'There are {len(self.fruits)} apples in the garden.')
        print(f'There are {self.fruit_insects.pests_quantity} fruit insects in the garden!!!')

class Fruits:
    def __init__(self, fruits_type):
        self.fruits_type = fruits_type

    states = {0: "None", 1: "Flowering", 2: "Green", 3: "Red"}

    @abstractmethod
    def growth(self):
        raise NotImplementedError('You missed me.')

    @abstractmethod
    def is_ripe(self):
        raise NotImplementedError("You missed me")


class Apple(Fruits):
    def __init__(self, fruits_type, number_of_apples):
        Fruits.__init__(self, fruits_type)
        self.number_of_apples = number_of_apples
        self.states = 0

    def growth(self):
        if self.states < 3:
            self.states += 1
        self.print_state()

    def is_ripe(self):
        return self.states == 3

    def eatable(self):
        return self.states == 3 or self.states == 2

    def print_state(self):
        print(f"{self.fruits_type}, {self.number_of_apples} , {self.states}")


class AppleTree:
    def __init__(self, number_of_apples):
        self.apples = [Apple('White', index) for index in range(0, number_of_apples)]

    def count_of_apples(self):
        return len(self.apples)

    def growth_all(self):
        for apple in self.apples:
            apple.growth()

    def all_are_ripe(self):
        return all([apple.is_ripe() for apple in self.apples])

    def give_away_all(self):
        self.apples = []

    def insects_attack(self, pests):
        print('Insects attack!')
        for _ in range(pests.pests_quantity):
            for apple in self.apples:
                index = self.apples.index(apple)
                if apple.eatable():
                    self.apples.pop(index)
                    break


class Pests:
    def __init__(self, pests_type, pests_quantity):
        self.pests_type = pests_type
        self.pests_quantity = pests_quantity

    def kill(self):
        self.pests_quantity = 0


class Gardener:
    def __init__(self, name, plants):
        self.name = name
        self.plants = plants

    def work(self):
        for plant in self.plants:
            plant.growth_all()

    def harvest(self):
        for plant in self.plants:
            if plant.all_are_ripe():
                plant.give_away_all()
            else:
                print('Too early to harvest')

    @staticmethod
    def poison_fruit_pests(insects):
        if insects.pests_quantity > 0:
            insects.kill()
            print('All fruit insects are killed!')
        else:
            print('There are no fruit insects in the garden! You can have a rest!')


apple_tree = AppleTree(6)
fruit_pests = Pests('worm', 4)

tom = Gardener('Tom', [apple_tree])
# tom = Gardener('Tom', [tomato_bush, apple_tree])

garden = Garden(fruits=apple_tree.apples, gardener=tom.name, fruit_insects=fruit_pests)
garden.show_the_garden()

# garden = Garden(tomato_bush, apple_tree)

tom.work()
tom.work()
tom.work()

garden.show_the_garden()
apple_tree.insects_attack(fruit_pests)
garden.show_the_garden()

# Gardener.poison_fruit_pests(fruit_pests)
tom.poison_fruit_pests(fruit_pests)
garden.show_the_garden()

tom.harvest()
print(apple_tree.apples)
