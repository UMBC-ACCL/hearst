import sys

for line in sys.stdin:
    c1, c2 = line.rstrip().split('\t')
    sys.stdout.write('{}\t{}\n'.format(c2, c1))

