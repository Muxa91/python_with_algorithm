import sys

old_print = print
f=open('log.txt')

def print(*args, **kwargs):
    old_print("~", *args, "~", **kwargs)
print('govno')
