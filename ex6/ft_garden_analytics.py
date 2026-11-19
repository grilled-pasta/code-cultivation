# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: alkonsta <alkonsta@student.codam.nl>      +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/19 12:25:47 by alkonsta         #+#    #+#              #
#    Updated: 2026/11/19 16:41:25 by alkonsta        ###   ########.nl        #
#                                                                             #
# *************************************************************************** #

from ex6.plants import Tree, Plant, Seed, Flower


def main() -> None:
    print("=== Garden Statistics ===")

    print("=== Check year-old ===")
    print(f"Is 30 days older than a year? {Plant.is_older_than_year(30)}")
    print(f"Is 400 days older than a year? {Plant.is_older_than_year(400)}")

    print("\n=== Flower ===")
    flower = Flower("Rose", 15, 10, "red", 8)
    flower.show()
    print(" [statistics for Rose]")
    flower.get_statistics().show()
    print("[asking the rose to grow and bloom]")
    flower.grow()
    flower.bloom()
    flower.show()
    print(" [statistics for Rose]")
    flower.get_statistics().show()

    print("\n=== Tree ===")
    tree = Tree("Oak", 200, 365, 5)
    tree.show()
    print(" [statistics for Oak]")
    tree.get_statistics().show()
    print(" [asking the oak to produce shade]")
    tree.produce_shade()
    print(" [statistics for Oak]")
    tree.get_statistics().show()

    print("\n=== Seed ===")
    seed = Seed("Sunflower", 80, 45, "yellow")
    seed.show()
    print(" [make sunflower grow, age, and bloom]")
    seed.age(20)
    seed.bloom(42)
    seed.show()
    print(" [statistics for Sunflower]")
    seed.get_statistics().show()

    print("\n=== Anonymous ===")
    anonymous = Plant.anonymous()
    anonymous.show()
    print(" [statistics for Unknown plant]")
    anonymous.get_statistics().show()


if __name__ == "__main__":
    main()
