graph = {'you':    ['alice', 'bob', 'claire'],
         'bob':    ['anuj', 'peggy', 'you', 'anuj'],
         'alice':  ['peggy'],
         'anuj':   [],
         'peggy':  ['bob', 'you'],
         'thom':   [],
         'claire': ['thom', 'jonny'],
         'jonny':  []}

def dfs_has_path(graph, source, dest):
    """
    v = Vertices
    e = Edges
    d = Depth

    Time complexity:   O(v + e)
    Space complexity:  O(d)
    """
    searched = set()

    def has_path(source, dest):
        if source in searched:
            return False
        searched.add(source)
        if source == dest:
            return True
        for child in graph:
            if has_path(child, dest):
                return True
        return False

    return has_path(source, dest)


# test
print(dfs_has_path(graph, 'you', 'thom'))  # True
print(dfs_has_path(graph, 'you', 'daniel'))  # False
