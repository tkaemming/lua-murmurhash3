import itertools
import operator
import subprocess
import sys

import mmh3

path = sys.argv[1]

lua = subprocess.Popen(
    ('lua', 'example.lua'),
    stdin=open(path),
    stdout=subprocess.PIPE,
)

lines = itertools.tee(itertools.imap(operator.methodcaller('rstrip'), open(path)), 2)
streams = itertools.izip(
    lines[0],
    itertools.imap(int, lua.stdout),
    itertools.imap(mmh3.hash, lines[1]),
)

for line, expected, actual in streams:
    print '{:+09x} {:+09x} {} {}'.format(expected, actual, 'y' if expected == actual else 'n', line)
