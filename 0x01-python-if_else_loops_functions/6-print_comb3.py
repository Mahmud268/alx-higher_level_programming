#!/usr/bin/python3

for i in range(10):
    for j in range(1, 10):
        if i >= j:
            continue
        if j == 9 and i == 8:
            print("{:d}{:d}".format(i, j))
        else:
            print("{:d}{:d}".format(i, j), end=", ")
