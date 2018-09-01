import sys

#print(sys.argv[1:len(sys.argv)])
if len(sys.argv) > 1:
    i = 1
    while i < len(sys.argv):
        print(sys.argv[i], end=' ')
        i += 1
