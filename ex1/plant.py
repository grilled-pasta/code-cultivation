# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    plant.py                                          :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: alkonsta <alkonsta@student.codam.nl>      +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/17 02:41:13 by alkonsta         #+#    #+#              #
#    Updated: 2026/11/17 02:41:13 by alkonsta        ###   ########.nl        #
#                                                                             #
# *************************************************************************** #

class Plant:

    # PEP-0484 => _init__ returns None + omitting return type is allowed
    def __init__(self) -> None:
        self.name: str = ""
        self.height: float = 0.0
        self.days: int = 0

    def show(self) -> None:
        print(f"{self.name}: {self.height:.0f}cm, {self.days} days old")
