import sys
import random
import string


def _gen_random(size):
    """
    Generate a random set of integers that totals to size `size`
    """

    # Return file
    ret = []
    
    # Each integer is 2 bytes, so we take our size (in bytes)
    # and divide by two to find total number of ints we need
    #num = size//2
    num = size
    for i in range(num):
        ret +=(str(random.randint(-2147483648, 2147483647)) + '\n')

    return ret


def main():
    """
    Do the things
    """

    # TODO: sys.argv these bad boys
    size = 1024
    filepath = 'test.txt'

    to_file = _gen_random(size)

    with open(filepath, 'a') as outfile:
        for line in to_file:
            outfile.write(str(line))


if __name__ == '__main__':
    main()

