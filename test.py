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
from day_6.machine import Day6
from day_7.machine import Day7
from day_8.machine import Day8
from day_9.machine import Day9
from day_10.machine import Day10
from day_11.machine import Day11
from day_12.machine import Day12
from day_13.machine import Day13
from day_14.machine import Day14
from day_15.machine import Day15


@pytest.mark.parametrize(
    "input_path,puzzle_number,machine,expected",
    [
        # pytest.param(
        #     os.path.join("day_15", "example.txt"),
        #     1,
        #     Day15,
        #     26,
        #     id="example_1",
        # ),
        # pytest.param(
        #     os.path.join("day_15", "puzzle.txt"),
        #     1,
        #     Day15,
        #     5147333,
        #     id="puzzle_1",
        # ),
        pytest.param(
            os.path.join("day_15", "example.txt"),
            2,
            Day15,
            56000011,
            id="example_2",
        ),
        # pytest.param(
        #     os.path.join("day_15", "puzzle.txt"),
        #     2,
        #     Day15,
        #     False,
        #     id="puzzle_2",
        # ),
    ],
)
def test_day_15(
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
            os.path.join("day_14", "example.txt"),
            1,
            Day14,
            24,
            id="example_1",
        ),
        pytest.param(
            os.path.join("day_14", "puzzle.txt"),
            1,
            Day14,
            False,
            id="puzzle_1",
        ),
        pytest.param(
            os.path.join("day_14", "example.txt"),
            2,
            Day14,
            93,
            id="example_2",
        ),
        pytest.param(
            os.path.join("day_14", "puzzle.txt"),
            2,
            Day14,
            24166,
            id="puzzle_2",
        ),
    ],
)
def test_day_14(
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
            os.path.join("day_13", "example.txt"),
            1,
            Day13,
            13,
            id="example_1",
        ),
        pytest.param(
            os.path.join("day_13", "puzzle.txt"),
            1,
            Day13,
            6101,
            id="puzzle_1",
        ),
        pytest.param(
            os.path.join("day_13", "example.txt"),
            2,
            Day13,
            140,
            id="example_2",
        ),
        pytest.param(
            os.path.join("day_13", "puzzle.txt"),
            2,
            Day13,
            21909,
            id="puzzle_2",
        ),
    ],
)
def test_day_13(
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
        # commented out bc slow
        # pytest.param(
        #     os.path.join("day_12", "puzzle.txt"),
        #     2,
        #     Day12,
        #     377,
        #     id="puzzle_2",
        # ),
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
            os.path.join("day_11", "example.txt"),
            1,
            Day11,
            10605,
            id="example_1",
        ),
        pytest.param(
            os.path.join("day_11", "puzzle.txt"),
            1,
            Day11,
            67830,
            id="puzzle_1",
        ),
        pytest.param(
            os.path.join("day_11", "example.txt"),
            2,
            Day11,
            2713310158,
            id="example_2",
        ),
        pytest.param(
            os.path.join("day_11", "puzzle.txt"),
            2,
            Day11,
            15305381442,
            id="puzzle_2",
        ),
    ],
)
def test_day_11(
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
            os.path.join("day_6", "example_one.txt"),
            1,
            Day6,
            7,
            id="example_1",
        ),
        pytest.param(
            os.path.join("day_6", "example_two.txt"),
            1,
            Day6,
            5,
            id="example_1",
        ),
        pytest.param(
            os.path.join("day_6", "example_three.txt"),
            1,
            Day6,
            6,
            id="example_1",
        ),
        pytest.param(
            os.path.join("day_6", "example_four.txt"),
            1,
            Day6,
            10,
            id="example_1",
        ),
        pytest.param(
            os.path.join("day_6", "example_five.txt"),
            1,
            Day6,
            11,
            id="example_1",
        ),
        pytest.param(
            os.path.join("day_6", "puzzle.txt"),
            1,
            Day6,
            1282,
            id="puzzle_1",
        ),
        pytest.param(
            os.path.join("day_6", "example_one.txt"),
            2,
            Day6,
            19,
            id="example_1",
        ),
        pytest.param(
            os.path.join("day_6", "example_two.txt"),
            2,
            Day6,
            23,
            id="example_1",
        ),
        pytest.param(
            os.path.join("day_6", "example_three.txt"),
            2,
            Day6,
            23,
            id="example_1",
        ),
        pytest.param(
            os.path.join("day_6", "example_four.txt"),
            2,
            Day6,
            29,
            id="example_1",
        ),
        pytest.param(
            os.path.join("day_6", "example_five.txt"),
            2,
            Day6,
            26,
            id="example_1",
        ),
        pytest.param(
            os.path.join("day_6", "puzzle.txt"),
            2,
            Day6,
            False,
            id="puzzle_2",
        ),
    ],
)
def test_day_6(
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
