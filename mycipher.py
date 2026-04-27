#!/usr/bin/env python3
import sys

shift = int(sys.argv[1])

letters = []
for line in sys.stdin:
    for ch in line.upper():
        if ch.isalpha():
            encoded = chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            letters.append(encoded)


blocks = [letters[i:i+5] for i in range(0, len(letters), 5)]
lines = [blocks[i:i+10] for i in range(0, len(blocks), 10)]

for line in lines:
    print(' '.join(''.join(b) for b in line))
