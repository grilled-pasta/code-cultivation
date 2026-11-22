# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: alkonsta <alkonsta@student.codam.nl>      +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/19 12:25:47 by alkonsta         #+#    #+#              #
#    Updated: 2026/11/22 19:10:05 by alkonsta        ###   ########.nl        #
#                                                                             #
# *************************************************************************** #

class Plant:

    class Statistics():
        def __init__(self) -> None:
            self._calls: dict[str, int] = {
                    "grow": 0,
                    "age": 0,
                    "show": 0
                    }

        def log(self, method: str) -> None:
            if method in self._calls:
                self._calls[method] += 1

        def display(self) -> None:
            print(f"Stats: {self._calls["grow"]} grow" +
                  f", {self._calls["age"]} age" +
                  f", {self._calls["show"]} show")

    def __init__(self, name: str, height: float = 0, age: int = 0,
                 growth_per_day: float = 1.5) -> None:
        self._name: str = name
        self._height: float = 0.0
        self._age: int = 0
        self._growth_per_day: float = growth_per_day
        self._statistics: Plant.Statistics = self.Statistics()

        self.set_height(height)
        self.set_age(age)

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def anonymous(cls) -> Plant:
        return cls("Unknown plant")

    def _is_not_negative(self, attr: str, value: int | float) -> bool:
        if value < 0:
            print(f"{self._name}: Error, {attr} can't be negative")
            return False
        return True

    def get_height(self) -> float:
        return self._height

    def set_height(self, value: float) -> None:
        if self._is_not_negative("height", value):
            self._height = round(value, 1)

    def get_age(self) -> int:
        return self._age

    def set_age(self, value: int) -> None:
        if self._is_not_negative("age", value):
            self._age = value

    def get_statistics(self) -> Plant.Statistics:
        return self._statistics

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")
        self._statistics.log("show")

    def grow(self) -> None:
        self.set_height(self._height + self._growth_per_day)
        self._statistics.log("grow")

    def age(self) -> None:
        self.set_age(self._age + 1)
        self._statistics.log("age")


class Flower(Plant):

    def __init__(self, name: str, height: float = 0, age: int = 0,
                 growth_per_day: float = 1.5, color: str = ""):
        super().__init__(name, height, age, growth_per_day)
        self._color: str = color
        self._bloom: bool = False

    def bloom(self) -> None:
        self._bloom = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._bloom:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")


class Seed(Flower):

    def __init__(self, name: str, height: float = 0, age: int = 0,
                 growth_per_day: float = 1.5, color: str = ""):
        super().__init__(name, height, age, growth_per_day, color)
        self._seeds: int = 0

    def bloom(self, seeds: int = 0) -> None:
        super().bloom()
        self._seeds = seeds

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds}")

    def grow(self, days: int = 1) -> None:
        self.set_height(self._height + self._growth_per_day * days)
        self._statistics.log("grow")

    def age(self, days: int = 1) -> None:
        self.set_age(self._age + days)
        self._statistics.log("age")


class Tree(Plant):

    class Statistics(Plant.Statistics):

        def __init__(self) -> None:
            super().__init__()
            self._calls["shade"] = 0

        def display(self) -> None:
            super().display()
            print(f" {self._calls["shade"]} shade")

    def __init__(self, name: str, height: float = 0, age: int = 0,
                 growth_per_day: float = 0, trunk_diameter: float = 0):
        super().__init__(name, height, age, growth_per_day)
        self._trunk_diameter: float = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of {self._height:.1f}cm"
              + f" long and {self._trunk_diameter:.1f}cm wide.")
        self._statistics.log("shade")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter:.1f}cm")


class Vegetable(Plant):

    def __init__(self, name: str, height: float = 0, age: int = 0,
                 growth_per_day: float = 0, harvest_season: str = "",
                 nutritional_value: int = 0):
        super().__init__(name, height, age)
        self._harvest_season: str = harvest_season
        self._nutritional_value: int = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season.capitalize()}")
        print(f" Nutritional value: {self._nutritional_value}")

    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 1


def display_statistics(plant: Plant) -> None:
    plant.get_statistics().display()


def main() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    print("\n=== Flower")
    flower = Flower("Rose", 15, 10, 8, "red")
    flower.show()
    print(" [statistics for Rose]")
    display_statistics(flower)
    print(" [asking the rose to grow and bloom]")
    flower.grow()
    flower.bloom()
    flower.show()
    print(" [statistics for Rose]")
    display_statistics(flower)

    print("\n=== Tree")
    tree = Tree("Oak", 200, 365, trunk_diameter=5)
    tree.show()
    print(" [statistics for Oak]")
    display_statistics(tree)
    print("[asking the oak to produce shade]")
    tree.produce_shade()
    print(" [statistics for Oak]")
    display_statistics(tree)

    print("\n=== Seed")
    seed = Seed("Sunflower", 80, 45, color="yellow")
    seed.show()
    print("[make sunflower grow, age and bloom]")
    seed.age(20)
    seed.grow(20)
    seed.bloom(42)
    seed.show()
    print(" [statistics for Sunflower]")
    display_statistics(seed)

    print("\n=== Anonymous")
    anonymous = Plant.anonymous()
    anonymous.show()
    print(" [statistics for Unknown plant]")
    display_statistics(anonymous)


if __name__ == "__main__":
    main()
