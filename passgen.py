#!/usr/bin/env python3

import random
import sys


def get_words(n, min_length=4):
    with open("words.txt", 'r') as f:
        wordlist = f.read()

    words = [
        word for word in wordlist.split('\n')
        if len(word) >= min_length
    ]

    return [
        random.choice(words)
        for i in range(n)
    ]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.stderr.write("Usage: passgen <num_words>\n")
        sys.exit(1)

    words = get_words(int(sys.argv[1]))
    sys.stdout.write("".join(words) + "\n")
    sys.exit(0)
