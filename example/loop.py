#!/usr/bin/env python

import time
import os


def main():
    print 'Process running with PID', os.getpid()
    while 1:
        time.sleep(5)


if __name__ == '__main__':
    main()
