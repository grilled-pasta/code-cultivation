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

from ex1.plant import Plant


def main() -> None:
    plants: list[tuple[str, int, int]] = [
            ("Rose", 25, 30),
            ("Sunflower", 80, 45),
            ("Cactus", 15, 120)
    ]

    for name, height, age in plants:
        plant = Plant()
        plant.name = name
        plant.height = height
        plant.days = age
        plant.show()


if __name__ == "__main__":
    main()
