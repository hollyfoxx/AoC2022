import json
import itertools
from elf_machine import ElfMachine


def _compare_lists(left: list, right: list):
    for l_item, r_item in itertools.zip_longest(left, right):
        res = None
        if l_item is None:
            res = True

        if r_item is None:
            res = False

        if isinstance(l_item, int) and isinstance(r_item, int):
            if l_item < r_item:
                res = True
            elif l_item > r_item:
                res = False

        elif isinstance(l_item, list) and isinstance(r_item, list):
            res = _compare_lists(l_item, r_item)

        elif isinstance(l_item, int) and isinstance(r_item, list):
            res = _compare_lists([l_item], r_item)

        elif isinstance(l_item, list) and isinstance(r_item, int):
            res = _compare_lists(l_item, [r_item])

        if res is not None:
            return res


class Day13(ElfMachine):
    def solve_first_puzzle(self, input_data: str) -> int:
        pairs = input_data.split("\n\n")

        correct_pair_sum = 0
        for index, pair in enumerate(pairs):
            left, right = pair.split("\n")
            left = json.loads(left)
            right = json.loads(right)

            correct_order = _compare_lists(left, right)
            if correct_order:
                correct_pair_sum += index + 1

        return correct_pair_sum

    def solve_second_puzzle(self, input_data: str) -> int:
        class Packet:
            def __init__(self, packet: list):
                self.packet = packet

            def __eq__(self, other):
                return json.dumps(self.packet) == json.dumps(other.packet)

            def __ne__(self, other):
                return not json.dumps(self.packet) == json.dumps(other.packet)

            def __lt__(self, other):
                return _compare_lists(self.packet, other.packet)

        packets = [p for p in input_data.split("\n") if p != ""]
        packets.append("[[2]]")
        packets.append("[[6]]")
        loaded_packets = [Packet(json.loads(p)) for p in packets]

        sorted_packets = [p.packet for p in sorted(loaded_packets)]
        divider_packet_index_a = sorted_packets.index([[2]]) + 1
        divider_packet_index_b = sorted_packets.index([[6]]) + 1

        return divider_packet_index_a * divider_packet_index_b
