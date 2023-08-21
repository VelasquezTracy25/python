# Queues are not the best option if you have a long list because if you try to remove an item from the begining of the list, you will have to move all items over one index (time consuming)
# Deques can be used to remove items from the beginning without having to move all items left one index
# The Deque interface supports insertion, removal and retrieval of elements at both ends.
from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.popleft()
print(queue)
if not queue:
    print("empty")
