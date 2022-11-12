import sys
N = int(sys.stdin.readline())
result = ''
for i in range(0,N,4):
    result += 'long '
result += 'int'
print(result)