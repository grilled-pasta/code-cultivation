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

from ex2.plant import Plant


def main() -> None:
    print("=== Plant Factory Output ===")
    plants: list[tuple[str, float, int]] = [
            ("Rose", 25, 30),
            ("Sunflower", 80, 45),
            ("Cactus", 15.5, 120),
            ("Tulip", 3, 0),
            ("Oak", 200, 365)
    ]

    for plant_data in plants:
        plant = Plant(*plant_data)
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    main()
