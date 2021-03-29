
import sys

#
#
# with open('result.txt', 'w') as f:
#     x=input('')
#     f.write(sys.stdin.read())

import sys

print()


def input(self, text):
    print(text)
    arg = sys.stdin.readline()
    self.out_file.write(arg)
    return arg