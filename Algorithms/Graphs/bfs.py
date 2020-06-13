from collections import deque


graph = {'you':    ['alice', 'bob', 'claire'],
         'bob':    ['anuj', 'peggy', 'you', 'anuj'],
         'alice':  ['peggy'],
         'anuj':   [],
         'peggy':  ['bob', 'you'],
         'thom':   [],
         'claire': ['thom', 'jonny'],
         'jonny':  []}

def bfs(graph, wanted):
    """
    v = Vertices
    e = Edges

    Time complexity:   O(v + e)
    Space complexity:  O(v)
    """
    search_queue = deque()
    search_queue += graph.keys()
    searched = set()
    while search_queue:
        node = search_queue.popleft()
        if node not in searched:
            if node == wanted:
                return True
            else:
                searched.add(node)
                search_queue += graph[node]
    return False

def bfs_has_path(graph, source, dest):
    """
    v = Vertices
    e = Edges

    Time complexity:   O(v + e)
    Space complexity:  O()
    """
    searched = set()
    search_queue = deque()
    search_queue += graph.keys()
    while search_queue:
        node = search_queue.popleft()
        if node not in searched:
            if dest in graph[node]:
                return True
            else:
                searched.add(node)
                search_queue += graph[node]
    return False


# test
print(bfs(graph, 'jonny'))  # True
print(bfs(graph, 'daniel'))  # False

print(bfs_has_path(graph, 'you', 'thom'))  # True
print(bfs_has_path(graph, 'you', 'daniel'))  # False
