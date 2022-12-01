from abc import ABC, abstractmethod
from typing import Union


class ElfMachine(ABC):
    def read_input(self, path: str, lines: bool = True):
        with open(path) as f:
            if lines:
                return f.readlines()

            else:
                return f.read()

    @abstractmethod
    def execute(self, input_data: Union[str, list[str]]) -> Union[int, str]:
        pass
