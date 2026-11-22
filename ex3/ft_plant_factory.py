#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_plant_factory.py                               :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: alkonsta <alkonsta@student.codam.nl>      +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/17 05:05:35 by alkonsta         #+#    #+#              #
#    Updated: 2026/11/17 05:05:35 by alkonsta        ###   ########.nl        #
#                                                                             #
# *************************************************************************** #

class Plant():

    def __init__(self, name: str, height: float, age: int,
                 growth_per_day: float = 1.5) -> None:
        self.name: str = name
        self.height: float = height
        self._age: int = age
        self.growth_per_day: float = growth_per_day

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        self.height = round(self.height + self.growth_per_day, 1)

    def age(self) -> None:
        self._age += 1


def main() -> None:
    print("=== Plant Factory Output ===")
    plants: list[tuple[str, float, int]] = [
            ("Rose", 25, 30),
            ("Oak", 200, 365),
            ("Cactus", 5, 90),
            ("Sunflower", 80, 45),
            ("Fern", 15, 120)
    ]

    for plant_data in plants:
        plant = Plant(*plant_data)
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    main()
