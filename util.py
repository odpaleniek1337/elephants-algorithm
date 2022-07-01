

def read_data():
    elements = int(input())
    masses = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    target_numbers = list(map(int, input().split()))
    checked = [False for x in range(elements)]
    return elements, masses, numbers, target_numbers, checked