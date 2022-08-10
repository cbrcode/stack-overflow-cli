#!/usr/bin/python3

from sys import argv

def ask(q):
    return q

if __name__ == '__main__':
    question = " ".join(argv[1:])
    print(ask(question))
