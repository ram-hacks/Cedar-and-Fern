import random
import string
# import argparse
from sys import getsizeof


def _gen_random(size):
    """
    Generate a random set of integers that totals to size `size`
    """

    # Return file
    ret = []
    
    while getsizeof(ret) <= size:
        num = (str(random.randint(-2147483648, 2147483647)) + '\n')
        ret += [num]

    return ret


def main():
    """
    Do the things
    """
    # parser = argparse.ArgumentParser()

    # parser.add_argument('-o', '--output-file', action='store', dest='o')

    # TODO: sys.argv these bad boys
    size = 100
    filepath = 'test.txt'

    to_file = _gen_random(size)
    lines = 0

    with open(filepath, 'w') as outfile:
        for line in to_file:
            lines += 1
            print(line)
            outfile.write(str(line))
    print('File written of size %d in %d lines' % (size, lines))


if __name__ == '__main__':
    main()

