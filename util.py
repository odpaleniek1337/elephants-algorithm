from typing import Tuple, List, Dict

def read_data() -> Tuple[int, List[int], Dict[int, int]]:
    """Returns number of elements & masses read from stdin and permutations mapped to ints"""
    elements = int(input())
    masses = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    permutations = {int(x): numbers[i] for i, x in enumerate(input().split())}
    return elements, masses, permutations

def output_data(result: int) -> None:
    """Prints output to stdout"""
    print(result)