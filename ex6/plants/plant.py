# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    plant.py                                          :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: alkonsta <alkonsta@student.codam.nl>      +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/17 02:41:13 by alkonsta         #+#    #+#              #
#    Updated: 2026/11/19 16:00:49 by alkonsta        ###   ########.nl        #
#                                                                             #
# *************************************************************************** #

from ex5.plants import Plant as PlantBase


class Plant(PlantBase):

    class Statistics():
        def __init__(self) -> None:
            self._calls: dict[str, int] = {
                    "grow": 0,
                    "age": 0,
                    "show": 0
                    }

        def log(self, method: str) -> None:
            if method in self._calls:
                self._calls[method] += 1

        def show(self) -> None:
            print(f"Stats: {self._calls["grow"]} grow" +
                  f", {self._calls["age"]} age" +
                  f", {self._calls["show"]} show")

    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float = 1.5) -> None:
        super().__init__(name, height, age, growth_rate)
        self._statistics: Plant.Statistics = self.Statistics()

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def anonymous(cls) -> Plant:
        return cls("Unknown plant", 0, 0)

    def grow(self, days: int = 1) -> None:
        super().grow(days)
        self._statistics.log("grow")

    def age(self, days: int = 1) -> None:
        super().age(days)
        self._statistics.log("age")

    def show(self) -> None:
        super().show()
        self._statistics.log("show")

    def get_statistics(self) -> Plant.Statistics:
        return self._statistics
