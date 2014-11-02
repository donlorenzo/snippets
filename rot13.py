#!/usr/bin/env python

import sys
import io
import argparse

def rot(s, n=13):
    characters = []
    for c in s:
        if ord("A") <= ord(c) <= ord("Z"):
            characters.append(chr(((ord(c) - ord("A") + n) % 26) + ord("A")))
        elif ord("a") <= ord(c) <= ord("z"):
            characters.append(chr(((ord(c) - ord("a") + n) % 26) + ord("a")))
        else:
            characters.append(c)
    return "".join(characters)

def rot13(s):
    return rot(s, 13)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", metavar="INFILE", dest="infile", 
                        help="file to read")
    parser.add_argument("-o", "--output", metavar="OUTFILE", dest="outfile",
                        help="file to write")
    parser.add_argument("-n", type=int, default=13, help="rotate by N (default is 13)")
    parser.add_argument("input", nargs="*",
                        help="input")
    args = parser.parse_args()

    if args.input and args.infile:
        print("providing input on the commandline and an "
              "input file is mutually exclusive")
        sys.exit(1)

    if args.infile:
        input = open(args.infile)
    elif args.input:
        input = io.StringIO(u" ".join(args.input))
    else:
        input = sys.stdin
    if args.outfile:
        output = open(args.outfile, "w")
    else:
        output = sys.stdout

    output.write(rot(input.read(), args.n))

    if output != sys.stdout:
        output.close()
    if input != sys.stdin:
        input.close()


if __name__ == '__main__':
    main()

