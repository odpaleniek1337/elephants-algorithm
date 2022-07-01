#/usr/bin/python3

from algo import calculate_result
from util import read_data

def main() -> int:
    elem, mass, places, targets, checked = read_data()
    price = calculate_result(elem, mass, places, targets, checked)
    return price

if __name__ == '__main__':
    main()