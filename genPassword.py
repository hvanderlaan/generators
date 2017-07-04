#!/usr/bin/env python

from __future__ import print_function

import sys
import string
import random
import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Random password generator")
    parser.add_argument('-c', '--count', default=1, type=int, help="number of passwords")
    parser.add_argument('-l', '--length', default=8, type=int, help="length of password")

    return parser.parse_args()

def GenChars(length, charSet):
    return '' .join(random.sample(charSet*length, length))

def main():
    args = get_args()
    count = args.count
    length = args.length
    safeSpecials = '~!@#$%^&*()-=_+.:'
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + safeSpecials

    for _ in range(0, count):
        print('{}' .format(GenChars(length, chars)))

if __name__ == "__main__":
    main()
    sys.exit(0)
