import sys
# get the shift value from the command line argument
shift = int(sys.argv[1])
message = ""
# read each line from standard input (keyboard)
for line in sys.stdin:
    message += line
# convert the entire message to uppercase
message = message.upper()
# loop through each character in the message
encoded_letters = []
for ch in message:
    # only process letters, ignore spaces, punctuation, numbers, etc.
    if ch.isalpha():
        # shift the letter by the given amount using ASCII values
        # use modulo 26 to wrap around if we go past 'Z'
        new_char = chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        encoded_letters.append(new_char)
# split the encoded letters into blocks of 5
result = ""
block_count = 0
for i in range(0, len(encoded_letters), 5):
    # join the next 5 letters into a block
    block = ''.join(encoded_letters[i:i+5])
    result += block
    block_count += 1
    # print 10 blocks per line then reset
    if block_count == 10:
        print(result.strip())
        result = ""
        block_count = 0
    else:
        # add a space between blocks
        result += " "
# print the last line if there are any remaining letters
if result.strip():
    print(result.strip())
