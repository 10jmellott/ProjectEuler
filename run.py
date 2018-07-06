"""Run.py
A startup location to execute all problems
"""

from utils import stopwatch
from problems.p013 import main

print('Project Euler - https://projecteuler.net')

timer = stopwatch.Timer()
timer.start()

ret = main()

timer.stop()

if ret:
    print('  Solution: {}'.format(ret))

print('  Elapsed: {}'.format(timer.elapsed()))
