#!/usr/bin/python3
from collections import deque

def canUnlockAll(boxes):
    n = len(boxes)
    visited = set()
    queue = deque([0])
    while queue:
        box = queue.popleft()
        visited.add(box)

        keys = boxes[box]
        for key in keys:
            if key < n and key not in visited:
                queue.append(key)

    return len(visited) == n
