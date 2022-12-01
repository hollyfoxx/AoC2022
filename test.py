from typing import Union
import os
import pytest

from elf_machine import ElfMachine
from day_0.day_0 import Day0
from day_1.day_1 import Day1


@pytest.mark.parametrize(
    "input_path,problem_number,implementation,expected",
    [
        pytest.param(
            os.path.join("day_0", "input_1.txt"),
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
            id="day_1_example",
        ),
    ],
)
def test_implementation(
    input_path: str,
    problem_number: int,
    implementation: ElfMachine,
    expected: Union[int, str],
):
    machine = implementation()
    test_input = machine.read_input(path=input_path)

    if problem_number == 1:
        result = machine.solve_first_problem(test_input)

    if problem_number == 2:
        result = machine.solve_second_problem(test_input)

    assert result == expected
