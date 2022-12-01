from typing import Union
import os
import pytest

from elf_machine import ElfMachine
from day_0.day_0 import Day0
from day_1.day_1 import Day1


@pytest.mark.parametrize(
    "input_path,puzzle_number,machine,expected",
    [
        pytest.param(
            os.path.join("day_0", "input.txt"),
            1,
            Day0,
            "hello world",
            id="test",
        ),
        pytest.param(
            os.path.join("day_1", "example.txt"),
            1,
            Day1,
            24000,
            id="day_1_example_1",
        ),
        pytest.param(
            os.path.join("day_1", "puzzle.txt"),
            1,
            Day1,
            71124,
            id="day_1_puzzle_1",
        ),
        pytest.param(
            os.path.join("day_1", "example.txt"),
            2,
            Day1,
            45000,
            id="day_1_example_2",
        ),
        pytest.param(
            os.path.join("day_1", "puzzle.txt"),
            2,
            Day1,
            204639,
            id="day_1_puzzle_2",
        ),
    ],
)
def test_machines(
    input_path: str,
    puzzle_number: int,
    machine: ElfMachine,
    expected: Union[int, str],
):
    machine = machine()
    test_input = machine.read_input(path=input_path)

    if puzzle_number == 1:
        result = machine.solve_first_puzzle(test_input)

    if puzzle_number == 2:
        result = machine.solve_second_puzzle(test_input)

    if expected:
        assert result == expected
        print(f"\nResult: {result}")
    else:
        print(f"\n(WIP) Result: {result}")
