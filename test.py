import os
from typing import Union
from day_0.day_0 import Day0
import pytest

from elf_machine import ElfMachine


@pytest.mark.parametrize(
    "input_path,input_lines,implementation,expected",
    [
        pytest.param(
            os.path.join("day_0", "input_1.txt"),
            False,
            Day0,
            "hello world",
            id="test",
        ),
    ],
)
def test_implementation(
    input_path: str,
    input_lines: bool,
    implementation: ElfMachine,
    expected: Union[int, str],
):
    machine = implementation()
    test_input = machine.read_input(path=input_path, lines=input_lines)
    result = machine.execute(test_input)

    assert result == expected
