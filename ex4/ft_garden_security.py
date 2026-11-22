#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_garden_security.py                             :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: alkonsta <alkonsta@student.codam.nl>      +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/17 07:52:27 by alkonsta         #+#    #+#              #
#    Updated: 2026/11/17 07:52:27 by alkonsta        ###   ########.nl        #
#                                                                             #
# *************************************************************************** #

class Plant():

    def __init__(self, name: str, height: float, age: int,
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


def main() -> None:
    print("=== Garden Security System ===")
    plant = Plant("Rose", 15, 10)
    if plant:
        print("Plant created: ", end="")
        plant.show()
    print()
    plant.set_height(25.0)
    if plant.get_height() == 25:
        print("Height updated: 25cm")
    plant.set_age(30)
    if plant.get_age() == 30:
        print("Age updated: 30 days")
    print()
    plant.set_height(-1)
    if plant.get_height() != -1:
        print("Height update rejected")
    plant.set_age(-1)
    if plant.get_age() != -1:
        print("Age update rejected")
    print()
    print("Current state: ", end="")
    plant.show()


if __name__ == "__main__":
    main()
