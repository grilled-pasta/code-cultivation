#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_garden_security.py                             :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: alkonsta <alkonsta@student.codam.nl>      +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/17 07:52:27 by alkonsta         #+#    #+#              #
#    Updated: 2026/11/17 07:52:27 by alkonsta        ###   ########.nl        #
#                                                                             #
# *************************************************************************** #

from ex4.plant import Plant


def main() -> None:
    print("=== Garden Security System ===")
    plant = Plant("Rose", -15, 10)
    if plant:
        print("Plant created: ", end="")
        plant.show()
    print()
    plant.set_height(25.0)
    if plant.get_height() == 25:
        print("Height updated: 25cm")
    plant.set_age(30)
    if plant.get_age() == 30:
        print("Age updated: 30 days")
    print()
    plant.set_height(-1)
    if plant.get_height() != -1:
        print("Height update rejected")
    plant.set_age(-1)
    if plant.get_age() != -1:
        print("Age update rejected")
    print()
    print("Current state: ", end="")
    plant.show()


if __name__ == "__main__":
    main()
