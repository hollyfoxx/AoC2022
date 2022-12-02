from elf_machine import ElfMachine


class Day2(ElfMachine):
    def solve_first_puzzle(self, input_data: str) -> int:
        # A/X = ROCK
        # B/Y = PAPER
        # C/Z = SCISSORS

        winning_combos = ["C X", "B Z", "A Y"]
        tie_combos = ["A X", "B Y", "C Z"]

        points_map = {"X": 1, "Y": 2, "Z": 3}

        total_score = 0
        for strategy in input_data.split("\n"):
            if strategy in winning_combos:
                total_score += 6
            elif strategy in tie_combos:
                total_score += 3

            total_score += points_map[strategy.split(" ")[1]]

        return total_score

    def solve_second_puzzle(self, input_data: str) -> str:
        # A = ROCK
        # B = PAPER
        # C = SCISSORS

        # A = LOSE
        # B = DRAW
        # C = WIN

        winning_responses = {
            "A": "B",
            "B": "C",
            "C": "A",
        }
        losing_responses = {"A": "C", "B": "A", "C": "B"}
        points_map = {"A": 1, "B": 2, "C": 3}

        total_score = 0
        for strategy in input_data.split("\n"):
            opponent_move, round_outcome = strategy.split(" ")
            if round_outcome == "X":
                total_score += points_map[losing_responses[opponent_move]]

            if round_outcome == "Y":
                total_score += points_map[opponent_move]
                total_score += 3

            if round_outcome == "Z":
                total_score += points_map[winning_responses[opponent_move]]
                total_score += 6

        return total_score
