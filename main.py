#/usr/bin/python3
from algo import calculate_result
from util import read_data, output_data

def main() -> None:
    elements, masses, permutations = read_data()
    price = calculate_result(elements, masses, permutations)
    output_data(price)

if __name__ == '__main__':
    main()