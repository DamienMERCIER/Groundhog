#!/usr/bin/env python3

from src.groundhog import Groundhog
import sys

def groundhog_day():
    groundhog = Groundhog()
    groundhog.start()

if __name__ == '__main__':
    groundhog_day()