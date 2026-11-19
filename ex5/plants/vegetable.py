# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    vegetable.py                                      :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: alkonsta <alkonsta@student.codam.nl>      +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/19 12:31:42 by alkonsta         #+#    #+#              #
#    Updated: 2026/11/19 16:17:22 by alkonsta        ###   ########.nl        #
#                                                                             #
# *************************************************************************** #

from ex5.plants import Plant


class Vegetable(Plant):

    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, growth_rate: float = 2,
                 nutritional_value: int = 0):
        super().__init__(name, height, age, growth_rate)
        self._harvest_season: str = harvest_season
        self._nutritional_value: int = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season.capitalize()}")
        print(f" Nutritional value: {self._nutritional_value}")

    def grow(self, days: int = 1) -> None:
        super().grow(days)
        self._nutritional_value += 1
