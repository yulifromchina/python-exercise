#!/usr/bin/env python3

import os

def counter_generator(low, high):
    while low <= high:
        yield low
        low += 1


if __name__ == "__main__":
    for i in counter_generator(5,10):
        print(i, end=' ')
