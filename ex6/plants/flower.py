# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    flower.py                                         :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: alkonsta <alkonsta@student.codam.nl>      +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/19 12:55:59 by alkonsta         #+#    #+#              #
#    Updated: 2026/11/19 16:40:52 by alkonsta        ###   ########.nl        #
#                                                                             #
# *************************************************************************** #

from .plant import Plant


class Flower(Plant):

    def __init__(self, name: str, height: float, age: int,
                 color: str, growth_rate: float = 1.5):
        super().__init__(name, height, age, growth_rate)
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

    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age, color)
        self._seeds: int = 0

    def bloom(self, seeds: int = 0) -> None:
        super().bloom()
        self._seeds = seeds

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds}")
