""" Sum square difference """

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('number', type=int)


def sum_of_squares(limit):
    """ Limit is inclusive """
    result = 0
    for n in range(1, limit+1):
        result += n**2
    return result


def square_of_sum(limit):
    """ Limit is inclusive """
    result = 0
    for n in range(1, limit+1):
        result += n
    return result**2


if __name__ == '__main__':
    args = parser.parse_args()
    difference = abs(square_of_sum(args.number) - sum_of_squares(args.number))
    print('difference:', difference)
