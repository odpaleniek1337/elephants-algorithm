from typing import Tuple, List

def read_data() -> Tuple[int, List[int], List[int]]:
    """Returns number of elements & masses read from stdin and permutations"""
    elements = int(input())
    masses = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    targets = list(map(int, input().split()))
    permutations = [0 for _ in range(elements)]
    for i in range(elements):
        permutations[targets[i] - 1] = numbers[i]
    return elements, masses, permutations

def output_data(result: int) -> None:
    """Prints output to stdout"""
    print(result)