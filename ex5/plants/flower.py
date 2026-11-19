# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    flower.py                                         :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: alkonsta <alkonsta@student.codam.nl>      +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/19 12:30:48 by alkonsta         #+#    #+#              #
#    Updated: 2026/11/19 16:01:55 by alkonsta        ###   ########.nl        #
#                                                                             #
# *************************************************************************** #

from ex5.plants import Plant


class Flower(Plant):

    def __init__(self, name: str, height: float, age: int,
                 color: str, growth_rate: float = 0.8):
        super().__init__(name, height, age, growth_rate)
        self._color: str = color
        self._bloom: bool = False

    def bloom(self, value: bool) -> None:
        self._bloom = value

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._bloom:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")
