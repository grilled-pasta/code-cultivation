# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    tree.py                                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: alkonsta <alkonsta@student.codam.nl>      +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/19 12:31:19 by alkonsta         #+#    #+#              #
#    Updated: 2026/11/19 14:59:42 by alkonsta        ###   ########.nl        #
#                                                                             #
# *************************************************************************** #

from .plant import Plant


class Tree(Plant):

    class Statistics(Plant.Statistics):

        def __init__(self) -> None:
            super().__init__()
            self._calls["shade"] = 0

        def show(self) -> None:
            super().show()
            print(f" {self._calls["shade"]} shade")

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float):
        super().__init__(name, height, age)
        self._trunk_diameter: float = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of {self._height:.1f}cm"
              + f" long and {self._trunk_diameter:.1f}cm wide.")
        self._statistics.log("shade")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter:.1f}cm")
