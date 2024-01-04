#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    allfun = dir()
    for i in range(0, len(allfun)):
        if allfun[i][:2] != "__":
            print("{:s}".format(allfun[i]))
