#/usr/bin/python3

from algo import calculate_result
from util import read_data, output_data

def main() -> None:
    elements, masses, permutations = read_data()
    checked = [False for x in range(elements)]
    price = calculate_result(elements, masses, permutations, checked)
    output_data(price)

if __name__ == '__main__':
    main()