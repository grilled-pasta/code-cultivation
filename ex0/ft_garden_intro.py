#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_garden_intro.py                                :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: alkonsta <alkonsta@student.codam.nl>      +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/17 01:00:16 by alkonsta         #+#    #+#              #
#    Updated: 2026/11/17 01:00:16 by alkonsta        ###   ########.nl        #
#                                                                             #
# *************************************************************************** #

def main() -> None:
    print("=== Welcome to My Graden ===")
    name = 'Rose'
    height = '20cm'
    age = '30 days'
    data = {
            'plant': name,
            'height': height,
            'age': age
            }
    for k, v in data.items():
        print(f"{k.capitalize()}: {v}")
    print("\n=== End of Program ===")


if __name__ == "__main__":
    main()
