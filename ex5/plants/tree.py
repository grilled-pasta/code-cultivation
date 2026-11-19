# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    tree.py                                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: alkonsta <alkonsta@student.codam.nl>      +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/19 12:31:19 by alkonsta         #+#    #+#              #
#    Updated: 2026/11/19 12:38:25 by alkonsta        ###   ########.nl        #
#                                                                             #
# *************************************************************************** #

from ex5.plants import Plant


class Tree(Plant):

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: int):
        super().__init__(name, height, age)
        self._trunk_diameter: int = trunk_diameter

    def produce_shade(self) -> None:
        print(f"{self._name} now produces a shade of {self._height:.1f}cm long"
              + f" and {self._trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}")
