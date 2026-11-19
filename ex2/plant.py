# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    plant.py                                          :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: alkonsta <alkonsta@student.codam.nl>      +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/17 02:41:13 by alkonsta         #+#    #+#              #
#    Updated: 2026/11/19 16:21:31 by alkonsta        ###   ########.nl        #
#                                                                             #
# *************************************************************************** #

class Plant():

    def __init__(self, name: str, height: float, days: int,
                 growth_rate: float = 1.5) -> None:
        self.name: str = name
        self.height: float = height
        self.days: int = days
        self.growth_rate: float = growth_rate

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, " +
              f"{self.days} days old")

    def grow(self, days: int = 1) -> None:
        self.height = round(self.height + self.growth_rate * days, 1)

    def age(self, days: int = 1) -> None:
        self.days += 1 * days
        self.grow(days)
