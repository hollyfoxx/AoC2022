from typing import Union
import os
import pytest

from elf_machine import ElfMachine
from day_0.machine import Day0
from day_1.machine import Day1
from day_2.machine import Day2
from day_3.machine import Day3
from day_4.machine import Day4
from day_5.machine import Day5
from day_7.machine import Day7
from day_8.machine import Day8
from day_9.machine import Day9
from day_10.machine import Day10
from day_12.machine import Day12


@pytest.mark.parametrize(
    "input_path,puzzle_number,machine,expected",
    [
        pytest.param(
            os.path.join("day_12", "example.txt"),
            1,
            Day12,
            31,
            id="example_1",
        ),
        pytest.param(
            os.path.join("day_12", "puzzle.txt"),
            1,
            Day12,
            383,
            id="puzzle_1",
        ),
        pytest.param(
            os.path.join("day_12", "example.txt"),
            2,
            Day12,
            29,
            id="example_2",
        ),
        pytest.param(
            os.path.join("day_12", "puzzle.txt"),
            377,
            Day12,
            False,
            id="puzzle_2",
        ),
    ],
)
def test_day_12(
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


@pytest.mark.parametrize(
    "input_path,puzzle_number,machine,expected",
    [
        pytest.param(
            os.path.join("day_10", "example.txt"),
            1,
            Day10,
            False,
            id="example_1",
        ),
        pytest.param(
            os.path.join("day_10", "example_two.txt"),
            1,
            Day10,
            13140,
            id="example_1",
        ),
        pytest.param(
            os.path.join("day_10", "puzzle.txt"),
            1,
            Day10,
            16060,
            id="puzzle_1",
        ),
        pytest.param(
            os.path.join("day_10", "example_two.txt"),
            2,
            Day10,
            False,
            id="example_2",
        ),
        pytest.param(
            os.path.join("day_10", "puzzle.txt"),
            2,
            Day10,
            False,  # BACEKLHF
            id="puzzle_2",
        ),
    ],
)
def test_day_10(
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


@pytest.mark.parametrize(
    "input_path,puzzle_number,machine,expected",
    [
        pytest.param(
            os.path.join("day_9", "example.txt"),
            1,
            Day9,
            13,
            id="example_1",
        ),
        pytest.param(
            os.path.join("day_9", "example_two.txt"),
            1,
            Day9,
            2,
            id="example_1",
        ),
        pytest.param(
            os.path.join("day_9", "puzzle.txt"),
            1,
            Day9,
            False,
            id="puzzle_1",
        ),
        pytest.param(
            os.path.join("day_9", "example.txt"),
            2,
            Day9,
            1,
            id="example_2",
        ),
        pytest.param(
            os.path.join("day_9", "example_three.txt"),
            2,
            Day9,
            36,
            id="example_2",
        ),
        pytest.param(
            os.path.join("day_9", "puzzle.txt"),
            2,
            Day9,
            2367,
            id="puzzle_2",
        ),
    ],
)
def test_day_9(
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


@pytest.mark.parametrize(
    "input_path,puzzle_number,machine,expected",
    [
        pytest.param(
            os.path.join("day_8", "example.txt"),
            1,
            Day8,
            21,
            id="example_1",
        ),
        pytest.param(
            os.path.join("day_8", "puzzle.txt"),
            1,
            Day8,
            1792,
            id="puzzle_1",
        ),
        pytest.param(
            os.path.join("day_8", "example.txt"),
            2,
            Day8,
            8,
            id="example_2",
        ),
        pytest.param(
            os.path.join("day_8", "puzzle.txt"),
            2,
            Day8,
            334880,
            id="puzzle_2",
        ),
    ],
)
def test_day_8(
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


@pytest.mark.parametrize(
    "input_path,puzzle_number,machine,expected",
    [
        pytest.param(
            os.path.join("day_7", "example.txt"),
            1,
            Day7,
            95437,
            id="example_1",
        ),
        pytest.param(
            os.path.join("day_7", "puzzle.txt"),
            1,
            Day7,
            1648397,
            id="puzzle_1",
        ),
        pytest.param(
            os.path.join("day_7", "example.txt"),
            2,
            Day7,
            24933642,
            id="example_2",
        ),
        pytest.param(
            os.path.join("day_7", "puzzle.txt"),
            2,
            Day7,
            1815525,
            id="puzzle_2",
        ),
    ],
)
def test_day_7(
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


@pytest.mark.parametrize(
    "input_path,puzzle_number,machine,expected",
    [
        pytest.param(
            os.path.join("day_5", "example.txt"),
            1,
            Day5,
            "CMZ",
            id="example_1",
        ),
        pytest.param(
            os.path.join("day_5", "puzzle.txt"),
            1,
            Day5,
            "SVFDLGLWV",
            id="puzzle_1",
        ),
        pytest.param(
            os.path.join("day_5", "example.txt"),
            2,
            Day5,
            "MCD",
            id="example_2",
        ),
        pytest.param(
            os.path.join("day_5", "puzzle.txt"),
            2,
            Day5,
            "DCVTCVPCL",
            id="puzzle_2",
        ),
    ],
)
def test_day_5(
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


@pytest.mark.parametrize(
    "input_path,puzzle_number,machine,expected",
    [
        pytest.param(
            os.path.join("day_4", "example.txt"),
            1,
            Day4,
            2,
            id="example_1",
        ),
        pytest.param(
            os.path.join("day_4", "puzzle.txt"),
            1,
            Day4,
            573,
            id="puzzle_1",
        ),
        pytest.param(
            os.path.join("day_4", "example.txt"),
            2,
            Day4,
            4,
            id="example_2",
        ),
        pytest.param(
            os.path.join("day_4", "puzzle.txt"),
            2,
            Day4,
            867,
            id="puzzle_2",
        ),
    ],
)
def test_day_4(
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


@pytest.mark.parametrize(
    "input_path,puzzle_number,machine,expected",
    [
        pytest.param(
            os.path.join("day_3", "example.txt"),
            1,
            Day3,
            157,
            id="example_1",
        ),
        pytest.param(
            os.path.join("day_3", "puzzle.txt"),
            1,
            Day3,
            7967,
            id="puzzle_1",
        ),
        pytest.param(
            os.path.join("day_3", "example.txt"),
            2,
            Day3,
            70,
            id="example_2",
        ),
        pytest.param(
            os.path.join("day_3", "puzzle.txt"),
            2,
            Day3,
            2716,
            id="puzzle_2",
        ),
    ],
)
def test_day_3(
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


@pytest.mark.parametrize(
    "input_path,puzzle_number,machine,expected",
    [
        pytest.param(
            os.path.join("day_2", "example.txt"),
            1,
            Day2,
            15,
            id="example_1",
        ),
        pytest.param(
            os.path.join("day_2", "puzzle.txt"),
            1,
            Day2,
            14069,
            id="puzzle_1",
        ),
        pytest.param(
            os.path.join("day_2", "example.txt"),
            2,
            Day2,
            12,
            id="example_2",
        ),
        pytest.param(
            os.path.join("day_2", "puzzle.txt"),
            2,
            Day2,
            12411,
            id="puzzle_2",
        ),
    ],
)
def test_day_2(
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


@pytest.mark.parametrize(
    "input_path,puzzle_number,machine,expected",
    [
        pytest.param(
            os.path.join("day_1", "example.txt"),
            1,
            Day1,
            24000,
            id="example_1",
        ),
        pytest.param(
            os.path.join("day_1", "puzzle.txt"),
            1,
            Day1,
            71124,
            id="puzzle_1",
        ),
        pytest.param(
            os.path.join("day_1", "example.txt"),
            2,
            Day1,
            45000,
            id="example_2",
        ),
        pytest.param(
            os.path.join("day_1", "puzzle.txt"),
            2,
            Day1,
            204639,
            id="puzzle_2",
        ),
    ],
)
def test_day_1(
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
    ],
)
def test_tests(
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
