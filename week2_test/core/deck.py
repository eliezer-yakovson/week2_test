import random

def build_standard_deck() -> list[dict]:
    suites = ["H", "C", "D", "S"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    return [{"rank": r, "suite": s} for s in suites for r in ranks]

def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    n = len(deck)
    for _ in range(swaps):
        i = random.randint(0, n - 1)
        suite = deck[i]["suite"]
        while True:
            j = random.randint(0, n - 1)
            if j == i:
                continue
            if suite == "H" and j % 5 != 0:
                continue
            if suite == "C" and j % 3 != 0:
                continue
            if suite == "D" and j % 2 != 0:
                continue
            if suite == "S" and j % 7 != 0:
                continue
            break
        deck[i], deck[j] = deck[j], deck[i]
    return deck

