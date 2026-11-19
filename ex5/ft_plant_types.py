#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_plant_types.py                                 :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: alkonsta <alkonsta@student.codam.nl>      +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/19 11:42:26 by alkonsta         #+#    #+#              #
#    Updated: 2026/11/19 11:42:26 by alkonsta        ###   ########.nl        #
#                                                                             #
# *************************************************************************** #

from ex5.plants import Flower, Tree, Vegetable


def main():
    print("=== Garden Plant Types ===")

    print("=== Flower")
    flower = Flower("Rose", 15, 10, "red")
    flower.show()
    print("[asking the rose to bloom]")
    flower.bloom(True)
    flower.show()

    print("\n=== Tree")
    tree = Tree("Oak", 200, 365, 5)
    tree.show()
    print("[asking the oak to produce shade]")
    tree.produce_shade()

    print("\n=== Vegetable")
    vegetable = Vegetable("Tomato", 5, 10, "april", 2)
    vegetable.show()
    print("[make tomato grow and age for 20 days]")
    vegetable.age(20)
    vegetable.grow()
    vegetable.show()


if __name__ == "__main__":
    main()
