import sys

text = sys.stdin.readline()

if text[0] != ' ' and text[-2] != ' ':
    print(text.count(' ') + 1)
elif text[0] == ' ' and text[-2] == ' ':
    print(text.count(' ') - 1)
else:
    print(text.count(' '))