# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    test.py                                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: alkonsta <alkonsta@student.codam.nl>      +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/22 16:14:35 by alkonsta         #+#    #+#              #
#    Updated: 2026/11/22 16:55:47 by alkonsta        ###   ########.nl        #
#                                                                             #
# *************************************************************************** #

import subprocess
from pathlib import Path
import difflib

TEST_DIR = Path(__file__).resolve().parent
PROJECT_DIR = TEST_DIR.parent


def test(exercise: int, name: str) -> bool:
    result = subprocess.run(
            ["python3", f"{PROJECT_DIR}/ex{exercise}/{name}"],
            capture_output=True,
            text=True
            )
    expected = Path(f"{TEST_DIR}/ex{exercise}_expected.txt").read_text()
    actual = result.stdout

    if result.returncode != 0:
        print("ERROR: Program exited with a non-zero status.")
        print(result.stderr)

    elif actual == expected:
        print("PASS")
        return True

    else:
        print("FAIL")
        print("\nDifferences:")

        diff = difflib.unified_diff(
                expected.splitlines(),
                actual.splitlines(),
                fromfile="expected",
                tofile="actual",
                lineterm=""
                )
        print("\n".join(diff))

    if result.stderr:
        print("\nStderr:")
        print(result.stderr)

    return False


def main() -> None:
    files = [
            "ft_garden_intro.py",
            "ft_garden_data.py",
            "ft_plant_growth.py",
            "ft_plant_factory.py",
            "ft_garden_security.py",
            "ft_plant_types.py",
            "ft_garden_analytics.py"
            ]
    for i, filename in enumerate(files):
        print(f"=== EX{i} ===")
        if not test(i, filename):
            break


if __name__ == "__main__":
    main()
