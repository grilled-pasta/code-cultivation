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

from ex2.plant import Plant


def main() -> None:
    print("== Garden Plant Growth ===")
    plant = Plant("Rose", 25, 30, 0.4)
    plant.show()
    start_height = plant.height

    for i in range(1, 8):
        print(f"=== Day {i} ===")
        plant.grow()
        plant.age()
        plant.show()
    growth = plant.height - start_height
    print(f"Growth this week: {growth:.1f}cm")


if __name__ == "__main__":
    main()
