# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    plant.py                                          :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: alkonsta <alkonsta@student.codam.nl>      +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/17 02:41:13 by alkonsta         #+#    #+#              #
#    Updated: 2026/11/19 16:18:33 by alkonsta        ###   ########.nl        #
#                                                                             #
# *************************************************************************** #

class Plant():

    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float = 1.5) -> None:
        self._name: str = name
        self._height: float = 0.0
        self._age: int = 0
        self._growth_rate: float = growth_rate

        self.set_height(height)
        self.set_age(age)

    def _is_not_negative(self, attr: str, value: int | float) -> bool:
        if value < 0:
            print(f"{self._name}: Error, {attr} can't be negative")
        return value >= 0

    def get_height(self) -> float:
        return self._height

    def set_height(self, value: float) -> None:
        if self._is_not_negative("height", value):
            self._height = value

    def get_age(self) -> int:
        return self._age

    def set_age(self, value: int) -> None:
        if self._is_not_negative("age", value):
            self._age = value

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self, days: int = 1) -> None:
        self.set_height(self._height + self._growth_rate * days)

    def age(self, days: int = 1) -> None:
        self.set_age(self._age + days)
        self.grow(days)
