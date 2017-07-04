#!/usr/bin/env python

from __future__ import print_function

import sys
import string
import random
import argparse

def get_args():
    parser = argparse.ArgumentParser(description="random passphrase generator")
    parser.add_argument('-c', '--count', default=1, type=int, help="amount of passphrases")
    parser.add_argument('-d', '--dictfile', default='/usr/share/dict/words', help="dict file")
    parser.add_argument('-m', '--min', default=4, type=int, help="minimal word length")
    parser.add_argument('-w', '--words', default=4, type=int, help="amount of words")
    parser.add_argument('-x', '--max', default=8, type=int, help="maximum word length")

    return parser.parse_args()

def GetWord(dictFilePath, minWordLength, maxWordLength):
    kMargin = 100
    try:
        inFile = open(dictFilePath, 'r')
        inFile.seek(0, 2)
        fileSize = inFile.tell() - kMargin

        for i in range(1, 1000):
            pointer = random.randint(0, fileSize-kMargin)
            inFile.seek(pointer)
            result = inFile.readline()
            result = inFile.readline()[:-1]
            if ((minWordLength <= len(result) <= maxWordLength) and (string.lower(result[0]) == result[0])):
                break

        inFile.close()
    except:
        result = "Error in function: getWord"

    return result

def GetPass(wordCount, minWordLength, maxWordLength, dictFilePath):
    seperators = "-23456789!@#$%^&*()[]+.,;:"

    try:
        pw = GetWord(dictFilePath, minWordLength, maxWordLength)

        for i in range(1, wordCount):
            pw = pw + random.choice(seperators) + GetWord(dictFilePath, minWordLength, maxWordLength)
    except:
        pw = "Error in functio GetPass"

    return pw + random.choice(seperators)

def main():
    args = get_args()

    for _ in range(0, args.count):
        print('{}' .format(GetPass(args.words, args.min, args.max, args.dictfile)))

if __name__ == "__main__":
    main()
    sys.exit(0)
