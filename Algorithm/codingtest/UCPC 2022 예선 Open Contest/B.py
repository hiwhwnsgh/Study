import sys
result_array = []
result = []
N = int(sys.stdin.readline())
for i in range(N):
    array = []
    x_y = list(map(int,sys.stdin.readline().split()))
    array.append(x_y[2] - x_y[0])
    array.append(x_y[3] - x_y[1])
    result_array.append(array)
for i in range(len(result_array)):
    print(i)
