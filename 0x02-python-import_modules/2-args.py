#!/usr/bin/python3
import sys
if __name__ == '__main__':
    arbs = sys.argv
    arbs.pop(0)
    arbc = len(args)
    line1 = "{:d} argument".format(arbc)
    if arbc == 0:
        line1 += "s."
    elif arbc == 1:
        line1 += ":"
    else:
        line1 += "s:"
    print(line1)
    for i, arg in enumerate(arbs):
        print("{:d}: {:s}".format(i+1, arg))
