#!/usr/bin/env python3

import sys
import os.path

def main():
    if len(sys.argv) != 3:
        print("Usage: python sample.py <integer> <integer>")
        exit()   
    a = sys.argv[1]
    b = sys.argv[2]
    print(a+b)
    exit()

if __name__ == "__main__":
    main()
