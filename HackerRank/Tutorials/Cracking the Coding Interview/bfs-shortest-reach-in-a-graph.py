# https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem

from collections import deque

class Graph:
    def __init__(self, size):
        self.size = size
        self.connections = [[] for i in range(self.size)]

    def connect(self, a, b):
        self.connections[a].append(b)
        self.connections[b].append(a)

    def find_all_distances(self, start):
        """
        BFS

        v = Vertices
        e = Edges

        Time complexity:   O(v + e)
        Space complexity:  O(v)
        """
        distances = [-1 for i in range(self.size)]
        distances[start] = 0
        search_queue = deque()
        search_queue.append(start)

        while search_queue:
            curr = search_queue.popleft()
            adjacents = self.connections[curr]
            for node in adjacents:
                searched = distances[node] != -1
                if not searched:
                    search_queue.append(node)
                    distances[node] = distances[curr] + 6

        del distances[start]
        print(' '.join(map(str, distances)))


t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1)
    s = int(input())
    graph.find_all_distances(s-1)
