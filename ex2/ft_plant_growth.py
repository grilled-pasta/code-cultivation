#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_plant_growth.py                                :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: alkonsta <alkonsta@student.codam.nl>      +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/17 03:05:55 by alkonsta         #+#    #+#              #
#    Updated: 2026/11/17 03:05:55 by alkonsta        ###   ########.nl        #
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
    print("=== Garden Plant Growth ===")
    plant = Plant("Rose", 25, 30, 0.8)
    plant.show()
    start_height = plant.height

    for i in range(7):
        print(f"=== Day {i + 1} ===")
        plant.grow()
        plant.age()
        plant.show()
    growth = plant.height - start_height
    print(f"Growth this week: {growth:.1f}cm")


if __name__ == "__main__":
    main()
