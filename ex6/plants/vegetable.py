# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    vegetable.py                                      :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: alkonsta <alkonsta@student.codam.nl>      +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/19 12:31:42 by alkonsta         #+#    #+#              #
#    Updated: 2026/11/19 13:54:17 by alkonsta        ###   ########.nl        #
#                                                                             #
# *************************************************************************** #

from .plant import Plant


class Vegetable(Plant):

    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, nutritional_value: int = 0):
        super().__init__(name, height, age)
        self._harvest_season: str = harvest_season
        self._nutritional_value: int = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season.capitalize()}")
        print(f" Nutritional value: {self._nutritional_value}")

    def grow(self, amount: float = 0.3) -> None:
        super().grow(amount)
        self._nutritional_value += 1
