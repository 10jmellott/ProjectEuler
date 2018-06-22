"""Run.py
A startup location to execute all problems
"""

from shared_lib import stopwatch
from problems import p003

print('Project Euler - https://projecteuler.net')

print('Problem 3:')

timer = stopwatch.Timer()
timer.start()

ret = p003.main()

timer.stop()

if ret:
    print('  Solution: {}'.format(ret))

print('  Elapsed: {}'.format(timer.elapsed()))
