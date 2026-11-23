#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_plant_types.py                                 :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: alkonsta <alkonsta@student.codam.nl>      +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/19 11:42:26 by alkonsta         #+#    #+#              #
#    Updated: 2026/11/19 11:42:26 by alkonsta        ###   ########.nl        #
#                                                                             #
# *************************************************************************** #

class Plant:

    def __init__(self, name: str, height: float = 0, age: int = 0,
                 growth_per_day: float = 1.5) -> None:
        self._name: str = name
        self._height: float = 0.0
        self._age: int = 0
        self._growth_per_day: float = growth_per_day

        self.set_height(height)
        self.set_age(age)

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

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        self.set_height(self._height + self._growth_per_day)

    def age(self) -> None:
        self.set_age(self._age + 1)


class Flower(Plant):

    def __init__(self, name: str, height: float = 0, age: int = 0,
                 growth_per_day: float = 0.8, color: str = ""):
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


class Tree(Plant):

    def __init__(self, name: str, height: float = 0, age: int = 0,
                 growth_per_day: float = 1.5,
                 trunk_diameter: int = 0):
        super().__init__(name, height, age, growth_per_day)
        self._trunk_diameter: int = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of" +
              f" {self._height:.1f}cm long" +
              f" and {self._trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter:.1f}cm")


class Vegetable(Plant):

    def __init__(self, name: str, height: float = 0, age: int = 0,
                 growth_per_day: float = 1.5, harvest_season: str = "",
                 nutritional_value: float = 0):
        super().__init__(name, height, age, growth_per_day)
        self._harvest_season: str = harvest_season
        self._nutritional_value: float = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season.capitalize()}")
        print(f" Nutritional value: {self._nutritional_value:.0f}")

    def grow(self, nutritional_value: float = 0.5) -> None:
        super().grow()
        self._nutritional_value += nutritional_value

    def age(self, nutritional_value: float = 0.5) -> None:
        super().age()
        self._nutritional_value += nutritional_value


def main() -> None:
    print("=== Garden Plant Types ===")

    print("=== Flower")
    flower = Flower("Rose", 15, 10, color="red")
    flower.show()
    print("[asking the rose to bloom]")
    flower.bloom()
    flower.show()

    print("\n=== Tree")
    tree = Tree("Oak", 200, 365, trunk_diameter=5)
    tree.show()
    print("[asking the oak to produce shade]")
    tree.produce_shade()

    print("\n=== Vegetable")
    vegetable = Vegetable("Tomato", 5, 10, 2.1, "april")
    vegetable.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        vegetable.age()
        vegetable.grow()
    vegetable.show()


if __name__ == "__main__":
    main()
