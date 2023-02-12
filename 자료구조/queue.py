#queue

from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
# 5 2 3 7
print(queue.popleft())
queue.append(1)
# 2 3 7 1
queue.appendleft(9)
# 9 2 3 7 1
print(queue.pop())

print(queue) # 9 2 3 7
queue.reverse()
print(queue) # 7 3 2 9