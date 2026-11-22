#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_garden_data.py                                 :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: alkonsta <alkonsta@student.codam.nl>      +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/17 01:22:13 by alkonsta         #+#    #+#              #
#    Updated: 2026/11/17 01:22:13 by alkonsta        ###   ########.nl        #
#                                                                             #
# *************************************************************************** #

class Plant:

    def __init__(self) -> None:
        self.name: str = ""
        self.height: float = 0.0
        self.age: int = 0

    def show(self) -> None:
        print(f"{self.name}: {self.height:.0f}cm, {self.age} days old")


def main() -> None:
    plants: list[tuple[str, int, int]] = [
            ("Rose", 25, 30),
            ("Sunflower", 80, 45),
            ("Cactus", 15, 120)
    ]

    print("=== Garden Plant Registry ===")
    for name, height, age in plants:
        plant = Plant()
        plant.name = name
        plant.height = height
        plant.age = age
        plant.show()


if __name__ == "__main__":
    main()
