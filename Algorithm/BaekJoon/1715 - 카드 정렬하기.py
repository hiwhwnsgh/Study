import sys
import heapq
N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    cardCount = int(sys.stdin.readline())
    heapq.heappush(heap,cardCount)
num1 =heapq.heappop(heap)
num2 =heapq.heappop(heap)
result = num1 + num2
add = num1 + num2
prevNum = num2
while heap:
    nowNum = heapq.heappop(heap)
    add = nowNum + add
    if prevNum + nowNum > add:
        add = prevNum + nowNum
    print(nowNum,add)
    result += add
    prevNum = nowNum
print(result)